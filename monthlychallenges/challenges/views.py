from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.

monthly_challenges = {
    "january": "Eat no candy for the entire month",
    "february": "Work out for at least 20 minutes a day",
    "march": "Learn Django for at least 20 minutes a day",
    "april": "Do not drink alcohol for the month",
    "may": "Do not smoke for the entire month",
    "june": "Read at least 10 pages of a book every day",
    "july": "Drink at least 2 liters of water a day",
    "august": "Wake up before 7 AM every day",
    "september": "Spend at least 30 minutes learning something new every day",
    "october": "Avoid fast food for the entire month",
    "november": "Write in a journal for at least 10 minutes a day",
    "december": "Spend no more than 30 minutes a day on social media"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # "<li><a href='...'>January</a></li><li><a href='...'>February</a></li>..."

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {"text": challenge_text, "month_name": month})
    except:
        return HttpResponseNotFound("Month not found")
