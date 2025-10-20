from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import NewsModel, MembersModel, EventsModel, GalleryImageModel, GalleryVideoModel


@admin.register(NewsModel)
class NewsAdmin(TranslatableAdmin):
    list_display = ('title', 'date')
    search_fields = ('translations__title',)
    readonly_fields = ('date',)
    fieldsets = (
        (None, {
            'fields': ('main_image',)
        }),
        ('Translations', {
            'fields': ('title', 'text')
        }),
    )

    def title(self, obj):
        return obj.safe_translation_getter('title', any_language=True)


@admin.register(MembersModel)
class MembersAdmin(TranslatableAdmin):
    list_display = ('name', 'website_url')
    search_fields = ('translations__name',)
    fieldsets = (
        ('Basic Info', {
            'fields': ('image', 'website_url')
        }),
        ('Translations', {
            'fields': ('name',)
        }),
    )

    def name(self, obj):
        return obj.safe_translation_getter('name', any_language=True)

@admin.register(EventsModel)
class EventsAdmin(TranslatableAdmin):
    list_display = ('title', 'location')
    search_fields = ('translations__title', 'location')


@admin.register(GalleryImageModel)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'created_at')
    search_fields = ('caption',)
    readonly_fields = ('created_at',)


@admin.register(GalleryVideoModel)
class GalleryVideoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'video_url', 'created_at')
    search_fields = ('caption',)
    readonly_fields = ('created_at',)
