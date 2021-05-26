import scrapy


class OnsSpider(scrapy.Spider):
    name = 'ons'
    start_urls = ['https://www.ons.dz/spip.php?rubrique124']

    def parse(self, response):
        for link in response.css('.acces-rapide'):
            yield {'link': link.css('a::attr(href)').get()}
