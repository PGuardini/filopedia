import scrapy
from philoscrapper.items import PhiloscrapperItem

class MapeadoraSpider(scrapy.Spider):
    name = "mapeadora"
    allowed_domains = ["plato.stanford.edu"]
    start_urls = ["https://plato.stanford.edu/contents.html"]

    custom_settings = {
        "FEEDS": {
            "urls.json":{
                "format": "json"
            }
        }
    }

    def parse(self, response):

        for url in response.css("div#content li"):
            item = PhiloscrapperItem()
            
            if not url.css("a strong::text").get():
                item["titulo"] = url.css("li *::text")[1].get()
            else:
                item['titulo'] = url.css("a strong::text").get()
            
            item['url'] = f"erdfhttps://plato.stanford.edu/{url.css("a::attr(href)").get()}"

            yield item
