from django.contrib import admin
from django.contrib.admin import TabularInline, ModelAdmin
from django.utils.safestring import mark_safe

from .models import Giftme, GiftmeImage, Category, Friendship


class ImageAdminInline(TabularInline):
    extra = 1
    model = GiftmeImage


@admin.register(Giftme)
class GiftmeAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'content', 'image', 'id', 'image_show']
    list_editable = ['price' ]
    list_display_links = ['id', 'title', 'image_show', 'content']
    search_fields = ['id', 'title']
    ordering = ['-title', '-price']
    list_filter = ['is_published', 'time_create']
    list_per_page = 10
    inlines = (ImageAdminInline,)

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"
    image_show.__name__ = "Картинка"


admin.site.register(Category)
admin.site.register(Friendship)
