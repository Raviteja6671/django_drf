from django.contrib import admin
from django.urls import path
from .views import sample, Song, Users, getSongsBySinger  # ✅ Now imports correctly

urlpatterns = [
    path('sample/', sample.as_view(), name='sample'),
    path('songs/', Song.as_view(), name='songs'),
    path('users/', Users.as_view(), name='users'),
    path('songs/singer/<str:singer>/', getSongsBySinger, name='songs_by_singer'),  # ✅ Trainer's endpoint
]
