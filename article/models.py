from ckeditor.fields import RichTextField
from django.db import models

from accounts.models import CustomUser
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    thumbail = models.ImageField(upload_to='articles')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = RichTextField()
    date_published = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=20,
                              choices=[('Published', 'Published'), ('Draft', 'Draft'), ('Archived', 'Archived')])
    is_featured = models.BooleanField(default=False)
    en_vedette = models.BooleanField(default=False)
    is_special = models.BooleanField(default=False)
    alerte_info = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_published']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    @property
    def author_or_default(self):
        return self.author.username if self.author else "L'auteur inconnu"