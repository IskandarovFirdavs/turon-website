from django.contrib import admin
from django.utils.html import format_html
from parler.admin import TranslatableAdmin
from .models import NewsModel, NewsImageModel, NewsVideoModel, MembersModel


# --- Inlines ---
class NewsImageInline(admin.TabularInline):
    model = NewsImageModel
    extra = 1
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100"/>', obj.image.url)
        return "-"
    preview.short_description = "Preview"


class NewsVideoInline(admin.TabularInline):
    model = NewsVideoModel
    extra = 1
    readonly_fields = ("video_link",)

    def video_link(self, obj):
        if obj.video:
            return format_html('<a href="{}" target="_blank">Watch</a>', obj.video.url)
        return "-"
    video_link.short_description = "Video"


# --- News ---
@admin.register(NewsModel)
class NewsAdmin(TranslatableAdmin):
    list_display = ("title", "date", "has_images", "has_videos")
    list_display_links = ("title",)
    search_fields = ("translations__title",)
    list_filter = ("date",)
    date_hierarchy = "date"
    ordering = ("-date",)
    readonly_fields = ("date",)
    inlines = [NewsImageInline, NewsVideoInline]

    fieldsets = (
        ("Asosiy ma'lumotlar", {
            "fields": ("title", "text", "date"),
        }),
        ("Media fayllar", {
            "fields": ("main_image", "main_video"),
            "classes": ("collapse",),  # Collapsible bo‘lim
        }),
    )

    def has_images(self, obj):
        return obj.images.exists()
    has_images.boolean = True
    has_images.short_description = "Images?"

    def has_videos(self, obj):
        return obj.videos.exists()
    has_videos.boolean = True
    has_videos.short_description = "Videos?"


# --- Members ---
@admin.register(MembersModel)
class MembersAdmin(TranslatableAdmin):
    list_display = ("name", "website_url", "preview")
    list_display_links = ("name",)
    search_fields = ("translations__name",)
    list_filter = ("website_url",)

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80"/>', obj.image.url)
        return "-"
    preview.short_description = "Preview"


# --- NewsImage ---
@admin.register(NewsImageModel)
class NewsImageAdmin(admin.ModelAdmin):
    list_display = ("news", "preview")
    search_fields = ("news__translations__title",)

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100"/>', obj.image.url)
        return "-"
    preview.short_description = "Preview"


# --- NewsVideo ---
@admin.register(NewsVideoModel)
class NewsVideoAdmin(admin.ModelAdmin):
    list_display = ("news", "video_link")
    search_fields = ("news__translations__title",)

    def video_link(self, obj):
        if obj.video:
            return format_html('<a href="{}" target="_blank">Watch</a>', obj.video.url)
        return "-"
    video_link.short_description = "Video"
