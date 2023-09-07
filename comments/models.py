from ckeditor.fields import RichTextField
from django.db import models

from accounts.models import CustomUser
from article.models import Article
from podcast.models import Media


class Comment(models.Model):
    content = RichTextField()
    date_published = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    media = models.ForeignKey(Media, on_delete=models.CASCADE, null=True, blank=True)
