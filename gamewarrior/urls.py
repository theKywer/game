from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name = "index"),
    path("card/<int:id>", views.card, name="card")
]