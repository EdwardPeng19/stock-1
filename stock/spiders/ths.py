# -*- coding: utf-8 -*-
import scrapy
from stock.items import StockItem
from copy import deepcopy
from urllib.parse import urljoin


class ThsSpider(scrapy.Spider):
    name = 'ths'
    allowed_domains = ['10jqka.com.cn']
    start_urls = ['http://basic.10jqka.com.cn/']

    def parse(self, response):
        print(response.url)
        div_list = response.xpath("//div[contains(@class,'category')]")  # 大分类列表
        for div in div_list[1:2]:
            item = StockItem()
            item["b_cate"] = div.xpath("./div[@class='c_title']//h2/text()").extract_first()
            a_list = div.xpath(".//div[@class='option_group clearfix']/div")  # 小分类列表
            for a in a_list:
                item["s_href"] = a.xpath("./a/@href").extract_first()
                item["s_cate"] = a.xpath("./a/text()").extract_first()
                if item["s_href"] is not None:
                    item["s_href"] = urljoin(response.url,item["s_href"])
                    yield scrapy.Request(
                        item["s_href"],
                        callback=self.parse_stock_list,
                        meta={"item":deepcopy(item),
                              'download_timeout': 10,
                              },
                        dont_filter=True
                    )

    def parse_stock_list(self, response):  # 解析列表页
        item = response.meta["item"]
        li_list = response.xpath("//div[@class='c_content clearfix']/a")
        for li in li_list:
            # item["stock_name"] = li.xpath("./text()").extract_first()
            item["stock_url"] = li.xpath("./@href").extract_first()
            item["stock_url"] = urljoin(response.url,item["stock_url"])
            yield scrapy.Request(
                item["stock_url"],
                callback=self.parse_data_list,
                meta={"item": deepcopy(item),
                      'download_timeout': 10,
                      },
                dont_filter=True
            )
    def parse_data_list(self, response):  # 解析数据页
        item = response.meta["item"]
        item["stock_name"] = []
        stock = response.xpath("//div[@class='code fl']/h1/a/text()").extract()
        for i in stock:
            item["stock_name"].append(i.strip())
        item["business"] = response.xpath("//span[@class='tip f14 fl']/a/@title").extract_first()
        # concept_url = response.xpath("//a[@class='alltext newtaid']/@href").extract_first()
        # concept_url = urljoin(response.url,concept_url)
        yield item
        # yield scrapy.Request(
        #     concept_url,
        #     callback=self.parse_concept,
        #     meta={"item": deepcopy(item)}
        # )
        # print(item)
    # def parse_concept(self, response):  # 解析概念页
    #     item = response.meta["item"]
    #     concept = []
    #     concept_base = response.xpath("//td[@class='gnName']/text()").extract()
    #     for i in concept_base:
    #         concept.append(i.strip())
    #     concept_other = response.xpath("//td[@class='gnStockList']/text()").extract()
    #     for i in concept_other:
    #         concept.append(i.strip())
    #     item["concept"] = str(concept)
    #     print(item)
    #     yield item
