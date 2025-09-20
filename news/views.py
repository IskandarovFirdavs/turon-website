from django.shortcuts import render, get_object_or_404
from news.models import (
    NewsModel, MembersModel, EventsModel,
    NewsImageModel, NewsVideoModel, EventsImageModel, EventsVideoModel
)


def entering_view(request):
    return render(request, "entering.html")


def home_view(request):
    news = NewsModel.objects.all().order_by('-date')[:5]
    members = MembersModel.objects.all()
    events = EventsModel.objects.all().order_by('-date')[:5]
    images = NewsImageModel.objects.all()[:12]
    videos = NewsVideoModel.objects.all()[:6]

    return render(request, "home.html", {
        "news": news,
        "members": members,
        "events": events,
        "images": images,
        "videos": videos
    })

def about_view(request):
    return render(request, "about.html")


def history_view(request):
    return render(request, "history.html")


def news_list_view(request):
    news_list = NewsModel.objects.order_by('-date')
    return render(request, "news.html", {"news_list": news_list})


def events_list_view(request):
    events = EventsModel.objects.order_by('-date')
    return render(request, "events.html", {"events": events})


def gallery_view(request):
    images = NewsImageModel.objects.all()
    videos = NewsVideoModel.objects.all()
    return render(request, "gallery.html", {
        "images": images,
        "videos": videos,
    })


def members_view(request):
    members = MembersModel.objects.all()
    return render(request, "members.html", {"members": members})


def contact_view(request):
    return render(request, "contact.html")


def news_detail_view(request, pk):
    news = get_object_or_404(NewsModel, pk=pk)
    related_news = NewsModel.objects.exclude(pk=pk).order_by('-date')[:3]
    additional_img = NewsImageModel.objects.filter(news=news)
    additional_video = NewsVideoModel.objects.filter(news=news)
    return render(request, "news-detail.html", {
        "news": news,
        "additional_img": additional_img,
        "additional_video": additional_video,
        "related_news": related_news
    })


def event_detail_view(request, pk):
    event = get_object_or_404(EventsModel, pk=pk)
    related_events = EventsModel.objects.exclude(pk=pk).order_by('-date')[:3]
    additional_img = EventsImageModel.objects.filter(events=event)
    additional_video = EventsVideoModel.objects.filter(events=event)
    return render(request, "event-detail.html", {
        "event": event,
        "related_events": related_events,
        "additional_img": additional_img,
        "additional_video": additional_video,
    })

def custom_page_not_found_view(request, exception):
    return render(request, "404.html", status=404)
