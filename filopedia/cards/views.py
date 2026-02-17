from django.shortcuts import render, get_object_or_404
from cards.data_retriever import get_all_data, get_philosopher, get_card_diario
#from filopedia.cards.data_retriever import get_all_data
from cards.constants import DATA_PATH
from cards.models import Filosofo, Exibicao
from datetime import date

def index(request):
    """
    Retorna todos os filósofos e filósofos em destaque
    """
    
    cards = Filosofo.objects.order_by("nome").filter(publicado=True)

    exibido_hoje = Exibicao.objects.filter(data_exibicao=date.today()).first()

    if not exibido_hoje:
        filosofo_destaque = Filosofo.objects.filter(exibicao__isnull=True).order_by('?').first()
        registro = Exibicao(id_filosofo=filosofo_destaque)
        registro.save()

    destaques = Exibicao.objects.select_related('id_filosofo').order_by('data_exibicao')

    context = {
            "cards": cards,
            "destaques": destaques
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