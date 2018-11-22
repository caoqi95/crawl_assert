# -*- coding: utf-8 -*-
import scrapy


class AssertSpiderSpider(scrapy.Spider):
    name = 'assert_spider'
    allowed_domains = ['assert.pub']
    start_urls = ['http://www.assert.pub']

    def parse(self, response):

        for item in response.css('div h5'):
            # 文章标题
            print(item.css('a::text').extract()[0])
            # 文章链接
            short = item.css('a::attr(href)').extract()[0]
            # 文章完整 url
            full_url = response.urljoin(short)
            print(full_url)
            yield{
                'paper': item.css('a::text').extract_first(),
                'url': response.urljoin(item.css('a::attr(href)').extract_first())
            }
