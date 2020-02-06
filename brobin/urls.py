from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.flatpages import views
from django.contrib.sitemaps.views import sitemap
from django.conf.urls import url, include
from django.contrib import admin

from .blog.sitemaps import BlogPostSitemap, BlogCategorySitemap


sitemaps = {
    'page': FlatPageSitemap,
    'blog_post': BlogPostSitemap,
    'blog_category': BlogCategorySitemap,
}


urlpatterns = [
    url(r'^$', views.flatpage, {'url': '/'}),
    url(r'^blog/', include('brobin.blog.urls')),
    url(r'^fishing/', include('brobin.fishing.urls')),
    url(r'^nhl/', include('brobin.nhl.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^(?P<url>.*/)$', views.flatpage),
]

from django.conf import settings
from django.conf.urls import include, url

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
