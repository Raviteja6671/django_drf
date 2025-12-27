from rest_framework import serializers
from .models import Songs,Users

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Songs
        fids="__all__"

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fileds="__all__"