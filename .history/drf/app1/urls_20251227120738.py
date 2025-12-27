from django.contrib import admin
from django.urls import path
from.views import sample

app_name="app1"
urlpatterns = [
    path('admin/', admin.site.urls),
]
