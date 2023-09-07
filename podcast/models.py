from ckeditor.fields import RichTextField
from django.db import models

from accounts.models import CustomUser


class MediaCategory(models.Model):
    name = models.CharField(max_length=50)


class Media(models.Model):
    type = models.CharField(max_length=20, choices=[('Video', 'Video'), ('Audio', 'Audio')])
    url = models.URLField()
    content = RichTextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(MediaCategory, on_delete=models.CASCADE)
    status = models.CharField(max_length=20,
                              choices=[('Published', 'Published'), ('Draft', 'Draft'), ('Archived', 'Archived')])
