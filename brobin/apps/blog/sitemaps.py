
from django.contrib.sitemaps import Sitemap

from .models import Post, Category


class BlogPostSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.visible_posts.all()

    def lastmod(self, obj):
        return obj.created


class BlogCategorySitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Category.objects.all()
