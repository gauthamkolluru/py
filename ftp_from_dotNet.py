import scrapy

class xmlFileSpider(scrapy.Spider):
    name = 'xmlFile'
    start_urls = ['ftp://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/',]

    def parse(self,response):
        print(response)