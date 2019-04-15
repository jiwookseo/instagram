from django.db import models
from django.conf import settings


class Post(models.Model):
    content = models.CharField(max_length=150)
    image = models.ImageField(blank=True, upload_to='postings/%Y%m%d')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts", blank=True)
    def __str__(self):
        return self.content
