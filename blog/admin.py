from django.contrib import admin
from blog.models import Post, Page


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_date', 'title', 'author', 'preview')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'updated')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


admin.site.register(Post, PostAdmin)
admin.site.register(Page, PageAdmin)
