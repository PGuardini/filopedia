from pathlib import Path
import scrapy
from scrapers.items import WikipediaItem
import json

class WikipediaSpider(scrapy.Spider):
    """
        Aranha que extrai os dados da Wikipedia, percorrendo todos os
        links coletados pela aranha mapeadora.

    """


    name = "wikipedia"
    allowed_domains = ["pt.wikipedia.org"]

    custom_settings = {
        'ITEM_PIPELINES':{
            "scrapers.pipelines.WikipediaPipeline": 300
        }
    }


    
    with open("urls.json", "r", encoding="utf-8") as arquivo:
        lista_urls = json.load(arquivo)
        lista_urls_wikipedia = [list(dicionario.values())[0] for dicionario in lista_urls]

    start_urls = lista_urls_wikipedia

    def parse(self, response):
            
        item = WikipediaItem()

        item['url'] = response.url
        item['codigo_http'] = response.status
        item['titulo'] = response.css("h1#firstHeading > span.mw-page-title-main::text").getall()
        item['conteudo'] = response.css("div.mw-parser-output > p").getall()
        item['ligacoes'] = response.css("div.mw-parser-output > ul").getall()
        item['categorias'] = response.css("div#mw-normal-catlinks > ul").getall()
        item['imagem'] = response.css("td.infobox-image img::attr(src)").get()   

        yield item
        