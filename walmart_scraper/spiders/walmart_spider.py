import scrapy
import time

class WalmartSpiderSpider(scrapy.Spider):
    name = 'walmart_spider'
    allowed_domains = ['walmart.com']
    start_urls = ['https://walmart.com/ip/IZOD-Men-s-Short-Sleeve-Advantage-Chest-Stripe-Polo/486362422']
    handle_httpstatus_list = [301]

    def parse(self, response):
        request = scrapy.Request(url=self.start_urls[0], callback=self.parse_url)
        request.meta['proxy'] = "136.226.18.238:443"
        yield request

    def parse_url(self, response):
        product_title = response.xpath("//div[@id='product-overview']/div/div[3]/div/h1/text()")
        yield { 
            'prod title' : product_title
        }