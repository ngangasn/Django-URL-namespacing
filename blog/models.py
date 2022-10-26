from django.db import models


class BlogPost(models.Model):
    article_title = models.CharField(max_length=80)

    def __str__(self):
        return self.article_title
