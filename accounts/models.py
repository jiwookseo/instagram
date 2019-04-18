from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='profile/%Y%m%d', default='profile/default.jpg')
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=40, blank=True)

class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followings")
