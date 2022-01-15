import scrapy

class ChweyspySpider(scrapy.Spider):
    name = 'chweyspy'
    allowed_domains = ['chewy.com']
    start_urls = ['https://www.chewy.com/b/food-332']

    def parse(self, response):
        cato_list = response.xpath('//div[@class="js-tracked-facet"]/div/a[position() mod 2 = 1]/text()').getall()
        cato_urls = [f'https://www.chewy.com{i}' for i in response.xpath('//div[@class="js-tracked-facet"]/div/a[position() mod 2 = 1]/@href').getall()]
        cato_products = response.xpath('//div[@class="js-tracked-facet"]/div/a/text()[position() mod 2 = 0]').getall()
        print("-------------------------")

        for i in range(len(cato_list)):
            yield{
                "Category" : cato_list[i],
                "Total Products" : cato_products[i],
                "Category Url" : cato_urls[i]
            }
        print("-------------------------")
