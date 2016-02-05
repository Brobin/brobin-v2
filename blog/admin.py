from django.contrib import admin
from blog.models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'parent']
    list_display_links = ['id', 'title']
    list_per_page = 25


def make_visible(modeladmin, request, queryset):
    queryset.update(visible=True)


def make_invisible(modeladmin, request, queryset):
    queryset.update(visible=False)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'visible', 'get_date', 'author', 'preview']
    list_display_links = ['title']
    list_filter = ['visible']
    search_fields = ['title', 'content']
    ordering = ['-created']
    list_per_page = 25
    actions = [make_visible, make_invisible]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
