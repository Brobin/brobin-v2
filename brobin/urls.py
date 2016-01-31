from django.contrib.sitemaps.views import sitemap
from django.contrib.flatpages import views
from django.conf.urls import url, include
from django.contrib import admin
from blog.sitemap import BlogPostSitemap, BlogCategorySitemap, PageSitemap


sitemaps = {
    'page': PageSitemap,
    'blog_post': BlogPostSitemap,
    'blog_category': BlogCategorySitemap,
}


urlpatterns = [
    url(r'^$', views.flatpage, {'url': '/'}),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^(?P<url>.*/)$', views.flatpage),
]
