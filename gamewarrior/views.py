from django.http import HttpResponse
from django.shortcuts import render
from .models import Game




def card(request, id):
    game = Game.objects.get(pk=id)
    
    return render(request, "card.html", {"model": game}) 

def basket(request):
    data = Game.objects.all()
    return render(request, "basket.html")

def contact(request):
    return render(request, "contact.html")

def community(request):
    return render(request, "community.html")

def review(request):
    return render(request, "review.html")

def login(request):
    return render(request, "login.html")

def review(request):
    return render(request, "review.html")

def registration(request):
    return render(request, "registration.html")

def blog(request):
    return render(request, "blog.html")

def index(request):
    ctx = {}
    return render(request, "index.html", ctx)
    # return HttpResponse(id)