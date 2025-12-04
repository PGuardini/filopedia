import json
import re

class Listagem:

    def __init__(self):
        self._lista_titulos = self.lista_titulos()
        self._lista_filosofos = self.lista_filosofos(self._lista_titulos)
        self._lista_url_artigos = self.lista_urls_filosofos(self._lista_filosofos)


    def lista_urls(self) -> list:
        """Retorna a lista de urls do arquivo JSON extraído pela aranha mapeadora"""

        with open('urls.json', 'r+', encoding="utf-8") as urls:
            urls = json.load(urls)

        lista_urls = [dict(url)['url'] for url in urls]

        return lista_urls

    def lista_titulos(self) -> list:
        """Retorna a lista de titulos do arquivo JSON"""
        
        with open('urls.json', 'r+', encoding="utf-8") as titulos:
            titulos = json.load(titulos)

        lista_titulos = [dict(titulo)['titulo'] for titulo in titulos]

        return lista_titulos

    def lista_filosofos(self, lista_titulos) -> list:
        """Retorna uma lista com os nomes de todos os filósofos"""

        lista_filosofos = []

        for titulo in lista_titulos:
            #nomes_simples = re.search(r"\w[a-z]{1,}", titulo)
            nomes_romanizados = re.match(r"((^[A-Z][a-z]+, )(\w+[ .]?)+)", titulo)
            nomes_arabes_al = re.match(r"(^al-\w+)", titulo)
            nomes_arabes_ibn = re.match(r"(^Ibn \w+(\[\w+\])?)", titulo)
            nomes_sem_separacao = re.match(r"((^[A-Z][a-z]+ )(\w+ ?)+)", titulo)

            if nomes_romanizados or nomes_arabes_al or nomes_arabes_ibn or nomes_sem_separacao:
                lista_filosofos.append(titulo)

        return lista_filosofos

    def lista_urls_filosofos(self, lista_filosofos) -> list:
        """Retorna uma lista com as urls de pagina da wikipedia dos filosofos"""

        urls_filosofos = [f"https://pt.wikipedia.org/wiki/{filosofo}" for filosofo in lista_filosofos]

        return urls_filosofos


    @property
    def lista_url_artigos(self):
        return self._lista_url_artigos
