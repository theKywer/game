from django.db import models
from django.contrib.auth.models import User

from gamewarrior.models import Game

class Order(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.PROTECT)
    price = models.IntegerField()
    status = models.BooleanField()
    created_at = models.DateField()
    updated_at = models.DateField()

class OrderList(models.Model):
    id_order = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE)
    id_game = models.ForeignKey(Game, related_name='game', on_delete=models.PROTECT)
    price = models.IntegerField()