from django.db import models


class PostManager(models.Manager):

    def get_queryset(self):
        posts = super(PostManager, self).get_queryset()
        return posts.order_by('-created')


class VisiblePostManager(PostManager):

    def get_queryset(self):
        posts = super(VisiblePostManager, self).get_queryset()
        return posts.filter(visible=True)
