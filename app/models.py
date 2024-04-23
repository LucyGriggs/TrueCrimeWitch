"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.FileField(upload_to='app/static/uploads/')

class Podcasts(models.Model):
    titlepod = models.CharField(max_length=200, unique=True)
    authorpod = models.ForeignKey(User, on_delete=models.CASCADE, related_name='podcast_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    contentpod = models.TextField()
    statuspod = models.IntegerField(choices=STATUS, default=0)
    # urls
    apple = models.CharField(max_length=240)
    spotify = models.CharField(max_length=240)
    spreaker = models.CharField(max_length=240)
    castbox = models.CharField(max_length=240)
    
class Meta:
    ordering = ['-created_on']

def __str__(self):
    return self.title
    
