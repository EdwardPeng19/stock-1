# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StockItem(scrapy.Item):
    # define the fields for your item here like:
    collection = 'ths1'

    b_cate = scrapy.Field()
    s_href = scrapy.Field()
    s_cate = scrapy.Field()
    stock_name = scrapy.Field()
    stock_url = scrapy.Field()
    business = scrapy.Field()
    concept_base = scrapy.Field()
    concept_other = scrapy.Field()
    concept = scrapy.Field()



