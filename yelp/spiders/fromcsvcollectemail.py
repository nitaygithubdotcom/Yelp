# -*- coding: utf-8 -*-
import scrapy
import re
from csv import reader, writer

class CollectemailSpider(scrapy.Spider):
    name = 'fromcsvcollectemail'

    # start_urls = ['http://naanstopgrill.ca/']
    start_urls = ['http://www.damascuscalgary.com/']
    # start_urls = ['https://www.shawarma-palace.com/']
    # start_urls = ['https://www.theguildrestaurant.com/']
    # start_urls = ['https://cravingsmarketrestaurant.com/']
    # start_urls = ['https://www.brazilianbbq.ca/']

    def parse(self, response):
        read = open('X:/DataScrap/contact_url3.csv','r')
        websites = reader(read)
        alldata = list(websites)
        print(alldata)
        for i in alldata:
            print(i)



    def parsedata(self, response):
        try:
            emails = re.findall("[a-z0-9._-]+@[a-z0-9_-]+[.]+[a-z]+", str(response.body))
            print(emails)
            if emails != []:
                uniquemail = set(emails)
                emailid = " | ".join(uniquemail)
            else:
                contact = response.xpath('//a[contains(@href,"contact")]/@href').get()
                contactlink = response.urljoin(contact)
                print('nextlink>>',contactlink)
                yield scrapy.Request(contactlink, callback=self.parsedata)
                # emailid = 'N/A'
        except:
            pass

        yield {'Email':emailid}
