import scrapy


class BlogSpider(scrapy.Spider):

    name = 'adressespider'

    start_urls = ['https://fr.kompass.com/a/transport-maritime-par-conteneurs/7535009/']


    def parse(self, response):

        for link in response.css('div.addressCoordinates p'):

            yield {'character': link.css('span ::text').extract_first()}
