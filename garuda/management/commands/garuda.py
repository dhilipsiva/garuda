from ast import parse
from inspect import getsource

from inflect import engine
from orm_choices.core import user_attributes

from django.core.management.base import BaseCommand
from django.apps import apps

plural = engine().plural

GARUDA_SUFFIX = 'Garuda'

# Dict to translate Django fields into Protobuf fields
FIELDS_DICT = dict(
    CharField='string',
    DateTimeField='string',
    BooleanField='bool',
    EmailField='string',
    UUIDField='string',
    ManyToManyField='repeated string',
    TextField='string',
    PositiveSmallIntegerField='int32',
    IntegerField='int64',
    ForeignKey='string',
)

# `KW_INFO` basically says how to extract data from a given ast `Assign` object
KW_INFO = dict(
    Num=lambda kw: kw.value.n,
    Str=lambda kw: kw.value.s,
    Name=lambda kw: kw.value.id,
    NameConstant=lambda kw: kw.value.value,
    Attribute=lambda kw: '%s.%s' % (kw.value.value.id, kw.value.attr),
)

# Fields to ifnore while dictifying
IGNORE_FIELDS = ['created_on', 'updated_on', 'id']

CRUD_CONTENT = '''
from vandal.%(app_name)s.models import %(model_name)s  # NOQA
IGNORE_FIELDS = %(ignore_fields)s  # NOQA
def read_%(model_name_lower)s(*args, **kwargs):
    try:
        return %(model_name)s.objects.get(*args, **kwargs)
    except %(model_name)s.DoesNotExist:
        return None
def read_%(model_name_lower_plural)s_filter(*args, **kwargs):
    return %(model_name)s.objects.filter(*args, **kwargs)
def create_%(model_name_lower)s(*args, **kwargs):
    for ignore_field in IGNORE_FIELDS:
        if ignore_field in kwargs:
            del kwargs[ignore_field]
    for key in list(kwargs):
        if kwargs[key] in [None, 'None', '']:
            del kwargs[key]
    return %(model_name)s.objects.create(*args, **kwargs)
def update_%(model_name_lower)s(id, *args, **kwargs):
    for ignore_field in IGNORE_FIELDS:
        if ignore_field in kwargs:
            del kwargs[ignore_field]
    for key in list(kwargs):
        if kwargs[key] in [None, 'None', '']:
            del kwargs[key]
    return %(model_name)s.objects.filter(id=id).update(*args, **kwargs)
def delete_%(model_name_lower)s(id):
    return %(model_name)s.objects.get(id=id).delete()
'''

RPC_CONTENT = '''
from vandal.proto.vandal_pb2 import %(model_name)s, Void  # NOQA
from vandal.%(app_name)s.auto_crud import (  # NOQA
    read_%(model_name_lower)s,
    delete_%(model_name_lower)s,
    create_%(model_name_lower)s,
    update_%(model_name_lower)s,
    read_%(model_name_lower_plural)s_filter,
)
def %(model_name_lower)s_to_dict(obj):
    # Cycle through fields directly
    d = {  }
    if obj is None:
        return d
    is_dj_obj = obj.__module__.endswith('models')
    foriegn_keys = %(foriegn_keys)s
    for field in %(fields)s:  # NOQA
        value = getattr(obj, field, None)
        if field in [None, 'None']:
            continue
        d[field] = value
        if is_dj_obj and (field == 'id' or field in foriegn_keys):
            d[field] = str(value)
        elif is_dj_obj and field in ['created_on', 'updated_on']:
            d[field] = value.isoformat()
    return d
class %(rpc_name)s:
    def Read%(model_name_plural)sFilter(self, void, context):
        objs = read_%(model_name_lower_plural)s_filter()
        return [%(model_name)s(
            **%(model_name_lower)s_to_dict(obj)) for obj in objs]
    def Read%(model_name)s(self, id, context):
        obj = read_%(model_name_lower)s(id=id.id)
        return %(model_name)s(**%(model_name_lower)s_to_dict(obj))
    def Create%(model_name)s(self, obj, context):
        obj = create_%(model_name_lower)s(**%(model_name_lower)s_to_dict(obj))
        return %(model_name)s(**%(model_name_lower)s_to_dict(obj))
    def Update%(model_name)s(self, obj, context):
        obj_dict = %(model_name_lower)s_to_dict(obj)
        del obj_dict['id']
        obj = update_%(model_name_lower)s(obj.id, **obj_dict)
        return Void()
    def Delete%(model_name)s(self, id, context):
        delete_%(model_name_lower)s(id.id)
        return Void()
'''

GARUDA_RPC_CONTENT = '''
  rpc Delete%(model_name)s(ID) returns (Void);
  rpc Update%(model_name)s(%(model_name)s) returns (Void);
  rpc Read%(model_name)s(ID) returns (%(model_name)s);
  rpc Create%(model_name)s(%(model_name)s) returns (%(model_name)s);
  rpc Read%(model_name_plural)sFilter(Tracker) returns (stream %(model_name)s);
'''


def extract(ast, attrib):
    d = {}
    if ast.__class__.__name__ != "Assign":
        return d
    __import__('ipdb').set_trace()
    for kw in ast.value.keywords:
        if kw.arg != attrib:
            continue
        # If we ever encounter a new Type, uncomment the lines below to debug
        # if kw.value.__class__.__name__ == 'Name':
        #     __import__('pdb').set_trace()
        klass = kw.value.__class__.__name__
        d[ast.targets[0].id] = KW_INFO[klass](kw)
    return d


def process(model, attrib):
    d = {}
    ast = parse(getsource(model))
    ast = ast.body[0]
    print(getsource(model))
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
    which is not somethig\ng we want
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
    return FIELDS_DICT[dj_field_type]


def generate_model(model_name, model):
    fields = model['fields']
    choices = model['choices']
    many_fields = model['many_fields']
    # Every model will have an ID
    fields_declaration = '    string id = 1;'
    field_names = list(fields.keys()) + list(many_fields.keys())

    # remove id which is already in declaration
    for field in ['id', 'deleted']:
        # and we do not need these fields as well
        field_names.remove(field)
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


def write_to_file(app, kind, content, extention='py'):
    comment_prefix = '//'
    if extention in ['py']:
        comment_prefix = '#'
    with open(f"vandal/{app}/auto_{kind}.{extention}", "w") as f:
        print(f'writing to {f.name}...')
        f.write(f'{comment_prefix} DO NOT EDIT THIS FILE MANUALLY\n')
        f.write(f'{comment_prefix} THIS FILE IS AUTO-GENERATED\n')
        f.write(f'{comment_prefix} MANUAL CHANGES WILL BE DISCARDED\n')
        f.write(content.strip())


def codify_model(app_name, model_name, model_defnition):
    fields = sorted(model_defnition['fields'].keys())
    foriegn_keys = sorted(model_defnition['foriegn_keys'])
    fields.remove('deleted')  # Not requred
    ctx = dict(
        app_name=app_name, fields=fields, foriegn_keys=foriegn_keys,
        ignore_fields=IGNORE_FIELDS)
    ctx.update(model_defnition['inflections'])
    return CRUD_CONTENT % ctx, RPC_CONTENT % ctx


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


def generate_vandal_rpc(app_models):
    content = ''
    for app in app_models:
        models = app_models[app]
        for model in models:
            content += GARUDA_RPC_CONTENT % models[model]['inflections']
        v = __import__(f'vandal.{app}.rpc')
        rpc_module = getattr(v, app).rpc
        rpc_class_names = list(
            filter(lambda x: x.endswith('RPC'), dir(rpc_module)))
        for rpc_class_name in rpc_class_names:
            rpc_class = getattr(rpc_module, rpc_class_name)
            for attribute in user_attributes(rpc_class):
                content += '  %s\n' % getattr(rpc_class, attribute).__doc__
    return content


def generate_auto_vandal(app_models):
    content = ''
    models = []
    for app in app_models:
        _models = [
            f'%s%s' % (model, GARUDA_SUFFIX)
            for model in app_models[app].keys()]
        models += _models
        _models = ", ".join(_models)
        content += f'\nfrom vandal.{app}.auto_rpc import {_models}  # NOQA'
    models = ", ".join(models)
    content += f'\n\nclass AutoVandal({models}):  # NOQA\n    pass'
    with open("vandal/rpc/management/commands/auto_vandal.py", "w") as f:
        print(f'writing to {f.name}')
        f.write(content)


class Command(BaseCommand):
    help = 'Generate proto files'

    def handle(self, *args, **options):
        app_models = process_apps()
        generate_rpc_code(app_models)
        generate_auto_vandal(app_models)
        CHOICES_PROTO = generate_choices_proto()
        MODELS_PROTO = generate_model_proto(app_models)
        PROTO_HEADER = open('vandal/proto/messages.proto', 'r').read()
        PROTO_FOOTER = open('vandal/proto/services.proto', 'r').read()

        try:
            GARUDA_RPC = "service Vandal{%s}" % generate_vandal_rpc(app_models)
        except ImportError:
            GARUDA_RPC = ''
            print('ERROR: PLEASE RUN THIS COMMAND AGAIN... ')
            print('BECAUSE A NEW MODEL HAS BEEN ADDED!!!')
        with open('vandal/proto/vandal.proto', 'w') as f:
            print(f'writing to {f.name}...')
            f.write(f'''
{PROTO_HEADER}
{CHOICES_PROTO}
{MODELS_PROTO}
{GARUDA_RPC}
{PROTO_FOOTER}
                    '''.strip())
