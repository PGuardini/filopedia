from pathlib import Path
import scrapy
from lista_urls import Listagem

class SepSpider(scrapy.Spider):
    name = "sep"
    allowed_domains = ["plato.stanford.edu"]
    lista_urls = Listagem()
    start_urls = lista_urls.lista_url_artigos

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"{page}'s-page.html"

        Path(f"artigos/{filename}").write_bytes(response.body)

        yield {
            "title": response.css("title::text").getall()
        }

        self.log(f"Saved file {filename}")

        #>>> response.css("title::text").get().replace("(Stanford Encyclopedia of Philosophy)", "")