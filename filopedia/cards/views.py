from django.shortcuts import render, get_object_or_404
import json
from cards.data_retriever import get_all_data, get_philosopher, get_card_diario
#from filopedia.cards.data_retriever import get_all_data
from cards.constants import DATA_PATH
from cards.models import Filosofo

def index(request):
    """
    Retorna todos os filósofos em um dicionário chamado Cards
    """
    # arquivos = get_all_data()

    # cards = []

    # for arquivo in arquivos:
    #     with open(f"{DATA_PATH}{arquivo}", "r", encoding="utf-8") as f:
    #        cards.append(json.load(f))

    cards = Filosofo.objects.order_by("nome").filter(publicado=True)

    destaque = get_card_diario()
    
    context = {
            "cards": cards,
            "destaque": destaque
        }

    return render(request, "cards/index.html", context=context)



def card(request, filosofo):
    filosofo = filosofo.replace(" ", "_").lower()
    # card_filosofo = get_philosopher(filosofo)

    card_filosofo = get_object_or_404(Filosofo, slug=filosofo)
    context = {
        "card": card_filosofo
    }

    return render(request, "cards/card.html", context=context)

def sobre(request):
    return render(request, "filopedia/sobre.html")


def pesquisar(request):
    cards = Filosofo.objects.order_by("nome").filter(publicado=True)

    if "pesquisar" in request.GET:
        nome_pesquisa = request.GET['pesquisar']
        if nome_pesquisa:
            cards = cards.filter(nome__icontains=nome_pesquisa)

    context = {
        "cards": cards
    }

    return render(request, "cards/pesquisar.html", context=context)