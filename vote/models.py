from django.db import models

from accounts.models import CustomUser
from article.models import Article
from podcast.models import Media


class Rating(models.Model):
    score = models.IntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    media = models.ForeignKey(Media, on_delete=models.CASCADE, null=True, blank=True)
