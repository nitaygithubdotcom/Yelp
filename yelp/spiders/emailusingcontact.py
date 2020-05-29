# -*- coding: utf-8 -*-
import scrapy
import re


class CollectemailSpider(scrapy.Spider):
    name = 'emailusingcontact'
    start_urls = ['http://www.shawarmaknight.com/']

    def parse(self, response):
        try:
            emails = re.findall("[a-z0-9.]+@[a-z0-9]+[.]+[a-z]+", str(response.body))
            print('Email>>',emails)
            if emails != []:
                uniquemail = set(emails)
                emailid = " | ".join(uniquemail)
            # elif nextlink = response.urljoin('contact-us'):
            #     yield scrapy.Request(nextlink, callback=self.parse)
            else:
                nextlink = response.urljoin('contact-us')
                print('nextlink>>',nextlink)
                yield scrapy.Request(nextlink, callback=self.parse)
                # emailid = 'N/A' 
        except:
            pass

        yield {'Email':emailid}
