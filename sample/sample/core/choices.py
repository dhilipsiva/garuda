from orm_choices import choices

@choices
class ArticleStatus:
    class Meta:
        UNPUBLISHED = [1, "Not published yet"]
        PUBLISHED = [2, "Published"]
        REVIEW_REQUIRED = [3, "To be reviewed"]
        DELETED = [4, "Deleted"]
