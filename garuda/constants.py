from django.conf import settings


def default(var_name, value):
    if hasattr(settings, var_name):
        return getattr(settings, var_name)
    return value


GARUDA_DIR = default('GARUDA_DIR', 'garuda_dir')
GARUDA_SUFFIX = default('GARUDA_SUFFIX', 'Garuda')

# Fields to ifnore while dictifying
GARUDA_IGNORE_FIELDS = default(
    'GARUDA_IGNORE_FIELDS', ['created_on', 'updated_on', 'id'])

# Fields to remove while generating model
GARUDA_REMOVE_FIELDS = default('GARUDA_REMOVE_FIELDS', [])

# Dict to translate Django fields into Protobuf fields
GARUDA_FIELDS = default('GARUDA_FIELDS', dict(
    CharField='string',
    DateTimeField='string',
    BooleanField='bool',
    EmailField='string',
    UUIDField='string',
    ManyToManyField='repeated string',
    ManyToManyRel='repeated string',
    TextField='string',
    PositiveSmallIntegerField='int32',
    IntegerField='int64',
    ForeignKey='int64',
    AutoField='int64',
))

# `GARUDA_AST_MAP` basically says how to extract data
# from a given AST `Assign` object
GARUDA_AST_MAP = default('GARUDA_AST_MAP', dict(
    Num=lambda kw: kw.value.n,
    Str=lambda kw: kw.value.s,
    Name=lambda kw: kw.value.id,
    NameConstant=lambda kw: kw.value.value,
    Attribute=lambda kw: '%s.%s' % (kw.value.value.id, kw.value.attr),
))

GARUDA_PROTO_HEADER = default('GARUDA_PROTO_HEADER', '''
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.dhilipsiva.garuda";
option java_outer_classname = "GarudaProto";
option objc_class_prefix = "DSG";

package garuda;

message Void {}

message ID {
    int64 id = 1;
}
''')
GARUDA_PROTO_FOOTER = default('GARUDA_PROTO_FOOTER', '')

GARUDA_CRUD_TEMPLATE = default('GARUDA_CRUD_TEMPLATE', '''
from %(app)s.models import %(model_name)s  # NOQA
GARUDA_IGNORE_FIELDS = %(ignore_fields)s  # NOQA


def read_%(model_name_lower)s(*args, **kwargs):
    try:
        return %(model_name)s.objects.get(*args, **kwargs)
    except %(model_name)s.DoesNotExist:
        return None


def read_%(model_name_lower_plural)s_filter(*args, **kwargs):
    return %(model_name)s.objects.filter(*args, **kwargs)


def create_%(model_name_lower)s(*args, **kwargs):
    for ignore_field in GARUDA_IGNORE_FIELDS:
        if ignore_field in kwargs:
            del kwargs[ignore_field]
    for key in list(kwargs):
        if kwargs[key] in [None, 'None', '']:
            del kwargs[key]
    return %(model_name)s.objects.create(*args, **kwargs)


def update_%(model_name_lower)s(id, *args, **kwargs):
    for ignore_field in GARUDA_IGNORE_FIELDS:
        if ignore_field in kwargs:
            del kwargs[ignore_field]
    for key in list(kwargs):
        if kwargs[key] in [None, 'None', '']:
            del kwargs[key]
    return %(model_name)s.objects.filter(id=id).update(*args, **kwargs)


def delete_%(model_name_lower)s(id):
    return %(model_name)s.objects.get(id=id).delete()
''')

GARUDA_RPC_METHODS = default('GARUDA_RPC_METHODS', '''
from %(GARUDA_DIR)s.garuda_pb2 import %(model_name)s, Void  # NOQA
from %(app)s.auto_crud import (  # NOQA
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
''')

GARUDA_RPC_CONTENT = default('GARUDA_RPC_CONTENT', '''
  rpc Delete%(model_name)s(ID) returns (Void);
  rpc Update%(model_name)s(%(model_name)s) returns (Void);
  rpc Read%(model_name)s(ID) returns (%(model_name)s);
  rpc Create%(model_name)s(%(model_name)s) returns (%(model_name)s);
  rpc Read%(model_name_plural)sFilter(Void) returns (stream %(model_name)s);
''')
