from django.contrib import admin
from django.urls import path
from .views import sample, Song, Users, getSongsBySinger  # ✅ Correct import

urlpatterns = [
    path('sample/', sample.as_view(), name='sample'),
    path('songs/', Song.as_view(), name='songs'),
    path('users/', Users.as_view(), name='users'),
    path('songs/singer/<str:singer>/', getSongsBySinger, name='songs_by_singer'),  # ✅ NO .as_view()
]
