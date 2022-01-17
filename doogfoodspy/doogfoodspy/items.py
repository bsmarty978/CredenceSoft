# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoogfoodspyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ProductName  = scrapy.Field()
    Price  = scrapy.Field()
    Description  = scrapy.Field()
    Attributes  = scrapy.Field()
    Brand  = scrapy.Field()
    Brand_url = scrapy.Field()
    ingredients  = scrapy.Field()
    Key_Benefits  = scrapy.Field()
    Guaranteed_Analysis  = scrapy.Field()
    Images = scrapy.Field()
