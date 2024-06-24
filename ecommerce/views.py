from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ecommerce.models import Order, OrderList
from gamewarrior.models import Game

@login_required
def basket(request):
    order, created = Order.objects.get_or_create(id_user=request.user, status=False)
    order_items = OrderList.objects.filter(id_order=order)
    total_price = sum(item.price for item in order_items)

    return render(request, "basket.html", {"order": order, "order_items": order_items, "total_price": total_price})

@login_required
def add_to_basket(request, game_id):
    game = Game.objects.get(id=game_id)
    order, created = Order.objects.get_or_create(id_user=request.user, status=False)
    OrderList.objects.create(id_order=order, id_game=game, price=game.price)
    return redirect('ecommerce:basket')

@login_required
def remove_from_basket(request, item_id):
    item = OrderList.objects.get(id=item_id)
    item.delete()
    return redirect('ecommerce:basket')

@login_required
def checkout(request):
    order = Order.objects.get(id_user=request.user, status=False)
    order_items = OrderList.objects.filter(id_order=order)
    total_price = sum(item.price for item in order_items)
    order.status = True
    order.save()
    return render(request, "checkout.html", {"order": order, "order_items": order_items, "total_price": total_price})
