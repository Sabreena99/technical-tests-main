from django.db import models

class Post(models.Model):
    slug = models.TextField(unique=True, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(unique=True, blank=True, null=True)
    date = models.DateField(unique=True, blank=True, null=True)
    author_1 = models.TextField(unique=True, blank=True, null=True)
    author_2 = models.TextField(unique=True, blank=True, null=True)
    author_3 = models.TextField(unique=True, blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    image_alt = models.TextField(unique=True, blank=True, null=True)
