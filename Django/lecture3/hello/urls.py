from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("titobi", views.titobi, name="titobi"),
    path("leticia", views.leticia, name="leticia")
]