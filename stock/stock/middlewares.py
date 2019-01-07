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
        request.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        request.headers['Host'] = 'basic.10jqka.com.cn'
        request.headers['Cache-Control'] = 'max-age=0'
        # cookie = [{'searchGuide':'sg','reviewJump':'nojump', 'usersurvey':'1','v':'AgpryOi3Ynalne7a0RYCLxvcW_uv-45VgH8C-ZRDtt3oR6StfIveZVAPUg1n'},
        #           {'searchGuide': 'sg', 'reviewJump': 'nojump', 'usersurvey': '1','v': 'AgZnxIwLpiJYt3JGOY3G-zcIV_eLZ0ohHKt-hfAv8ikE86ihWPeaMew7zpHD'},
        #           {'searchGuide': 'sg', 'reviewJump': 'nojump', 'usersurvey': '1','v': 'Ag9uez24jzX5FIvJCGV_zHZLnqgaNGNW_YhnSiEcq36F8CFeKQTzpg1Y954y'},
        #           {'searchGuide': 'sg', 'reviewJump': 'nojump', 'usersurvey': '1','v': 'AmsKF3Fss4H9aO9V1FXTuPLH-oRWgH8C-ZRDtt3oR6oBfIVyZVAPUglk0wLu'},
        #           {'searchGuide': 'sg', 'reviewJump': 'nojump', 'usersurvey': '1','v': 'AiVEOfvOlReLUfFLjXe17tiFNOpcYtn0Ixa9SCcK4dxrPksc77LpxLNmzRy0'},
        #           ]
        # request.cookies = random.choice(cookie)
        # self.logger.debug('使用请求头 ' + user_agents)

class ProxyMiddleware():
    def __init__(self,proxy_url):
        self.logger = logging.getLogger(__name__)
        self.proxy_url = proxy_url
        self.count = 25

    def get_random_proxy(self):
        try:
            response = requests.get(self.proxy_url)
            if response.status_code == 200:
                proxy = response.text
                return proxy
        except requests.ConnectionError:
            return False

    def process_response(self, request, response, spider):
        if response.status == 403:
            # request.meta["proxy"] = proxyServer
            # request.headers["Proxy-Authorization"] = proxyAuth
            # self.logger.debug('使用代理 ' + proxyServer)
            self.logger.debug('请求失败 ','*'*50 )
            proxy = self.get_random_proxy()
            if proxy:
                uri = 'https://{proxy}'.format(proxy=proxy)
                self.logger.debug('使用代理 ' + uri)
                request.meta['proxy'] = uri
        return response

    def process_request(self, request, spider):
        self.count -= 1
        # print(self.count)
        if self.count == 0:
            proxy = self.get_random_proxy()

            if proxy:
                uri = 'https://{proxy}'.format(proxy=proxy)
                self.logger.debug('使用代理 ' + uri)
                request.meta['proxy'] = uri
                # self.logger.debug('使用代理 ' + proxyServer)
                # request.meta["proxy"] = proxyServer
                # request.headers["Proxy-Authorization"] = proxyAuth
                self.count = 25

        elif request.meta.get('Retrying'):
            self.logger.debug('请求失败 ','*'*50 )
            proxy = self.get_random_proxy()
            # request.meta["proxy"] = proxyServer
            # request.headers["Proxy-Authorization"] = proxyAuth
            # self.logger.debug('使用代理 ' + proxyServer)
            if proxy:
                uri = 'https://{proxy}'.format(proxy=proxy)
                self.logger.debug('使用代理 ' + uri)
                request.meta['proxy'] = uri

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(
            proxy_url=settings.get('PROXY_URL')
        )
