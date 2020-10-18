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
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']


class SidebarPostSerializer(PostSerializer):
    class Meta:
        model = Post
        fields = ['id', 'slug', 'title', 'created']


class ArchiveSerializer(serializers.Serializer):
    year = serializers.SerializerMethodField()
    posts = serializers.IntegerField()

    def get_year(self, obj):
        return obj.get('created__year')


class SidebarSerializer(serializers.Serializer):
    recent = SidebarPostSerializer(many=True)
    categories = CategorySerializer(many=True)
    archive = ArchiveSerializer(many=True)

