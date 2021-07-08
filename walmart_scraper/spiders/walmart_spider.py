import scrapy


class WalmartSpiderSpider(scrapy.Spider):
    name = 'walmart_spider'
    allowed_domains = ['walmart.com']
    start_urls = ['http://walmart.com/']

    def parse(self, response):
        pass
