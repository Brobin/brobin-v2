from rest_framework import serializers

from .models import Category, Post



class PostSerializer(serializers.ModelSerializer):
    preview = serializers.SerializerMethodField()

    def get_preview(self, obj):
        return obj.preview()

    class Meta:
        model = Post
        fields = [
            'id', 'slug', 'created', 'updated', 'title',
            'content', 'category_id', 'author', 'preview'
        ]


class CategorySerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'posts']
