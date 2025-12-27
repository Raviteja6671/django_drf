from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

# def sample(request):
#     info={"name":"Raviteja","city":"Nizamabad"}
#     return JsonResponse(info)

class sample(APIView):
    def get(request):
        pass
    def