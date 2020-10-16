from django.contrib import admin
from django.contrib.flatpages import views
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.urls import path, include, re_path
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('brobin.api.urls')),
    re_path(r'^(?:.*)/?$', TemplateView.as_view(template_name='index.html')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
