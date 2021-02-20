# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from itemadapter import ItemAdapter


class ScrapydemoPipeline:
    def open_spider(self, spider):
        self.filename = open('dataFile/films.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # 假如要使用json，MaoyanSpider请使用第一种数据传输方式
        # with open('dataFile/films.json', 'a', encoding='utf-8') as f:
        #     f.write(json.dump(item, ensure_ascii=False)+'\n')
        # self.filename.write(json.dumps(item, ensure_ascii=False)+'\n')
        # 假如要使用MaoyanSpider第二种方式保存json
        self.filename.write(json.dumps(dict(item), ensure_ascii=False)+'\n')
        return item

    def close_spider(self, spider):
        self.filename.close()
