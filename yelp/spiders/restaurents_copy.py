# -*- coding: utf-8 -*-
import scrapy
from csv import reader, writer
import re
from .checkhttp import httpcheck

class RestaurentsSpider(scrapy.Spider):
    name = 'restaurents_copy'
    start_urls = [
        'https://www.yelp.com/biz/saigon-maxim-calgary-2?osq=Restaurants',
        'https://www.yelp.com/biz/briggs-kitchen-bar-calgary?osq=Restaurants'
    ]

    # def parse(self,response):
    #     links = response.xpath('(//ul[@class="lemon--ul__373c0__1_cxs undefined list__373c0__2G8oH"])[1]//span[@class="lemon--span__373c0__3997G text__373c0__2Kxyz text-color--black-regular__373c0__2vGEn text-align--left__373c0__2XGa- text-weight--bold__373c0__1elNz text-size--inherit__373c0__2fB3p"]/a/@href').getall()
    #     for link in links:
    #         nextlink = response.urljoin(link)
    #         yield scrapy.Request(nextlink, callback=self.parsedata)

       

    def parse(self, response):
        comname = response.xpath('//div[@class="lemon--div__373c0__1mboc margin-t3__373c0__1l90z margin-b6__373c0__2Azj6 border-color--default__373c0__3-ifU"]//h1/text()').get()
        web = response.xpath('//div[@class="lemon--div__373c0__1mboc stickySidebar__373c0__3PY1o border-color--default__373c0__3-ifU"]//p/a[@target="_blank"]/text()').get()
        website = ''
        if web != None:
            x = web.split('/')
            website += httpcheck(x[0])
        ph = response.xpath('(//div[@class="lemon--div__373c0__1mboc stickySidebar__373c0__3PY1o border-color--default__373c0__3-ifU"]//p[@class="lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa-"])/text()').get()
        url = response.request.url

        yield {
            "Company_Name":comname,
            "Website":website,
            "Phone_Number":ph,
            "Yelp_Listing":url,
        }
    
        