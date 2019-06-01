#import all classes here
import scrapy
import pickle
from scrapy.crawler import CrawlerProcess
import os
import sys
#base directory to refer later
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

#sys.argv[2] is the pickle directory entered in the command line,
#so that we can make a new directory named that
os.mkdir(str(sys.argv[2]))

#item class
class FlipkartwebscraperItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()

#spiderclass  
class laptopsSpider(scrapy.Spider):
    name = 'laptops'
    #this is the number of laptops to be scraped entered in the command line
    count = int(sys.argv[1])
    page_number = 2
    all_laptops = {}
    allowed_domains = ['www.flipkart.com']
    start_urls = ['https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1']

    def parse(self, response):
        #we use conditionals here for different use cases
        #this one is when we initially scrape the first page
        #during that time there is nothing in the all_laptops dict
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
        #this is for all other pages
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
        #this is when we exceed the count given and have to remove the extra laptops
        else:
            for i in range(len(laptopsSpider.all_laptops.get('name'))-laptopsSpider.count):
                laptopsSpider.all_laptops.get('name').pop()
                laptopsSpider.all_laptops.get('price').pop()
                laptopsSpider.all_laptops.get('rating').pop()

        #here we define link for the next page
        next_page = ('https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page='+str(laptopsSpider.page_number))
        #the reason we have 18 here is because flipkart has some weird issue due to which one 
        #cannot scrape after page 18
        if laptopsSpider.page_number <= 18:
            laptopsSpider.page_number +=1
            yield response.follow(next_page, callback = self.parse, dont_filter=True)
        #here we save all the laptop data from the dictionary to pickle file
        pickle_out = open(BASE_DIR+'/'+str(sys.argv[2])+'/laptops.txt', 'wb')
        pickle.dump(laptopsSpider.all_laptops, pickle_out)
        pickle_out.close()

#this is to initiate the crawler
initiate = CrawlerProcess()
initiate.crawl(laptopsSpider)
initiate.start()

#this is to read the pickled data from txt file
pickle_in = open(BASE_DIR+'/'+str(sys.argv[2])+'/laptops.txt', 'rb')
laptop_pickled_data = pickle.load(pickle_in)
#prints the entire dictionary with name,price,rating of laptops
print (laptop_pickled_data)
#we print the number of laptops scraped as mentioned in the command line (just to verify)
print (len(laptop_pickled_data.get('name')))



##css for price - div._1vC4OE._2rQ-NK
##css for name - div._3wU53n
##css for rating - div.hGSR34
##css for next button - a._3fVaIS
##css for entire block of one laptop - div._1UoZlX

