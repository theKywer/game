# from integer import Integer
from django.conf import settings
from gamewarrior.models import *


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
             cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        game_id = self.cart.keys()
        games = Game.objects.filter(id__in=game_id)

        cart = self.cart.copy()
        for game in games:
            cart [str(game_id)]['game'] = game

        for item in cart.values():
            # item['price'] = Integer(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, game, quantity=1, update_quantity=False):   
        game_id = str(game.id)
        if game_id not in self.cart:
            self.cart[game_id] = {'quantity': 0,
                                  'price': str(game.price)}
        if update_quantity:
            self.cart[game_id]['quantity'] = quantity
        else:
            self.cart[game_id]['quantity'] +=quantity
        self.save()   

    def save(self):
        self.session.modified = True

    def remove(self, game):
        game_id = str(game.id)
        if game_id in self.cart:
            del self.cart[game_id]
            self.save()        

    def get_total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.cart.values())       

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()