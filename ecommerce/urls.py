from django.urls import path
from . import views

app_name = "ecommerce"

urlpatterns = [
    path('', views.basket, name='basket'),
    path('add/<int:game_id>/', views.add_to_basket, name='add_to_basket'),
    path('remove/<int:item_id>/', views.remove_from_basket, name='remove_from_basket'),
    path('checkout/', views.checkout, name='checkout'),
]
