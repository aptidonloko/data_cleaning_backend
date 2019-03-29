import scrapy


class BlogSpider(scrapy.Spider):

    name = 'adressespider'

    start_urls = ['https://fr.kompass.com/c/bollore-logistics/fr8209705/']


    def parse(self, response):

        for link in response.css('div.headerRowTop div.infos div.addressCoordinates p span'):

            yield {'character': link.css('span ::text').extract_first()}

