from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets

from cards.constants import DATA_PATH

from cards.models import Filosofo, Exibicao
from cards.serializers import FilosofoSerializer, ExibicaoSerializer


from datetime import date

class FilosofoView(viewsets.ModelViewSet):
    serializer_class = FilosofoSerializer
    queryset = Filosofo.objects.order_by("nome").filter(publicado=True)


class ExibicaoView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ExibicaoSerializer

    exibido_hoje = Exibicao.objects.filter(data_exibicao=date.today()).first()
        
    if not exibido_hoje:
        novo_filosofo_em_destaque = Filosofo.objects.filter(exibicao__isnull=True).order_by('?').first()
        nova_exibicao = Exibicao(id_filosofo=novo_filosofo_em_destaque)
        nova_exibicao.save()

    # Todos filósofos que já foram/estão sendo exibidos ordenados pela mais recente exibicao
    queryset = Exibicao.objects.select_related('id_filosofo').order_by('data_exibicao')




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

# Não vai mais precisar

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