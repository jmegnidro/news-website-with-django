from django.db import models

from accounts.models import CustomUser


class NewsletterSubscription(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField()
