# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis

class BosszpPipeline(object):
    def process_item(self, item, spider):
        return item


#保存到redis
class BosszpRedisPipeline(object):

    def __init__(self):
        self.redis_cli1 =redis.StrictRedis(
                host='192.168.1.3',
                port=6379,
                db=1,
                password='zzhabc123'
        )
        self.redis_cli2 =redis.StrictRedis(
                host='192.168.1.3',
                port=6379,
                db=2,
                password='zzhabc123'
        )

    def process_item(self, item, spider):
        self.redis_cli1.lpush('job',item['job'])
        self.redis_cli2.lpush('pay', item['pay'])
        return item