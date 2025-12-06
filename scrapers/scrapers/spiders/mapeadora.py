import scrapy
from scrapers.items import ScrapersItem

class MapeadoraSpider(scrapy.Spider):
    name = "mapeadora"
    allowed_domains = ["plato.stanford.edu"]
    start_urls = ["https://plato.stanford.edu/contents.html"]

    custom_settings = {
        'ITEM_PIPELINES':{
            "scrapers.pipelines.MapeadoraPipeline": 300
        }
    }

    def parse(self, response):

        for url in response.css("div#content li"):
            item = ScrapersItem()
            
            if not url.css("a strong::text").get():
                item["titulo"] = url.css("li *::text")[1].get()
            else:
                item['titulo'] = url.css("a strong::text").get()
            
            item['url'] = f"erdfhttps://plato.stanford.edu/{url.css("a::attr(href)").get()}"

            yield item
