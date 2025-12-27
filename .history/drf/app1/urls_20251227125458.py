from django.contrib import admin
from django.urls import path
from.views import sample,S

app_name="app1"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample/', sample.as_view()),
]
