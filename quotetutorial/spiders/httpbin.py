# -*- coding: utf-8 -*-
import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['www.httpbin.org']
    start_urls = ['http://www.httpbin.org/post/']

    def start_requests(self):
        yield scrapy.Request(url='http://www.httpbin.org/post', method='POST', callback=self.parse_post)

    def parse(self, response):
        pass

    def parse_post(self, response):
        self.logger.info(response.status)
        print('hello: ', response.text)
