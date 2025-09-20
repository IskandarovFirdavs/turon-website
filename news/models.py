from django.db import models
from parler.models import TranslatableModel, TranslatedFields

class NewsModel(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        text=models.TextField()
    )
    date = models.DateTimeField(auto_now_add=True)
    main_image = models.ImageField(upload_to="news/imgs/")
    main_video = models.FileField(upload_to="news/videos/")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True)


class NewsImageModel(models.Model):
    news = models.ForeignKey(NewsModel, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="news/imgs/")

    def __str__(self):
        return f"Image for {self.news}"


class NewsVideoModel(models.Model):
    news = models.ForeignKey(NewsModel, on_delete=models.CASCADE, related_name="videos")
    video = models.FileField(upload_to="news/videos/")

    def __str__(self):
        return f"Video for {self.news}"


class MembersModel(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255),
    )
    image = models.ImageField(upload_to="news/members/")
    website_url = models.URLField(max_length=255)

    def __str__(self):
        return self.safe_translation_getter("name", any_language=True)


class EventsModel(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        description=models.TextField()
    )
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    main_image = models.ImageField(upload_to="events/imgs/", blank=True, null=True)
    main_video = models.FileField(upload_to="events/videos/", blank=True, null=True)

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True)



class EventsImageModel(models.Model):
    events = models.ForeignKey(EventsModel, on_delete=models.CASCADE, related_name="event_images")
    image = models.ImageField(upload_to="news/imgs/")

    def __str__(self):
        return f"Image for {self.events}"


class EventsVideoModel(models.Model):
    events = models.ForeignKey(EventsModel, on_delete=models.CASCADE, related_name="event_ideos")
    video = models.FileField(upload_to="news/videos/")

    def __str__(self):
        return f"Video for {self.events}"