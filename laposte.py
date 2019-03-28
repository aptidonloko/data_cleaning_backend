# -*- coding: utf-8 -*-
import scrapy


class BlogSpider(scrapy.Spider):

    name = 'adressespider'

    start_urls = ['https://annuaire.laposte.fr/transport-maritime/marseille/']


    def parse(self, response):

        for link in response.css('div.uiSerpResults div#serp-list.uiSerpList div.coData a.uiSerpAddress.uaLv3'):

            yield {'adresse': link.css('a ::text').extract_first()}

