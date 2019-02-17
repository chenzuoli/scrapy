# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    #allowed_domains = ['ifeng.com']
    start_urls = ['http://ifeng.com/']

    def parse(self, response):
        yield {
            'html': response.css("a::attr(href)").extract()
        }
