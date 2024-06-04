from django.http import HttpResponse


def index(request):
    # model = game.getinfo()
    
    return HttpResponse("Главная страница.")

