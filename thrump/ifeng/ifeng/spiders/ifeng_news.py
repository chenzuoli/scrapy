# -*- coding: utf-8 -*-
import scrapy


class IfengNewsSpider(scrapy.Spider):
    name = 'ifeng_news'
    #allowed_domains = ['ifeng.com']
    start_urls = ['http://ifeng.com/']

    def parse(self, response):
        yield {
            'html': response.css("a::attr(href)").extract()
        }
