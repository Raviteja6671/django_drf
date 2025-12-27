from django.contrib import admin
from django.urls import path
from.views import sample

urlpatterns = [
    path('admin/', admin.site.urls),
]
