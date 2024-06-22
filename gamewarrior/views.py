from django.http import HttpResponse
from django.shortcuts import render
from .models import Game, Janr, TagsOfGame




def card(request, slug):
    game = Game.objects.get(slug=slug)
    tags = TagsOfGame.objects.filter(id_game=game.id)
    return render(request, "card.html", {
        "model": game,
        "tags": tags,
    }) 

def basket(request):
    data = Game.objects.all()
    return render(request, "basket.html")

def contact(request):
    return render(request, "contact.html")

def community(request):
    return render(request, "community.html")

def primerigr(request):
    game = Game.objects.all()
    janr = Janr.objects.all()
    return render(request, "primerigr.html", {"games": game, "janr": janr})

# def login(request):
    # return render(request, "login.html")

def registration(request):
    return render(request, "registration.html")

def blog(request):
    return render(request, "blog.html")

def index(request):
    ctx = {}
    return render(request, "index.html", ctx)
    # return HttpResponse(id)

    