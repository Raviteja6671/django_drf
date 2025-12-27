from django.contrib import admin
from django.urls import path
from.views import sample,Song,Users,getSongsBySinger

app_name="app1"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample/', sample.as_view()),
    path('song/',Song.as_view()),
    path('user/',Users.as_view()),
    path('songBysinger/',getSongBySinger.as_view())
]
