from django.contrib import admin
from .models import Source, News
from django.utils.html import format_html
# Register your models here.

class SourceAdmin(admin.ModelAdmin):
    list_display_links = ['photo_thumbnail', 'name',]
    list_display = ['photo_thumbnail','name', 'language', 'link', 'rss_url']
    order_by = ['name']

    def photo_thumbnail(self, obj):
        if obj.icon:
            return format_html('<img src="{}" style="width:50px; height:50px; border-radius:10px; object-fit: cover;" />'.format(obj.icon.url))
        return 'No image'

    photo_thumbnail.short_description = 'Icon'


class NewsAdmin(admin.ModelAdmin):
    list_display_links = ['photo_thumbnail', 'source',]
    list_display = ['photo_thumbnail','source', 'guid', 'title', 'url', 'view']
    order_by = ['title']

    def photo_thumbnail(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="width:50px; height:50px; border-radius:10px; object-fit: cover;" />'.format(obj.photo.url))
        return 'No image'

    photo_thumbnail.short_description = 'photo'

admin.site.register(Source, SourceAdmin)
admin.site.register(News ,NewsAdmin)
