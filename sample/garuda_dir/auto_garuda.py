
from garuda_dir.django_contrib_admin_rpc import LogEntryGaruda  # NOQA
from garuda_dir.django_contrib_auth_rpc import PermissionGaruda, GroupGaruda, UserGaruda  # NOQA
from garuda_dir.django_contrib_contenttypes_rpc import ContentTypeGaruda  # NOQA
from garuda_dir.django_contrib_sessions_rpc import SessionGaruda  # NOQA
from garuda_dir.sample_core_rpc import ArticleGaruda  # NOQA

class AutoGaruda(LogEntryGaruda, PermissionGaruda, GroupGaruda, UserGaruda, ContentTypeGaruda, SessionGaruda, ArticleGaruda):  # NOQA
    pass