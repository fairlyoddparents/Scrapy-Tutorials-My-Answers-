# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from selenium import webdriver

class ScrapePrices(scrapy.Spider):
    name = 'scrape_prices'
    allowed_domains = ['.com']
    start_urls = ['http://econpy.pythonanywhere.com/ex/001.html']

    def __init__(self):
        self.driver = webdriver.PhantomJS()

    def parse(self, response):
        self.driver.get(response.url)
        response_selenium = Selector(text=self.driver.page_source)

        for buyer in response_selenium.css('div[title=buyer-info]'):
            item = {'buyer': buyer.css('div[title=buyer-name]::text').get(),
                    'price': buyer.css('span::text').get()
                    }
            yield item

        self.driver.quit()

        #while True:
            #next = self.driver.find_elements_by_xpath('//a[@href="www.example.com"]')
            #try:
                #next.click()
                #code to extract data
            #except:
                #break

        #see https://stackoverflow.com/questions/50259652/how-to-use-selenium-with-scrapy-for-crawling-ajax-pages  ####best!!!!
        #see https://stackoverflow.com/questions/17975471/selenium-with-scrapy-for-dynamic-page
