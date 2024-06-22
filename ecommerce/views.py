from django.shortcuts import render

from ecommerce.models import Order, OrderList

def bascket(request):
    model = Order.objects.get_or_create(id_user=request.user)
    return render(request, "basket.html", {"model": model}) 