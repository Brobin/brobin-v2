from django.contrib.sitemaps import Sitemap
from blog.models import Page, Post


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.created


class BrobinSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Page.objects.all()

    def lastmod(self, obj):
        return obj.created
