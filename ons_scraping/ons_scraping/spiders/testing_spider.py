import json
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from os import path
from ons_scraping.items import OnsScrapingItem

if path.exists('ons.json') == True :

    class OnsPDF(scrapy.Spider):
        name = 'ons_pdf'
        f = open('ons.json')
        data = json.load(f)
        start_urls = []
        for li in data:
            start_urls.append("https://www.ons.dz/{}".format(li['link']))

        rules = (
            Rule(LinkExtractor(allow = r'Items/'),
                 callback = 'parse_item',
                 follow = True),
        )

        def parse(self, response):
            for link in response.css('#document_articles'):
                file_url = "https://www.ons.dz/{}".format(link.css('a::attr(href)').get())
                file_url = response.urljoin(file_url)
                item = OnsScrapingItem()
                item['file_urls'] = [file_url]
                yield item
else :
  pass
