# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

#https://blog.csdn.net/weixin_42260204/article/details/81100897 该模块参考文档
#继承模板crawlspider     scrapy genspider -t crawl boss zhipin.com
class BossSpider(CrawlSpider):
    name = 'boss'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101280100/?query=python&page=1&ka=page-1']

    rules = (
        #翻页地址 ,python为关键词的话只有七页，可以使用it等
        Rule(LinkExtractor(allow=r'page'), follow=True),
        #详情页地址获取，且继续获取，可实现全站
        Rule(LinkExtractor(allow=r'job_detail/.*?~.html'), callback='parse_item',follow=True),
    )

    def parse_item(self, response):
        item = {}
        #获取岗位名称
        item['job'] = response.xpath('//div/div[@class="name"]/h1/text()').get()
        #获取岗位薪资
        item['pay'] = response.xpath('//div/div[@class="name"]/span/text()').get()

        return item
