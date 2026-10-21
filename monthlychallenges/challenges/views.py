from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def january(request):
    return HttpResponse("Eat no meat for this entire month!")
def february(request):
    return HttpResponse("Works for at least 20 minutes every day")
