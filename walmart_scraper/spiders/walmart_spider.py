import scrapy
import time

class WalmartSpiderSpider(scrapy.Spider):
    name = 'walmart_spider'
    allowed_domains = ['walmart.com']
    start_urls = ['https://walmart.com/ip/IZOD-Men-s-Short-Sleeve-Advantage-Chest-Stripe-Polo/486362422']

    def parse(self, response):
        request = scrapy.Request(url=self.start_urls[0], callback=self.parse_url)
        request.meta['redirect_enabled'] = False
        yield request

    def parse_url(self, response):
        product_title = response.xpath("//div[@id='product-overview']/div/div[3]/div/h1/text()").get()
        rating = response.xpath("//span[@itemprop='ratingValue']/text()").get()
        no_of_reviews = response.xpath("//span[@class='stars-reviews-count-node']/text()").get()
        starting_price = response.xpath("//span[@itemprop='lowPrice']/text()").get()
        ending_price = response.xpath("//span[@itemprop='highPrice']/text()").get()
        categories = response.xpath("//span[@itemprop='name']/text()").getall()
        delivery_period = response.xpath("//div[@class='ShippingMessage-container fulfillment-shipping-msg-tile  color-black']/text()").get()
        original_price = response.xpath("//span[@class='visuallyhidden']/text()").get()
        gift_eligibility =  response.xpath("//span[@class='copy-small font-bold']/text()").get()
        available_colors = response.xpath("//div[@class='variants__list']/input/@aria-label/text()").getall()
        picture = response.xpath("//img[@class='hover-zoom-hero-image']/@src").get()
        picture_url = "https:" + picture.split('?')[0]
        product_features = response.xpath("//div[@class='collapsable-about-product-container']/div/section/div/div/div[@class='about-item-collapsable-features xxs-margin-left m-margin-top']/div/div/text()").get()

        yield { 
            'product title' : product_title,
            'rating' : float(rating),
            'number of people who rated' : int(no_of_reviews.split()[0]),
            'starting price' : starting_price,
            'ending price' : ending_price,
            'categories' : categories,
            'delivery period' : delivery_period,
            'original price' : original_price,
            'gift eligibility' : gift_eligibility,
            'available colors' : available_colors,
            'main picture url' : picture_url,
            'product features' : product_features,
        }   