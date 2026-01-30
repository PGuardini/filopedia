from django.shortcuts import render
import json
from cards.data_retriever import get_all_data, get_philosopher
#from filopedia.cards.data_retriever import get_all_data
from cards.constants import DATA_PATH

def index(request):
    """
    Retorna todos os filósofos em um dicionário chamado Cards
    """
    arquivos = get_all_data()

    cards = []

    for arquivo in arquivos:
        with open(f"{DATA_PATH}{arquivo}", "r", encoding="utf-8") as f:
           cards.append(json.load(f))

    context = {
            "cards": cards
        }

    return render(request, "index.html", context=context)



def card(request, filosofo):
    filosofo = filosofo.replace(" ", "_").lower()
    card_filosofo = get_philosopher(filosofo)

    return render(request, "card.html", card_filosofo)