
from garuda_dir.django_contrib_admin import LogEntryGaruda  # NOQA
from garuda_dir.django_contrib_auth import PermissionGaruda, GroupGaruda, UserGaruda  # NOQA
from garuda_dir.django_contrib_contenttypes import ContentTypeGaruda  # NOQA
from garuda_dir.django_contrib_sessions import SessionGaruda  # NOQA
from garuda_dir.django_contrib_messages import   # NOQA
from garuda_dir.django_contrib_staticfiles import   # NOQA
from garuda_dir.garuda import   # NOQA
from garuda_dir.sample_core import ArticleGaruda  # NOQA

class AutoGaruda(LogEntryGaruda, PermissionGaruda, GroupGaruda, UserGaruda, ContentTypeGaruda, SessionGaruda, ArticleGaruda):  # NOQA
    pass