from django.contrib import admin
from blog.models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'parent']
    list_display_links = ['id', 'title']
    list_per_page = 25


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'visible', 'get_date', 'author', 'preview']
    list_display_links = ['title']
    list_filter = ['visible', 'category']
    search_fields = ['title', 'content']
    ordering = ['-created']
    list_per_page = 25
    actions = ['make_visible', 'make_invisible']

    def make_visible(self, request, queryset):
        queryset.update(visible=True)
    make_visible.short_description = 'Make selected Posts visible'

    def make_invisible(self, request, queryset):
        queryset.update(visible=True)
    make_invisible.short_description = 'Make selected Posts invisible'
