import scrapy

class FoodDataSpy(scrapy.Spider):
    name = 'foodspy'
    allowed_domains = ['chewy.com']
    start_urls = ['https://www.chewy.com/pedigree-adult-complete-nutrition/dp/141438']
    custom_settings = {"FEED_EXPORT_ENCODING" : "utf-8"}

    def parse(self, response):
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

        yield{
            "ProductName" : name,
            "Price" : price,
            "Description" : descp,
            "Attributes" : attributes,
            "Brand" : brand,
            "Brand_url": brand_url,
            "ingredients" : ingredients,
            "Key Benefits" : key_benefits,
            "Guaranteed Analysis" : analysis,
            "Images" : imgs

        }