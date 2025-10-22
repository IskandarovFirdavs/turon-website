from django.db import models
from parler.models import TranslatableModel, TranslatedFields

class NewsModel(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        text=models.TextField()
    )
    date = models.DateTimeField(auto_now_add=True)
    main_image = models.ImageField(upload_to="news/imgs/")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True)

    class Meta:
        ordering = ['-date']



class MembersModel(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255),
    )
    image = models.FileField(max_length=255)
    website_url = models.URLField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.safe_translation_getter("name", any_language=True)
    
    class Meta:
        ordering = ['-date']


class EventsModel(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        description=models.TextField()
    )
    location = models.CharField(max_length=255)
    main_image = models.ImageField(upload_to="events/imgs/")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True)


class GalleryImageModel(TranslatableModel):
    image = models.ImageField(upload_to="gallery/imgs/")
    translations = TranslatedFields(
        caption=models.CharField(max_length=255)
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"
        ordering = ["-created_at"]

    def __str__(self):
        return self.safe_translation_getter("caption", any_language=True) or "Untitled Image"


class GalleryVideoModel(TranslatableModel):
    video_url = models.URLField(max_length=255)
    translations = TranslatedFields(
        caption=models.CharField(max_length=255)
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Gallery Video"
        verbose_name_plural = "Gallery Videos"
        ordering = ["-created_at"]

    def __str__(self):
        return self.safe_translation_getter("caption", any_language=True) or "Untitled Video"