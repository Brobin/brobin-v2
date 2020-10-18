
from django.urls import path
from rest_framework.routers import DefaultRouter

from brobin.apps.blog.urls import urlpatterns as blog_urls


urlpatterns = blog_urls

