from django.urls import path
from . import views

app_name = "ecommerce"

urlpatterns = [
    path('', views.bascket, name='bascet'),
    # path('add/', views.logout_user, name='add'),
    # path('delete/', views.register, name='delete'),
    # path('pay/', views.register, name='pay'),
]