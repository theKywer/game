from django.db import models
from django.contrib.auth.models import User

from gamewarrior.models import Game

class Order(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.PROTECT)
    price = models.IntegerField(null=True)
    status = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(null=True)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id_user.id
        super().save(*args, **kwargs)

class OrderList(models.Model):
    id_order = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE)
    id_game = models.ForeignKey(Game, related_name='game', on_delete=models.PROTECT)
    price = models.IntegerField(null=True)