from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class PostDetailView(RetrieveAPIView):
    serializer_class = PostSerializer

    def get_object(self, *args, **kwargs):
        return get_object_or_404(Post, slug=self.kwargs.get('slug'))

class PostListView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.visible_posts.all()


class PostArchiveListView(PostListView):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset().filter(created__year=self.kwargs.get('year'))


class PostCategoryListView(PostListView):

    def get_queryset(self, *args, **kwargs):
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        categories = category.get_children()
        return super().get_queryset().filter(category__in=categories)
