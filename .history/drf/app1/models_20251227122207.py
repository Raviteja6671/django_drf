from django.db import models

# Create your models here.
class Songs(models.model):
    song_name=models.CharField(max_length=100)
    song_duration=