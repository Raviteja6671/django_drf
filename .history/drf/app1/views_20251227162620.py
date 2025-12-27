from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Songs
from .serializers import SongsSerializer,UsersSerializer

# Create your views here.

# def sample(request):
#     info={"name":"Raviteja","city":"Nizamabad"}
#     return JsonResponse(info)

class sample(APIView):
    def get(self,request):
        #info={"name":"Raviteja","city":"Nizamabad"}
        info="Hello World"
        return Response(info)
    def post(self,request):
        pass

class Song(APIView):
    def get(self,request):
        data=Songs.objects.values()
        # print(data)
        serializeddata=SongsSerializer(data,many=True)
        final_data=serializeddata.data
        return Response({"status":"success","data":final_data})

    def post(self,request):
        data=SongsSerializer(data=request.data)  # Serializing is Done 
        if data.is_valid(): # validating
            data.save()  
        print(data.data,"Hello it is a Serializing")   #saving
        return Response({"status":"success","data":data.data})
    class getSongsBySinger(APIView):
        def get(self,request)

class Users(APIView):
    def get(self,request):
        pass

    def post(self,request):
        userSrls=UsersSerializer(data=request.data)  # Serializing is Done 
        if userSrls.is_valid(): # validating
            userSrls.save()  
        print(userSrls.data,"Hello it is a Serializing")   #saving
        return Response({"status":"success","data":userSrls.data})