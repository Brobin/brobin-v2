from django.contrib import admin
from blog.models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'parent']
    list_display_links = ['id', 'title']
    list_per_page = 25


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_date', 'title', 'author', 'preview']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'content']
    list_per_page = 25


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)