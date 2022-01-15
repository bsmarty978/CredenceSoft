import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WetFoodSpy(CrawlSpider):
    name = 'chweyspy'
    allowed_domains = ['chewy.com']
    start_urls = ['https://www.chewy.com/b/wet-food-293']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[@aria-label='Next page']"), callback='parse_item', follow=True),

    )

    def parse_item(self, response):
        
        #NOTE:Total Page Number
        total_page = response.xpath('//ul[@class="kib-pagination-new__list"]/li[last()]/a/text()').get()
        print(f'?>>>>>>>>>>>>>Total page{total_page}')
        
        item = response.xpath("//div[@class='ProductListingGrid_overlayWrapper__1QmQq']/div//div/h2//strong/text()").getall()
        item_urls = response.xpath("//div[@class='ProductListingGrid_overlayWrapper__1QmQq']/div/div/div/a/@href").getall()
        
        for i in range(len(item_urls)):
            yield {
                "ProductName" : item[i],
                "ProductUrl" : item_urls[i]
            }



