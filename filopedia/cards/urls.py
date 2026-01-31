from django.urls import path
from cards.views import index, card, sobre

urlpatterns = [
    path('', index, name='index'),
    path('card/<str:filosofo>', card, name='card'),
    path('sobre', sobre, name='sobre'),
]