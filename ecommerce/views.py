from django.shortcuts import render

from ecommerce.models import Order, OrderList

def bascket(request):
    model = Order.objects.get(id_user=request.user.id)
    return render(request, "bascket.html", {"model": model}) 