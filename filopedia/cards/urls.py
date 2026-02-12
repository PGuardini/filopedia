from django.urls import path
from cards.views import index, card, sobre, pesquisar

urlpatterns = [
    path('', index, name='index'),
    path('card/<str:filosofo>', card, name='card'),
    path('sobre', sobre, name='sobre'),
    path('pesquisar', pesquisar, name='pesquisar')
]