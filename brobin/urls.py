from django.conf.urls import patterns, include, url
from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
from blog import views
from blog.sitemap import BlogSitemap, BrobinSitemap


sitemaps = {
    'brobin': BrobinSitemap,
    'blog': BlogSitemap,
}

urlpatterns = patterns('',

    url(r'^$', views.home),
    url(r'^blog/$', views.blog),
    url(r'^blog/tag/(.*)$', views.blog_tag),
    url(r'^blog/[0-9]*\/[0-9]*\/[0-9]*\/(.*)$', views.blog_post),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^(.*)$', views.page),
)

handler404 = views.not_found
