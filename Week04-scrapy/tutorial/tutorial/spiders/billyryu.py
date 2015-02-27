# -*- coding: utf-8 -*-
import scrapy


class BillyryuSpider(scrapy.Spider):
    name = "billyryu"
    allowed_domains = ["billyryu.com"]
    start_urls = (
        'http://www.billyryu.com/',
    )

    def parse(self, response):
        for sel in response.xpath('//div:work-list'):
        	title = sel.xpath('//span:work-list-title/a/text()').extract()
        	link = sel.xpath('//span:work-list-title/a/@href()').extract()
        	desc = sel.xpath('//span:work-list-desc()/text()').extract()
        	print title, link, desc