from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def january(request):
    return HttpResponse("Eat no meat for this entire month!")
def february(request):
    return HttpResponse("Works for at least 20 minutes every day")

def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no meat for the entire month!"
    elif month == "february":
        challenge_text = "Work for at least 20 minutes every day!"
    elif month == "march":
        challenge_text = "Learn Django for at least 20 minutes every day"
    else:
        return HttpResponseNotFound("The month is not supported")
    return HttpResponse(challenge_text)
