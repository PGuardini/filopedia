import scrapy


class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"
    allowed_domains = ["pt.wikipedia.org"]
    start_urls = ["https://pt.wikipedia.org/wiki/"]

    def parse(self, response):
        pass
