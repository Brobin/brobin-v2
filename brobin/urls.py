from django.contrib import admin
from django.contrib.flatpages import views
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('api', include('brobin.api.urls')),
    path('blog/', include('brobin.apps.blog.urls')),
    path('cookbook/', include('brobin.apps.cookbook.urls')),
    path('fishing/', include('brobin.apps.fishing.urls')),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
