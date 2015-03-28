from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager
import re


class Post(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(default='', blank=True, max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    author = models.ForeignKey(User)
    tags = TaggableManager()

    def __str__(self):
        return '{0} - {1}'.format(self.created, self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def preview(self):
        try:
            preview = re.findall('<p>(.*?)<\/p>', self.content)[0][:600]
        except:
            preview = ''
        if len(preview) == 600:
            preview += '...'
        return preview

class Page(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(default='', blank=True, max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    script = models.TextField(default='', blank=True)
    style = models.TextField(default='', blank=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title
