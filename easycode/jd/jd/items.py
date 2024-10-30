# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    b_cate = scrapy.Field()
    m_cate = scrapy.Field()
    s_cate = scrapy.Field()
    b_cate_url = scrapy.Field()
    b_cate_name = scrapy.Field()
    m_cate_url = scrapy.Field()
    m_cate_name = scrapy.Field()
    s_cate_url = scrapy.Field()
    s_cate_name = scrapy.Field()

class Product(scrapy.Item):
    """
    商品数据模型类：用于存储商品信息（Product）
    product_category    商品类别
    product_sku_id      商品id
    product_name        商品名称
    product_img_url     商品图片url
    product_book_info   图书信息，作者，出版社
    product_option      商品选项
    product_shop        商品店铺
    product_comments    商品评论数量
    product_ad          商品促销
    product_price       商品价格
    """

    product_category = scrapy.Field()
    product_category_id = scrapy.Field()
    product_sku_id = scrapy.Field()
    product_name = scrapy.Field()
    product_img_url = scrapy.Field()
    product_book_info = scrapy.Field()
    product_option = scrapy.Field()
    product_shop = scrapy.Field()
    product_comments = scrapy.Field()
    product_ad = scrapy.Field()
    product_price = scrapy.Field()
    product_good_comments = scrapy.Field()
    product_poor_comments = scrapy.Field()

class Mm(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()