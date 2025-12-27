from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import AP

# Create your views here.

def sample(request):
    info={"name":"Raviteja","city":"Nizamabad"}
    return JsonResponse(info)