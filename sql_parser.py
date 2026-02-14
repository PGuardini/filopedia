from pathlib import Path
import json

def get_all_data():
    data_directory = Path('data/')
    arquivos = [arquivo.name for arquivo in data_directory.iterdir() if "404" not in arquivo.name and "cards" not in arquivo.name]

    return arquivos

def parser():
    arquivos = get_all_data()
    
    sql_insert = "INSERT INTO cards_filosofo (nome, biografia, imagem, referencias, slug, publicado) VALUES "

    tamanho = len(arquivos)
    i = 0

    for caminho_arquivo in arquivos:
        i+=1
        with open(f"data/{caminho_arquivo}", "r", encoding="utf-8") as f:
            filosofo = json.load(f)

            nome = filosofo['titulo'][0]
            biografia = ''.join(filosofo['conteudo'])
            imagem = filosofo['imagem']
            referencias = filosofo['url']
            slug = filosofo['view']
            publicado = 'TRUE'

            biografia = biografia.replace("'", "''")

            if i != tamanho:
                values = f"('{nome}', '{biografia}', '{imagem}', '{referencias}', '{slug}', {publicado}),"
            else:
                values = f"('{nome}', '{biografia}', '{imagem}', '{referencias}', '{slug}', {publicado})"
            
            sql_insert += values

    with open("insert.sql", 'w', encoding='utf-8') as f:
        f.write(sql_insert)

parser()