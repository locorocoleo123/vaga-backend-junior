from django.urls import path,re_path
from . import views

urlpatterns = [
    path("classificacao/", views.ClubesView.as_view(), name = "clubes"),
    path("partida/", views.JogoView.as_view(), name = "jogos"),
]