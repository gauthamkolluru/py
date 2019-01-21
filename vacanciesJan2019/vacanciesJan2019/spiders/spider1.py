import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as le
from bs4 import BeautifulSoup as bs

class FollCareer(CrawlSpider):
    name = 'spider1'
    allowed_domains = ['valuelabs.com']
    start_urls = ['https://www.valuelabs.com/valuelabs-careers/']
    rules = (
            Rule
                (le
                    (
                        allow = ('/current-job-postings',)
                    )
                )
            )


    def parse_page(self, response):
        print(response.body)
