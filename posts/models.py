from django.db import models

class Post(models.Model):
    content = models.CharField(max_length=150)
    image = models.ImageField(blank=True, upload_to='postings/%Y%m%d')
    def __str__(self):
        return self.content
