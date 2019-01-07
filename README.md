# stock
## 同花顺http://basic.10jqka.com.cn/股票信息爬取
## 主要字段：
    b_cate = scrapy.Field()  # 大分类名称
    s_href = scrapy.Field()  # 中分类名称
    s_cate = scrapy.Field()  # 小分类名称
    stock_name = scrapy.Field()  # 股票名字
    stock_url = scrapy.Field()  # 股票地址
    business = scrapy.Field()  # 主营业务
    # concept_base = scrapy.Field()  # 主要概念
    # concept_other = scrapy.Field()  # 其他概念
    concept = scrapy.Field()  # 概念
## 延时1秒，太快会封。后续再破解
## 默认使用代理池，可以在setting中注释掉‘ProxyMiddleware’
