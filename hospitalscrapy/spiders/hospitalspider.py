# -*- coding: utf-8 -*-
import scrapy


class HospitalspiderSpider(scrapy.Spider):
    name = "hospitalspider"
    allowed_domains = ["https://medical.yahoo.co.jp/hospital"]
    start_urls = ['http://https://medical.yahoo.co.jp/hospital/']

    def parse(self, response):
        pass
