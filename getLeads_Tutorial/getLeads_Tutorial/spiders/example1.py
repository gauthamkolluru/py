# -*- coding: utf-8 -*-
import scrapy


class Example1Spider(scrapy.Spider):
    name = 'example1'
    allowed_domains = ['https://gauthamsk.me']

    start_urls = ['https://gauthamsk.me',]
    #def start_requests(self):
    #    urls = ['https://gauthamsk.me/',]
    #    for url in urls:
    #        yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        print(dir(response.text))
