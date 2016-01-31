from django.contrib import admin
from navigation.models import MenuItem, SubMenuItem


class SubMenuItemInline(admin.TabularInline):
    model = SubMenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'link']
    list_display_links = ['id', 'title', 'link']
    list_per_page = 25
    inlines = [SubMenuItemInline]


admin.site.register(MenuItem, MenuItemAdmin)
