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
        data=SongsSerializer(data=request.data)  # Serializing is Done 
        if data.is_valid(): # validating
            data.save()  
        print(data.data,"Hello Its Is a ")   #saving
        return Response("success")