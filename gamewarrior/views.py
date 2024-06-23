from django.shortcuts import render
from .models import Game, Janr, TagsOfGame

def primerigr(request):
    query = request.GET.get('q')
    if query:
        games = Game.objects.filter(name__icontains=query)
    else:
        games = Game.objects.all()
    janr = Janr.objects.all()
    return render(request, "primerigr.html", {"games": games, "janr": janr})

# Остальные функции остаются без изменений
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

def registration(request):
    return render(request, "registration.html")

def blog(request):
    return render(request, "blog.html")

def index(request):
    ctx = {}
    return render(request, "index.html", ctx)
