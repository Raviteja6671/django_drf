from django.db import models

# Create your models here.
class Songs(models.Model):
    song_name=models.CharField(max_length=100)
    song_duration=models.IntegerField()
    singer=models.CharField(max_length=75)

class Users(models.Mod)