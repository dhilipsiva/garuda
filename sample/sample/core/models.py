from sample.core.choices import ArticleStatus

from django.db.models import Model, PositiveSmallIntegerField, TextField, \
    CharField


class Article(Model):
    title = CharField(max_length=280)
    content = TextField()
    status = PositiveSmallIntegerField(
		default=ArticleStatus.UNPUBLISHED, choices=ArticleStatus.CHOICES)
