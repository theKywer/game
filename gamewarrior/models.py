from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Janr(models.Model):
    name = models.TextField()
    description = models.TextField()


class Game(models.Model):
    name = models.TextField()
    year = models.IntegerField()
    janr_id = models.ForeignKey(Janr, on_delete=models.PROTECT)
    description = models.TextField()
    imagemain = models.TextField(default="default title")
    imagecar1 = models.TextField(default="default title")
    imagecar2 = models.TextField(default="default title")
    imagecar3 = models.TextField(default="default title")
    imagecar4 = models.TextField(default="default title")
    imagecar5 = models.TextField(default="default title")
    developer = models.TextField(default="default title")
    publisher = models.TextField(default="default title")
    price = models.IntegerField()

def __str__(self):
    return self.name

class Order(models.Model):
    id_order = models.ForeignKey(Janr, on_delete=models.PROTECT)
    id_user = models.ForeignKey(User, on_delete=models.PROTECT)
    id_game = models.ForeignKey(Game, on_delete=models.PROTECT)
    status_pay = models.BooleanField()
    price = models.IntegerField()
    update_time = models.DateTimeField()

class OrderList(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    game_id = models.ForeignKey(Game, on_delete=models.PROTECT)
    price = models.IntegerField()


