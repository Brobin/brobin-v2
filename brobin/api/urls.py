
from django.urls import path, include
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('blog/', include('brobin.apps.blog.urls')),
    path('cookbook/', include('brobin.apps.cookbook.urls'))
]
