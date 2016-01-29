from django.contrib.flatpages import views
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^$', views.flatpage, {'url': '/'}),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<url>.*/)$', views.flatpage),
]
