# -*- coding: utf-8 -*-
import scrapy
import json
import sys
import imp
imp.reload(sys)

class ContentSpider(scrapy.Spider):
    name = 'content'

    def start_requests(self):
        urls = []
        filepath = getattr(self, "filepath", None)
        print (filepath)
        with open(filepath, 'r') as jsonline:
                strs=jsonline.readlines()
        for line in strs:
            json_dict=json.loads(line)
            html=json_dict['html']
            urls.append(str(html).strip())
        count_page=0
        for url in urls:
            if url == None or url == "":
                continue
            if url.endswith(".com") or url.endswith(".com/") or url.endswith(".cn") or url.endswith(".cn/") or url.endswith("javascript:void(0);") or url.endswith("null"):
                continue
            if url.find("//") == 0:
                url = "http:" + url
            url = url.strip()
            #print "###################url: " + url
            count_page+=1
            yield scrapy.Request(url=url, callback=self.parse)
        #print "###################page count: " + str(count_page)

    def parse(self, response):
        yield {
            'title': response.css("title::text").extract_first(),
            'content': response.css("div div div div p::text").extract(),
            'html': response.url,
            'author': response.css("div div p span span a::text").extract_first(),
            'publish_time': response.css("p span::text").extract_first(),
            'img': response.css('p img::attr(src)').extract()
        }
