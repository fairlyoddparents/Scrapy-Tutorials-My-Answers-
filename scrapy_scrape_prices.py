# -*- coding: utf-8 -*-
import scrapy

class ScrapePrices(scrapy.Spider):
    name = 'scrape_prices'
    allowed_domains = ['.com']
    start_urls = ['http://econpy.pythonanywhere.com/ex/001.html']

    def parse(self, response):
        for buyer in response.css('div[title=buyer-info]'):
            item = {'buyer': buyer.css('div[title=buyer-name]::text').get(),
                    'price': buyer.css('span::text').get()
                    }
            yield item
