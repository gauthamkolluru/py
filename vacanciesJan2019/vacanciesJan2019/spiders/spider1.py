import scrapy
from scrapy.linkextractors import LinkExtractor as le
from bs4 import BeautifulSoup as bs


class spider1(scrapy.Spider):
    name = "spider1"
    start_urls=['https://www.valuelabs.com/valuelabs-careers/']
    def parse(self, response):
        links = le(unique=True).extract_links(response)
        for link in links:
            self.parse(link.url) if link.text == 'Current Openings' else print(None)
       #return self.read_response(response)

    #def read_response(self,html_body):
        #self.html_body = html_body
        #self.root = bs(self.html_body, 'lxml')
        #links =  le(canonicalize=True, unique=True).extract_links(self.html_body)
        #for link in links:
            #print(link.url) if link.text == 'Current Openings' else print(None)
