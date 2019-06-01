import scrapy
import pickle
from scrapy.crawler import CrawlerProcess
import os
import sys
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
os.mkdir(str(sys.argv[2]))

class FlipkartwebscraperItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    
class laptopsSpider(scrapy.Spider):
    name = 'laptops'
    count = int(sys.argv[1])
    page_number = 2
    all_laptops = {}
    allowed_domains = ['www.flipkart.com']
    start_urls = ['https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1']

    def parse(self, response):
        if len(laptopsSpider.all_laptops)==0:
            laptop = FlipkartwebscraperItem()
            name = response.css('div._3wU53n::text').getall()
            price = response.css('div._1vC4OE._2rQ-NK::text').getall()
            rating = response.css('div.hGSR34::text').getall()
            laptop['name'] = name
            laptop['price'] = price
            laptop['rating'] = rating
            print (laptop)
            laptopsSpider.all_laptops.update(laptop)
        elif len(laptopsSpider.all_laptops.get('name'))<=laptopsSpider.count:
            laptop = FlipkartwebscraperItem()
            name = response.css('div._3wU53n::text').getall()
            price = response.css('div._1vC4OE._2rQ-NK::text').getall()
            rating = response.css('div.hGSR34::text').getall()
            laptop['name'] = name
            laptop['price'] = price
            laptop['rating'] = rating
            print (laptop)
            laptopsSpider.all_laptops.get('name').extend(laptop.get('name'))
            laptopsSpider.all_laptops.get('price').extend(laptop.get('price'))
            laptopsSpider.all_laptops.get('rating').extend(laptop.get('rating'))
        else:
            for i in range(len(laptopsSpider.all_laptops.get('name'))-laptopsSpider.count):
                laptopsSpider.all_laptops.get('name').pop()
                laptopsSpider.all_laptops.get('price').pop()
                laptopsSpider.all_laptops.get('rating').pop()

        next_page = ('https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page='+str(laptopsSpider.page_number))
        if laptopsSpider.page_number <= 18:
            laptopsSpider.page_number +=1
            yield response.follow(next_page, callback = self.parse, dont_filter=True)
        pickle_out = open(BASE_DIR+'/'+str(sys.argv[2])+'/laptops.txt', 'wb')
        pickle.dump(laptopsSpider.all_laptops, pickle_out)
        pickle_out.close()

initiate = CrawlerProcess()
initiate.crawl(laptopsSpider)
initiate.start()

pickle_in = open(BASE_DIR+'/'+str(sys.argv[2])+'/laptops.txt', 'rb')
laptop_pickled_data = pickle.load(pickle_in)
print (laptop_pickled_data)
print (len(laptop_pickled_data.get('name')))



##css for price - div._1vC4OE._2rQ-NK
##css for name - div._3wU53n
##css for rating - div.hGSR34
##css for next button - a._3fVaIS
##css for entire block of one laptop - div._1UoZlX

