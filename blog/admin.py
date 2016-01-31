from django.contrib import admin
from blog.models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'parent']
    list_display_links = ['id', 'title']
    list_per_page = 25


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_date', 'author', 'preview']
    list_display_links = ['title']
    search_fields = ['title', 'content']
    ordering = ['-created']
    list_per_page = 25


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)