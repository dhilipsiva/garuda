from orm_choices import choices

@choices
class ArticleStatus:
    class Meta:
        UNPUBLISHED = [0, "Not published yet"]
        PUBLISHED = [1, "Published"]
        REVIEW_REQUIRED = [2, "To be reviewed"]
        DELETED = [3, "Deleted"]
