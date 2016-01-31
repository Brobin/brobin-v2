from django.contrib.flatpages.models import FlatPage
from django.contrib.sitemaps import Sitemap
from blog.models import Post, Category


class BlogPostSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.created


class BlogCategorySitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Category.objects.all()


class PageSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return FlatPage.objects.all()
