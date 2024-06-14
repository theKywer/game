from django.db import models

# Create your models here.

class User(models.Model):
    login = models.TextField()
    nickname = models.TextField()
    password = models.TextField()
    email = models.EmailField()
    datareg = models.DateField()

class Janr(models.Model):
    name = models.TextField()
    description = models.TextField()


class Game(models.Model):
    name = models.TextField()
    year = models.IntegerField()
    janr_id = models.ForeignKey(Janr, on_delete=models.PROTECT)
    description = models.TextField()
    imagemain = models.ImageField(upload_to='img/', null=True, max_length=255)
    imagecar1 = models.ImageField(upload_to='img/', null=True, max_length=255)
    imagecar2 = models.ImageField(upload_to='img/', null=True, max_length=255)
    imagecar3 = models.ImageField(upload_to='img/', null=True, max_length=255)
    imagecar4 = models.ImageField(upload_to='img/', null=True, max_length=255)
    imagecar5 = models.ImageField(upload_to='img/', null=True, max_length=255)
    developer = models.TextField(default="default title")
    publisher = models.TextField(default="default title")
    price = models.IntegerField()


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