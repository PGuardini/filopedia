from scrapy.exceptions import DropItem
import re
import json
from datetime import datetime
import w3lib.html

class MapeadoraPipeline:
    def open_spider(self, spider):
        """
            Quando a aranha começa o processo de scraping,
            ela abre o arquivo json onde serão colocadas as urls dos
            itens raspados e gera uma lista com os dados do json.

            Caso não carregue o json, vai gerar uma lista vazia
        """
        try:
            self.arquivo = open("urls.json", "w+", encoding="utf-8")
            self.lista_urls = json.load(self.arquivo)
        except:
            self.lista_urls = []

    def process_item(self, item, spider):
        """
            Depois que a aranha começa o scraping,
            os itens são tratados para manter somente os nomes de
            filósofos e títulos parecidos com nomes.
            Remove qualquer título que contenha ':' ou 'commentators'

            Cada item vira uma url e é adicionado à propriedade
            'self.lista_urls'.
        """

        titulo = item['titulo']

        nomes_romanizados = re.match(r"((^[A-Z][a-z]+, )(\w+[ .]?)+)", titulo)
        nomes_arabes_al = re.match(r"(^al-\w+)", titulo)
        nomes_arabes_ibn = re.match(r"(^Ibn \w+(\[\w+\])?)", titulo)
        nomes_sem_separacao = re.match(r"((^[A-Z][a-z]+ )(\w+ ?)+)", titulo)

        if nomes_romanizados or nomes_arabes_al or nomes_arabes_ibn or nomes_sem_separacao:
            if "," in titulo:
                nome_filosofo_dividido = titulo.split(", ")
                nome_filosofo = f"{nome_filosofo_dividido[-1]}_{nome_filosofo_dividido[0]}" 
            
            nome_filosofo = nome_filosofo.replace(" ", "_")

            excecoes_nomes = (":", "commentators")

            if any(excecao in nome_filosofo for excecao in excecoes_nomes):
                nome_filosofo = None
                raise DropItem("O título não é um nome de filósofo")
        else:
            raise DropItem("O título não é um nome de filósofo")
        
        dado_formatado = {
                nome_filosofo: f"https://pt.wikipedia.org/wiki/{nome_filosofo}"
            }

        if isinstance(self.lista_urls, list):
            self.lista_urls.append(dado_formatado)
            
        return nome_filosofo
        
    
    def close_spider(self, spider):
        """
            Após ter feito o tratamento completo dos itens extraídos,
            a aranha escreve todos os dados em formato json no arquivo
            e fecha o arquivo.

            Esse processo reduz a quantidade de vezes que o arquivo é
            modificado, tornando mais eficiente o código, pois evita
            um processo redundante.
        """

        json.dump(self.lista_urls, self.arquivo, indent=4, ensure_ascii=False)

        self.arquivo.close()

class WikipediaPipeline:
    """
        A aranha wikipedia retém alguns itens no seu processo de
        raspagem: url, codigo_http, título, conteúdo, ligações
        externas, categorias e imagem da página que ela raspou.

        É feita a limpeza das tags HTML do conteúdo, para retermos
        somente o texto do artigo, possibilitando a formatação para
        o portal. Retemos também os links das categorias para traba-
        lharmos futuramente com eles.

        Após a limpeza, os dados são salvos em arquivos .json com
        seus correspondentes nomes. Caso a página gere o erro 404,
        o arquivo recebe o nome 404_[nome_da_página], para facilitar
        o mapeamento de quais links não possuem tradução para o por-
        tuguês ou que não existem.

        Os dados são salvos em arquivos .json para facilitar a sua
        futura consulta através do backend em Django.
    """

    def process_item(self, item, spider):
        
        conteudo_limpo = [w3lib.html.remove_tags(str(textos)) for textos in item['conteudo']]
        categorias_limpas = w3lib.html.remove_tags(str(item['categorias']), keep=("a",))
        dados = {
            'url': item['url'],
            'codigo_http': item['codigo_http'],
            'titulo': item['titulo'],
            'conteudo': conteudo_limpo,
            'ligacoes': item['ligacoes'],
            'categorias': categorias_limpas,
            'imagem': item['imagem'] 
        }
        
        nome_arquivo = str(item['titulo']).replace(" ","_")
        substituicoes_nome_arquivo = ["[", "]", "'"]

        for substituicao in substituicoes_nome_arquivo:
            nome_arquivo = nome_arquivo.replace(substituicao, "")
        
        if item['codigo_http'] != 200:
            nome_arquivo = str(item['codigo_http']) + "_" + item['url'].split("/")[-1]

        with open(f"scrapers/arquivos_brutos/{nome_arquivo}.json", "w+", encoding="utf-8") as f:
            dados_convertidos = json.dumps(dados, ensure_ascii=False, indent=4)
            f.write(dados_convertidos)

        return item