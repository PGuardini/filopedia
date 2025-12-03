from pathlib import Path
import scrapy
from lista_urls import lista_urls as urls_artigos

class SepSpider(scrapy.Spider):
    name = "sep"
    allowed_domains = ["plato.stanford.edu"]
    start_urls = urls_artigos()

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"{page}'s-page.html"

        Path(f"artigos/{filename}").write_bytes(response.body)

        yield {
            "title": response.css("title::text").getall()
        }

        self.log(f"Saved file {filename}")

        #>>> response.css("title::text").get().replace("(Stanford Encyclopedia of Philosophy)", "")