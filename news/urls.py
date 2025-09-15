from django.urls import path
from news import views

urlpatterns = [
    path('', views.entering_view, name='entering'),
    path('home/', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('history/', views.history_view, name='history'),
    path('news/', views.news_list_view, name='news'),
    path('news/<int:pk>/', views.news_detail_view, name='news_detail'),
    path('events/', views.events_list_view, name='events'),
    path('events/<int:pk>/', views.event_detail_view, name='event_detail'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('members/', views.members_view, name='members'),
    path('contact/', views.contact_view, name='contact'),
]
