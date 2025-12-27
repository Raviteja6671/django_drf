from django.contrib import admin
from django.urls import path
from.views import sample

app_name
urlpatterns = [
    path('admin/', admin.site.urls),
]
