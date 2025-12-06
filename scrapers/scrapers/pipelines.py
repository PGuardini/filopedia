from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import re
import json

class MapeadoraPipeline:
    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item

    def process_item(self, item, spider):
        titulo = item['titulo']

        nomes_romanizados = re.match(r"((^[A-Z][a-z]+, )(\w+[ .]?)+)", titulo)
        nomes_arabes_al = re.match(r"(^al-\w+)", titulo)
        nomes_arabes_ibn = re.match(r"(^Ibn \w+(\[\w+\])?)", titulo)
        nomes_sem_separacao = re.match(r"((^[A-Z][a-z]+ )(\w+ ?)+)", titulo)

        if nomes_romanizados or nomes_arabes_al or nomes_arabes_ibn or nomes_sem_separacao:
            if "," in titulo:
                nome_filosofo_dividido = titulo.split(", ")
                nome_filosofo = f"{nome_filosofo_dividido[-1]}_{nome_filosofo_dividido[0]}"
                nome_filosofo.replace(" ","_")
            else:
                nome_filosofo = titulo.replace(" ","_")
        else:
            raise DropItem("O título não é um nome")
        

        dado_formatado = {
                nome_filosofo: f"https://pt.wikipedia.org/wiki/{nome_filosofo}"
            }

        try:
            with open("urls.json", "r+", encoding="utf-8") as urls:
                lista_urls = json.load(urls)
        except:
            lista_urls = []

        if isinstance(lista_urls, list):
            lista_urls.append(dado_formatado)
        

        with open("urls.json", "w+", encoding="utf-8") as urls:
            json.dump(lista_urls, urls, indent=4, ensure_ascii=False)
            

        return nome_filosofo