from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Songs
from .serializers import SongsSerializer

# Create your views here.

# def sample(request):
#     info={"name":"Raviteja","city":"Nizamabad"}
#     return JsonResponse(info)

class sample(APIView):
    def get(self,request):
        info={"name":"Raviteja","city":"Nizamabad"}
        #info="Hello World"
        return Response(info)
    def post(self,request):
        pass

class Song(APIView):
    def get(self,request):
        pass

    def post(self,request):
        print(request.body,"Before Serializing")
        data=SongsSerializer(data=request.data)  # Serializing is Done 
        print(data,"After Serializing")
        if data.is_valid(): # validating
            data.save()      
        return Response("success")