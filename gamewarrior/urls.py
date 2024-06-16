from django.urls import path
from . import views

app_name = "gamewarrior"

urlpatterns = [
    path("", views.index, name = "index"),
    path("card/<int:id>", views.card, name="card"),
    path("main", views.index, name="main"),
    path("blog", views.blog, name="blog"), 
    path("basket", views.basket, name="basket"),
    path("contact", views.contact, name="contact"),
    path("community", views.community, name="community"),
    path("review", views.review, name="review"),
    path("registration", views.registration, name="registration"),
    # path("/login", views.login, name="login"),
    
]