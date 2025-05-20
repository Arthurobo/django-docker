from django.db import models
from autoslug import AutoSlugField


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='title', unique=True)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_created']
        indexes = [
            models.Index(fields=['-date_created']),
        ]
    