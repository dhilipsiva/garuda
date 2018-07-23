import os
import re
from ast import parse
from inspect import getsource
from importlib import import_module

from inflect import engine
from orm_choices.core import user_attributes

from django.apps import apps
from django.conf import settings
from django.core.management.base import BaseCommand

from garuda.constants import GARUDA_SUFFIX, GARUDA_FIELDS, GARUDA_AST_MAP, \
    GARUDA_IGNORE_FIELDS, GARUDA_RPC_METHODS, GARUDA_CRUD_TEMPLATE, \
    GARUDA_RPC_CONTENT, GARUDA_REMOVE_FIELDS, GARUDA_DIR, \
    GARUDA_PROTO_HEADER, GARUDA_PROTO_FOOTER

plural = engine().plural
CHOICES = import_module(settings.GARUDA_CHOICES)

if not os.path.exists(GARUDA_DIR):
    os.makedirs(GARUDA_DIR)


def extract(ast, attrib):
    d = {}
    if ast.__class__.__name__ != "Assign":
        return d
    if ast.value.__class__.__name__ == "List":
        # FIXME: Need to handle this the proper way.
        # Not sure what to do with this one yet.
        return d
    for kw in ast.value.keywords:
        if kw.arg != attrib:
            continue
        # If we ever encounter a new Type, uncomment the lines below to debug
        if kw.value.__class__.__name__ == 'List':
            __import__('pdb').set_trace()
        klass = kw.value.__class__.__name__
        d[ast.targets[0].id] = GARUDA_AST_MAP[klass](kw)
    return d


def process(model, attrib):
    d = {}
    ast = parse(getsource(model))
    ast = ast.body[0]
    for sub_ast in ast.body:
        d.update(extract(sub_ast, attrib))
    return d


def get_inflections(model_name):
    return dict(
        model_name=model_name,
        model_name_lower=model_name.lower(),
        model_name_plural=plural(model_name),
        model_name_lower_plural=plural(model_name.lower()),
        rpc_name=model_name + GARUDA_SUFFIX,
    )


def hacky_m2one_name(field):
    '''
    This is a Hacky, Hacky method to get name.
    field.related_model.__class__.__name__ somehow returns `BaseModel`
    which is not somethig we want
    '''
    return str(field.related_model).split(".")[-1].split("'")[0]


def process_model(model):
    fields = {}
    many_fields = {}
    foriegn_keys = []
    choices = process(model, 'choices')
    defaults = process(model, 'default')
    inflections = get_inflections(model.__name__)
    for field in model._meta.get_fields():
        f_name = field.__class__.__name__
        if f_name == 'ManyToOneRel':
            many_fields[field.name] = hacky_m2one_name(field)
        elif f_name == 'ForeignKey':
            name = f'{field.name}_id'
            fields[name] = f_name
            foriegn_keys.append(name)
        else:
            fields[field.name] = f_name
    return dict(
        choices=choices, fields=fields, defaults=defaults,
        inflections=inflections, foriegn_keys=foriegn_keys,
        many_fields=many_fields)


def process_app(app):
    models = {}
    for model in app.get_models():
        models[model.__name__] = process_model(model)
    return models


def process_apps():
    app_models = {}
    for app in apps.get_app_configs():
        app_models[app.name] = process_app(app)
    return app_models


def get_rpc_type(field, fields, choices, many_fields):
    if field in many_fields:
        return 'repeated string'  # ManyToOneRel fields
    if field in choices:
        return choices[field].split(".")[0]
    dj_field_type = fields[field]
    return GARUDA_FIELDS[dj_field_type]


def generate_model(model_name, model):
    fields = model['fields']
    choices = model['choices']
    many_fields = model['many_fields']
    # Every model will have an ID
    fields_declaration = '    string id = 1;'
    field_names = list(fields.keys()) + list(many_fields.keys())

    # remove id which is already in declaration
    if 'id' in field_names:
        field_names.remove('id')
    for idx, field in enumerate(sorted(field_names)):
        field_type = get_rpc_type(field, fields, choices, many_fields)
        fields_declaration += f'\n    {field_type} {field} = {idx + 2};'
    defnition = '\nmessage %s {\n%s\n}\n' % (
        model_name, fields_declaration)
    return defnition


def generate_app(app, models):
    app_defnition = ''
    for model_name, model in models.items():
        app_defnition += generate_model(model_name, model)
    return app_defnition


def generate_model_proto(app_models):
    model_protos = ''
    for app, models in app_models.items():
        model_protos += generate_app(app, models)
    return model_protos


def generate_choices_proto():
    choices_proto = ''
    for attr in dir(CHOICES):
        choices = getattr(CHOICES, attr)
        if not hasattr(choices, 'CHOICES'):
            continue
        choices_declaration = f'\n    {choices.__name__}UNKNOWN = 0;'
        attrs = user_attributes(choices.Meta)
        if 'UNKNOWN' in attrs:
            attrs.remove('UNKNOWN')
        c_dict = {}
        for attr in attrs:
            value = getattr(choices.Meta, attr)[0]
            c_dict.update({attr: value})
        c_list = sorted(c_dict.items(), key=lambda x: x[1])
        for key, value in c_list:
            choices_declaration += f'\n    {key} = {value};'
        choices_proto += '\nenum %s {%s\n}\n' % (
            choices.__name__, choices_declaration)
    return choices_proto


def sluggify(app):
    return re.sub('[^0-9a-zA-Z]+', '_', app)


def write_to_file(app, kind, content, extention='py'):
    app = sluggify(app)
    comment_prefix = '//'
    if extention in ['py']:
        comment_prefix = '#'
    with open(f"{GARUDA_DIR}/{app}_{kind}.{extention}", "w") as f:
        print(f'writing to {f.name} ...')
        f.write(f'{comment_prefix} DO NOT EDIT THIS FILE MANUALLY\n')
        f.write(f'{comment_prefix} THIS FILE IS AUTO-GENERATED\n')
        f.write(f'{comment_prefix} MANUAL CHANGES WILL BE DISCARDED\n')
        f.write(f'{comment_prefix} PLEASE READ GARUDA DOCS\n')
        f.write(content.strip())


def codify_model(app, model_name, model_defnition):
    fields = sorted(model_defnition['fields'].keys())
    foriegn_keys = sorted(model_defnition['foriegn_keys'])
    for field in GARUDA_REMOVE_FIELDS:
        fields.remove(field)
    ctx = dict(
        app=app, fields=fields, foriegn_keys=foriegn_keys,
        ignore_fields=GARUDA_IGNORE_FIELDS, GARUDA_DIR=GARUDA_DIR)
    ctx.update(model_defnition['inflections'])
    return GARUDA_CRUD_TEMPLATE % ctx, GARUDA_RPC_METHODS % ctx


def codify_app(app, models):
    crud_contents = ''
    rpc_contents = ''
    for model in models.keys():
        crud_content, rpc_content = codify_model(app, model, models[model])
        crud_contents += crud_content
        rpc_contents += rpc_content
    write_to_file(app, 'rpc', rpc_contents)
    write_to_file(app, 'crud', crud_contents)


def generate_rpc_code(app_models):
    for app in app_models.keys():
        codify_app(app, app_models[app])


def generate_garuda_rpc(app_models):
    content = ''
    for app in app_models:
        models = app_models[app]
        for model in models:
            content += GARUDA_RPC_CONTENT % models[model]['inflections']
        try:
            v = __import__(f'{app}.rpc')
        except ImportError:
            print(f'No Custom RPC declaration in {app}')
            # print('ERROR: PLEASE RUN THIS COMMAND AGAIN ... ')
            # print('PROBABLY BECAUSE A NEW MODEL HAS BEEN ADDED !!!')
            continue
        rpc_module = getattr(v, app).rpc
        rpc_class_names = list(
            filter(lambda x: x.endswith('RPC'), dir(rpc_module)))
        for rpc_class_name in rpc_class_names:
            rpc_class = getattr(rpc_module, rpc_class_name)
            for attribute in user_attributes(rpc_class):
                content += '  %s\n' % getattr(rpc_class, attribute).__doc__
    return content


def generate_auto_garuda(app_models):
    content = ''
    models = []
    for app in app_models:
        _models = [
            f'%s%s' % (model, GARUDA_SUFFIX)
            for model in app_models[app].keys()]
        models += _models
        _models = ", ".join(_models)
        app = sluggify(app)
        content += f'\nfrom {GARUDA_DIR}.{app} import {_models}  # NOQA'
    models = ", ".join(models)
    content += f'\n\nclass AutoGaruda({models}):  # NOQA\n    pass'
    with open(f"{GARUDA_DIR}/garuda_server.py", "w") as f:
        print(f'writing to {f.name}')
        f.write(content)


class Command(BaseCommand):
    help = 'Generate proto files'

    def handle(self, *args, **options):
        app_models = process_apps()
        generate_rpc_code(app_models)
        generate_auto_garuda(app_models)
        CHOICES_PROTO = generate_choices_proto()
        MODELS_PROTO = generate_model_proto(app_models)
        GARUDA_RPC = "service Garuda{%s}" % generate_garuda_rpc(app_models)
        with open(f'{GARUDA_DIR}/garuda.proto', 'w') as f:
            print(f'writing to {f.name} ...')
            f.write(f'''
{GARUDA_PROTO_HEADER}
{CHOICES_PROTO}
{MODELS_PROTO}
{GARUDA_RPC}
{GARUDA_PROTO_FOOTER}
                    '''.strip())
