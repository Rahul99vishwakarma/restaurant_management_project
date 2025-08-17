from django.shortcuts import render
from django.conf import settings

def home_view(request):
    context = {
        "restaurant_name": settings.RESTAURANT_NAME
    }
    return render(request, "index.html", context)
