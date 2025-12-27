from django.contrib import admin
from django.urls import path
from .views import sample, Song, Users, getSongsBySinger

urlpatterns = [
    path('sample/', sample.as_view(), name='sample'),
    path('songs/', Song.as_view(), name='songs'),
    path('users/', Users.as_view(), name='users'),
    path('songsBysinger/<str:singer>/', getSongsBySinger.as_view(), name='songs_by_singer'),
]
