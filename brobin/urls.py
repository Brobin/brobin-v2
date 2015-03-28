from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views


urlpatterns = patterns('',

    url(r'^$', views.home),
    url(r'^blog/$', views.blog),
    url(r'^blog/tag/(.*)$', views.blog_tag),
    url(r'^blog/[0-9]*\/[0-9]*\/(.*)$', views.blog_post),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(.*)$', views.page),
)

handler404 = views.not_found
