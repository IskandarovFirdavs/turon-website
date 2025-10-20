from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from itertools import chain
from operator import attrgetter
from news.models import (
    NewsModel, MembersModel, EventsModel,
    GalleryImageModel, GalleryVideoModel
)


def entering_view(request):
    return render(request, "entering.html")


def home_view(request):
    videos = GalleryVideoModel.objects.order_by('-created_at')[:3]
    for video in videos:
        if "youtube.com/watch?v=" in video.video_url:
            video.embed_url = video.video_url.replace("watch?v=", "embed/")
        elif "youtu.be/" in video.video_url:
            video.embed_url = video.video_url.replace("youtu.be/", "www.youtube.com/embed/")
        else:
            video.embed_url = video.video_url

    context = {
        "news": NewsModel.objects.order_by('-date')[:3],
        "events": EventsModel.objects.order_by('-start_time')[:3],  # fixed
        "members": MembersModel.objects.all(),
        "images": GalleryImageModel.objects.order_by('-created_at')[:3],
        "videos": videos,
    }
    return render(request, "home.html", context)


def about_view(request):
    return render(request, "about.html")


def history_view(request):
    return render(request, "history.html")


def news_list_view(request):
    news_list = NewsModel.objects.order_by('-date')
    paginator = Paginator(news_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    first_news = page_obj[0] if page_obj else None
    other_news = page_obj[1:] if len(page_obj) > 1 else []

    return render(request, "news.html", {
        "first_news": first_news,
        "other_news": other_news,
        "page_obj": page_obj,
    })


def events_list_view(request):
    events_list = EventsModel.objects.order_by('-start_time')  # fixed
    paginator = Paginator(events_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "events.html", {"page_obj": page_obj})


from django.core.paginator import Paginator
from django.shortcuts import render
from .models import GalleryImageModel, GalleryVideoModel

def gallery_view(request):
    image_list = GalleryImageModel.objects.order_by('-created_at')
    video_list = GalleryVideoModel.objects.order_by('-created_at')

    image_paginator = Paginator(image_list, 1)  # 6 tadan sahifada
    video_paginator = Paginator(video_list, 1)  # 3 tadan sahifada

    image_page_number = request.GET.get('page')
    video_page_number = request.GET.get('vpage')

    images = image_paginator.get_page(image_page_number)
    videos = video_paginator.get_page(video_page_number)

    for video in videos:
        if "youtube.com/watch?v=" in video.video_url:
            video.embed_url = video.video_url.replace("watch?v=", "embed/")
        elif "youtu.be/" in video.video_url:
            video.embed_url = video.video_url.replace("youtu.be/", "www.youtube.com/embed/")
        else:
            video.embed_url = video.video_url

    return render(request, "gallery.html", {
        "images": images,
        "videos": videos,
    })



def members_view(request):
    members = MembersModel.objects.all()
    paginator = Paginator(members, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "members": members,
        "page_obj": page_obj,
    }
    return render(request, "members.html", context)


def contact_view(request):
    return render(request, "contact.html")


def news_detail_view(request, pk):
    news = get_object_or_404(NewsModel, pk=pk)
    related_news = NewsModel.objects.exclude(pk=pk).order_by('-date')[:3]
    return render(request, "news-detail.html", {
        "news": news,
        "related_news": related_news
    })


def event_detail_view(request, pk):
    event = EventsModel.objects.get(pk=pk)
    related_events = EventsModel.objects.exclude(pk=pk)[:3]
    all_events = EventsModel.objects.all()  # kalendar uchun
    return render(request, "event-detail.html", {
        "event": event,
        "related_events": related_events,
        "all_events": all_events,
    })


def custom_page_not_found_view(request, exception):
    return render(request, "404.html", status=404)

