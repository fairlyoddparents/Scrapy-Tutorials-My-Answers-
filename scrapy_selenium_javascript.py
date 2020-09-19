# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from selenium import webdriver

class ScrapySeleniumJavascriptSpider(scrapy.Spider):
    name = 'scrapy_selenium_javascript'
    allowed_domains = ['toscrape.com/js']
    start_urls = ['http://quotes.toscrape.com/js']

    def __init__(self):
        self.driver = webdriver.PhantomJS()

    def parse(self, response):
        self.driver.get(response.url)
        response_selenium = Selector(text=self.driver.page_source)

        for quote in response_selenium.css("div.quote"):
            yield {
                'text': quote.css("span.text::text").extract_first(),
                'author': quote.css("small.author::text").extract_first(),
                'tags': quote.css("div.tags > a.tag::text").extract(),
            }

        self.driver.quit()
