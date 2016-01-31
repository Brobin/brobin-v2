from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.html import strip_tags


class Category(models.Model):
    title = models.CharField(max_length=32)
    slug = models.SlugField(default='', blank=True, max_length=64)
    parent = models.ForeignKey("self", null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_children(self):
        categories = [self]
        for cat in Category.objects.filter(parent=self):
            categories += cat.get_children()
        return categories

    @property
    def url(self):
        return '/blog/{0}'.format(self.slug)

    def get_absolute_url(self):
        return self.url

    class Meta:
        verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(default='', blank=True, max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    author = models.ForeignKey(User)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def preview(self):
        try:
            preview = strip_tags(self.content)[:400]
        except:
            preview = ''
        return preview + '...'
    preview.short_description = 'content'

    def get_date(self):
        return self.created
    get_date.short_description = 'date'

    @property
    def url(self):
        return '/blog/{0}/{1:02d}/{2}/'.format(self.created.year, self.created.month, self.slug)

    def get_absolute_url(self):
        return self.url
