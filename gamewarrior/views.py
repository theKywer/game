from django.http import HttpResponse
from django.shortcuts import render
from .models import Game




def card(request, id):
    game = Game.objects.get(pk=id)
    return render(request, "card.html", {"model": game})

def index(request):
    ctx = {}
    return render(request, "index.html", ctx)
    # return HttpResponse(id)