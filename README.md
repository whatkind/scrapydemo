# 项目快速创建
- 创建项目
```shell
scrapy startproject [项目名]
```
- 创建spider
```shell
scrapy genspider [爬虫程序名] [域名]
# 例如
scrapy genspider baidu baidu.com
```

- 运行spider
```shell
scrapy crawl [爬虫程序名]
# 输出数据
scrapy crawl [爬虫程序名] -o [文件名]
# 例如
scrapy crawl baidu
```