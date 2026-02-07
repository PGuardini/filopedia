from cards.constants import DATA_PATH
from pathlib import Path
import json
import datetime
import random


def get_all_data():
    data_directory = Path(DATA_PATH)
    arquivos = [arquivo.name for arquivo in data_directory.iterdir() if "404" not in arquivo.name and "cards" not in arquivo.name]

    return arquivos

def get_philosopher(name: str) -> dict:
    data_directory = Path(DATA_PATH)
    caminho_arquivo = None
    for arquivo in data_directory.iterdir():
        if name.lower() in arquivo.name.lower() and "404" not in arquivo.name.lower():
            caminho_arquivo = arquivo.name

            break

    if caminho_arquivo is None:
        return {"erro": "Filósofo não encontrado"}
    
    with open(f"{DATA_PATH}{caminho_arquivo}", "r", encoding="utf-8") as f:
        filosofo = json.load(f)

    return filosofo


def get_card_diario():
    """
        Retorna um filósofo aleatório por dia. 
        Caso já exista algum vinculado à data atual, retorna ele para não
        ficar alternando a cada atualização.
    """
    
    diretorio = Path(DATA_PATH)

    with open(f"{diretorio}/cards.json", 'r', encoding='utf-8') as f:
        cards = json.load(f)

    data_atual = str(datetime.date.today())

    nao_exibidos = [card['nome'] for card in cards if card['exibido'] is None]

    filosofo = None
    for card in cards:
        if card['exibido'] == data_atual:
            return get_philosopher(card['nome'])

    if filosofo is None:
        num_aleatorio = random.randint(0, len(nao_exibidos))
        filosofo = nao_exibidos[num_aleatorio]

        for card in cards:
            if card['nome'] == filosofo:
                card['exibido'] = data_atual
                break

    with open(f'{DATA_PATH}/cards.json', 'w+', encoding='utf-8') as f:
        dados_convertidos = json.dumps(cards, ensure_ascii=False, indent=4)
        f.write(dados_convertidos)

    return get_philosopher(filosofo)