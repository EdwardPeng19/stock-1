# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
import requests
import logging
from stock.user_agents import user_agents
from scrapy.http import HtmlResponse
import base64

# 代理服务器
proxyServer = "http://http-dyn.abuyun.com:9020"

# 代理隧道验证信息
proxyUser = "H01234567890123D"
proxyPass = "D0B7B78FE5A50514"
proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")

class RandomUserAgentMiddleware():
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.user_agents = user_agents

    def process_request(self, request, spider):
        user_agents = random.choice(self.user_agents)
        request.headers['User-Agent'] = user_agents
        # self.logger.debug('使用请求头 ' + user_agents)

class ProxyMiddleware():
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        # self.proxy_url = proxy_url
        self.count = 30

    # def get_random_proxy(self):
    #     try:
    #         response = requests.get(self.proxy_url)
    #         if response.status_code == 200:
    #             proxy = response.text
    #             return proxy
    #     except requests.ConnectionError:
    #         return False

    # def process_response(self, request, response, spider):
    #     if response.status == 403:
    #         self.logger.debug('请求失败403 ', '*' * 50)
    #         proxy = self.get_random_proxy()
    #         if proxy:
    #             uri = 'https://{proxy}'.format(proxy=proxy)
    #             self.logger.debug('使用代理 ' + uri)
    #             response.headers['proxy'] = uri
    #     return response

    def process_request(self, request, spider):
        self.count -= 1
        # print(self.count)
        if self.count == 0:
            # proxy = self.get_random_proxy()
            # uri = 'https://{proxy}'.format(proxy=proxy)
            self.logger.debug('使用代理 ' + proxyServer)
            # request.meta['proxy'] = uri
            request.meta["proxy"] = proxyServer
            request.headers["Proxy-Authorization"] = proxyAuth
            self.count = 30

        if request.meta.get('Retrying'):
            self.logger.debug('请求失败 ','*'*50 )
            request.meta["proxy"] = proxyServer
            request.headers["Proxy-Authorization"] = proxyAuth
            # proxy = self.get_random_proxy()
            # if proxy:
            #     uri = 'https://{proxy}'.format(proxy=proxy)
            #     self.logger.debug('使用代理 ' + uri)
            #     request.meta['proxy'] = uri

        if request.meta.get('403'):
            self.logger.debug('请求失败403 ', '*' * 50)
            request.meta["proxy"] = proxyServer
            request.headers["Proxy-Authorization"] = proxyAuth
            # proxy = self.get_random_proxy()
            # if proxy:
            #     uri = 'https://{proxy}'.format(proxy=proxy)
            #     self.logger.debug('使用代理 ' + uri)
            #     request.meta['proxy'] = uri

    # @classmethod
    # def from_crawler(cls, crawler):
    #     settings = crawler.settings
    #     return cls(
    #         proxy_url=settings.get('PROXY_URL')
    #     )

    def process_exception(self,request, exception, spider):
        self.logger.debug('Get Exception')
        self.logger.debug('Try Second Time')

        request.meta["proxy"] = proxyServer
        request.headers["Proxy-Authorization"] = proxyAuth
        # proxy = self.get_random_proxy()
        # if proxy:
        #     uri = 'https://{proxy}'.format(proxy=proxy)
        #     self.logger.debug('使用代理 ' + uri)
        #     # request.meta['proxy'] = uri
        #     request.meta['proxy'] = uri  # 设置request的代理，如果请求的时候，request会自动加上这个代理
        return request
