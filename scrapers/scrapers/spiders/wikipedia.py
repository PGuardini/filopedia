from pathlib import Path
import scrapy

class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"
    allowed_domains = ["pt.wikipedia.org"]
    
    start_urls = []

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"{page}'s-page.html"

        Path(f"artigos/{filename}").write_bytes(response.body)

        yield {
            "title": response.css("title::text").getall()
        }

        self.log(f"Saved file {filename}")

