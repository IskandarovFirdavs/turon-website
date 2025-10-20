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
    main_image = models.ImageField(upload_to="events/imgs/", blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True)



class GalleryImageModel(models.Model):
    image = models.ImageField(upload_to="gallery/imgs/")
    caption = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption if self.caption else "Gallery Image"
    
    
class GalleryVideoModel(models.Model):
    video_url = models.URLField(max_length=255)
    caption = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption if self.caption else "Gallery Video"