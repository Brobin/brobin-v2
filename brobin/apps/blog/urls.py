from django.urls import path

from .views import (
    PostListView,
    PostArchiveListView,
    PostCategoryListView,
    PostDetailView,
    PostSearchListView,
    SidebarAPIView
)

urlpatterns = [
    path('search', PostSearchListView.as_view()),
    path('sidebar', SidebarAPIView.as_view()),
    path('archive/<int:year>', PostArchiveListView.as_view()),
    path('<int:year>/<int:month>/<str:slug>', PostDetailView.as_view()),
    path('<str:slug>', PostCategoryListView.as_view()),
    path('', PostListView.as_view())
]
