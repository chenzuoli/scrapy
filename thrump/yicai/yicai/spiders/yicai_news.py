# -*- coding: utf-8 -*-
import scrapy


class YicaiNewsSpider(scrapy.Spider):
    name = 'yicai_news'
    # allowed_domains = ['yicai.com/news']
    start_urls = ['https://www.yicai.com/news/']

    def parse(self, response):
        yield {
            'html': response.css("a::attr(href)").extract()
        }
