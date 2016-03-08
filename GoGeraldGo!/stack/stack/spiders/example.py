# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["example.cpm"]
    start_urls = (
        'http://www.example.cpm/',
    )

    def parse(self, response):
        pass
