import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from doogfoodspy.items import DoogfoodspyItem #NOTE:To Use IteamLoader


class ChweyspySpider(CrawlSpider):
    name = 'chweyspy'
    allowed_domains = ['chewy.com']
    start_urls = ['https://www.chewy.com/b/food-332']
    custom_settings = {"FEED_EXPORT_ENCODING" : "utf-8"}

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='ProductListingGrid_overlayWrapper__1QmQq']/div/div/div/a"), callback='parse_item', follow=True),
        # Rule(LinkExtractor(restrict_xpaths="//a[@aria-label='Next page']")),
    )

    def parse_item(self, response):
        li = DoogfoodspyItem() #NOTE: TO USE ITEAMLOADER
        name = response.xpath("normalize-space(//div[@id='product-title']/h1/text())").get()
        descp = response.xpath("normalize-space((//article[@id='descriptions']//p)[1])").get()
        price = response.xpath("normalize-space(//p[@class='price']/span[1]/text())").get()
        brand = response.xpath("normalize-space(//div[@id='product-subtitle']/a/span/text())").get()
        brand_url = response.xpath("//div[@id='product-subtitle']/a/@href").get()
        ingredients  = response.xpath("normalize-space(//article[@id='Nutritional-Info']//p[1])").get()
        key_benefits = response.xpath("(//article[@id='descriptions']//ul)[1]/li/text()").getall()
        imgs = response.xpath("//div[@id='media-selector']//img/@src").getall()

        attributes = {}
        for attrib in response.xpath("//ul[@class='attributes']/li"):
            attrib_name = attrib.xpath("normalize-space(.//div[1]/text())").get()
            if attrib.xpath("normalize-space(.//div[2]/text())").get():
                attrib_value = attrib.xpath("normalize-space(.//div[2]/text())").get()
            else:
                attrib_value = attrib.xpath("normalize-space(.//div[2]/span/text())").get()

            attributes[attrib_name] = attrib_value

        analysis = {}
        for data in response.xpath("(//table)[1]/tbody/tr"):
            data_name = data.xpath("normalize-space(.//td[1])").get()
            data_value = data.xpath("normalize-space(.//td[2])").get()
            analysis[data_name] = data_value

        
        # yield{
        #     "ProductName" : name,
        #     "Price" : price,
        #     "Description" : descp,
        #     "Attributes" : attributes,
        #     "Brand" : brand,
        #     "Brand_url": brand_url,
        #     "ingredients" : ingredients,
        #     "Key_Benefits" : key_benefits,
        #     "Guaranteed_Analysis" : analysis,
        #     "Images" : imgs
        # }

        li["ProductName"] = name
        li["Price"] = price
        li["Description"] = descp
        li["Attributes"] = attributes
        li["Brand"] = brand
        li["Brand_url"]= brand_url
        li["ingredients"] = ingredients
        li["Key_Benefits"] = key_benefits
        li["Guaranteed_Analysis"] = analysis
        li["Images"] = imgs
        yield li



