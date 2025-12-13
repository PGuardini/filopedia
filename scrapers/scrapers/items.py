# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titulo = scrapy.Field()
    url = scrapy.Field()

class WikipediaItem(scrapy.Item):
    url = scrapy.Field()
    codigo_http = scrapy.Field()
    titulo = scrapy.Field()
    conteudo = scrapy.Field()
    ligacoes = scrapy.Field()
    categorias = scrapy.Field()
    imagem = scrapy.Field()