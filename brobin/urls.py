from django.contrib import admin
from django.contrib.flatpages import views
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.urls import path, include

from .blog.sitemaps import BlogPostSitemap, BlogCategorySitemap
from .blog.views import blog 


sitemaps = {
    'page': FlatPageSitemap,
    'blog_post': BlogPostSitemap,
    'blog_category': BlogCategorySitemap,
}


urlpatterns = [
    path('blog/', include('brobin.blog.urls')),
    path('fishing/', include('brobin.fishing.urls')),
    path('admin/', admin.site.urls),
    path('sitemap\.xml', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    path('<url>/', views.flatpage),
    path('', blog),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
