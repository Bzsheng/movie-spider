# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import pymysql.cursors
from demo.items import movieItem

class DemoPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(user = 'root', db = 'movie', password = 'w123456',
                                    host = 'localhost', charset = 'utf8', use_unicode = True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            insert into movie(title, url, info) value (%s, %s, %s)
        """
        self.cursor.execute(insert_sql, (item['title'], item['url'], item['info']))
        self.conn.commit()
