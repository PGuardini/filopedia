from cards.constants import DATA_PATH
from pathlib import Path
import json

def get_all_data():
    data_directory = Path(DATA_PATH)
    arquivos = [arquivo.name for arquivo in data_directory.iterdir() if "404" not in arquivo.name]

    return arquivos

def get_philosopher(name):
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