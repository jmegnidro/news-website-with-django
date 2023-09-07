from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    role = models.CharField(max_length=20, choices=[('Admin', 'Admin'), ('Author', 'Author'), ('Reader', 'Reader')])


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    telephone = PhoneNumberField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    social_media = models.JSONField(blank=True, null=True)

    def display_last_login(self):
        return self.user.last_login.strftime('%Y-%m-%d %H:%M:%S')

    def display_date_joined(self):
        return self.user.date_joined.strftime('%Y-%m-%d %H:%M:%S')