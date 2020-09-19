# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        authors_urls = response.css('div.quote > span > a::attr(href)').extract()
        for author_url in authors_urls:
            url = response.urljoin(author_url)
            yield scrapy.Request(url = url, callback = self.parse_author_details)

        #follow pagination
        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_author_details(self, response):
        yield {
            'author_name:' response.css('h3.author-title::text').extract_first(),
            'birth_date': response.css('span.author-born-date::text').extract_first()
        }
