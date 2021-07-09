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
        gift_eligibility =  response.xpath("//span[@class='copy-small font-bold']/text()").get()
        available_colors = response.xpath("//div[@class='variants__list']/input/@aria-label").getall()
        picture = response.xpath("//img[@class='hover-zoom-hero-image']/@src").get()
        picture_url = "https:" + picture.split('?')[0]
        product_features = response.xpath("//div[@class='collapsable-about-product-container']/div/section/div/div/div[@class='about-item-collapsable-features xxs-margin-left m-margin-top']/div/div/text()").get()
        available_sizes = response.xpath("//label[@availabilitystatus='AVAILABLE']/div/div[@class='var__overlay']/@data-label").getall()
        review_dates = response.xpath("//span[@class='review-date-submissionTime']/text()").getall()
        review_ratings = response.xpath("//span[@class='visuallyhidden seo-avg-rating']/text()").getall()[1:]

        yield { 
            'product title' : product_title,
            'product link' : response.url,
            'product rating' : float(rating),
            'number of ratings' : int(no_of_reviews.split()[0]),
            'product starting price' : starting_price,
            'product ending price' : ending_price,
            'available sizes' : available_sizes,
            'available colors' : available_colors,
            'categories' : categories,
            'delivery period' : delivery_period,
            'gift eligibility' : gift_eligibility,
            'main picture url' : picture_url,
            'features' : product_features,
            'reviews' : [(review_date, review_rating) for review_date, review_rating in zip(review_dates, review_ratings)]
        }   