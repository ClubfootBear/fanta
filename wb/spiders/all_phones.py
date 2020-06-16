# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AllPhonesSpider(CrawlSpider):
    name = 'all_phones'
    allowed_domains = ['www.wildberries.ru']
    start_urls = ['https://www.wildberries.ru/catalog/elektronika/smartfony-i-telefony/vse-smartfony']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class="dtList-inner"]/span/span/span/a'), callback='parse_item', follow=True),
    )


    def parse_item(self, response):
        yield{
            'Марка телефона': response.xpath('//span[@class="brand"]/text()').get(),
            'Модель телефона': response.xpath('//span[@class="name"]/text()').get().strip(),
            'URL карточки телефона': response.xpath('//link[2]/@href').get(),
            'Количество комментариев': response.xpath('//a[@id="comments_reviews_link"]/span/i/text()').get().strip(),
            'Количество покупок': response.xpath('//span[@class="j-orders-count"][1]//text()').get(),
            'Цена телефона': response.xpath('//span[@class="final-cost"]/text()').get().strip()
        }
        