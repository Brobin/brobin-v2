
from rest_framework.routers import DefaultRouter

from brobin.apps.blog.views import CategoryViewSet, PostViewSet


router = DefaultRouter()

router.register('blog/categories', CategoryViewSet, basename='category')
router.register('blog/posts', PostViewSet, basename='post')

urlpatterns = router.urls

