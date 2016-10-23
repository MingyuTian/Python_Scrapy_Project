#!/usr/bin/python
# -*- coding:utf-8 -*-

# from scrapy.contrib.spiders import  CrawlSpider,Rule

from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from ok_corp.items import OkCorpItem
import re
import string

class OkCorpSpider(Spider):
    """ok_corpSpider"""

    name = "ok_corp"
  
    allowed_domains = ["www.sos.ok.gov/"]
    start_urls = []
    #numbers = [1900]
    numbers = [12, 1000, 1100, 1200, 1400, 1412, 1600, 1900, 1910, 1912, 2000, 2012, 2100, 2112, 2200, 2212, 2300, 2310, 2312, 2400, 2512, 2600, 2612, 2800, 2900, 2912, 3012, 3100, 3110, 3300, 3312, 3400, 3412, 3500, 3512, 3600, 3612, 3700, 3712, 3800, 3812, 4300, 4312, 4400, 4412, 4500, 4512, 4700, 4712, 4812]
    
    for x in range(1, 999999):
    #for x in range(1,9999):
        for y in numbers:
            z = 6 - len(str(x))
            urls = "https://www.sos.ok.gov/corp/corpInformation.aspx?id=" + str(y) + "0"*z + str(x)
            start_urls.append(urls)
    

    #urls = "https://www.sos.ok.gov/corp/corpInformation.aspx?id=1900540651"
    #start_urls.append(urls)
    def parse(self, response):
        sel = Selector(response)
        item = OkCorpItem()
        businessname = sel.xpath('//*[@id="printDiv"]/h3/text()').extract()
        if businessname <> []:
        	businessname = businessname[0].strip()
        if businessname <> '':    
        	name_type = sel.xpath('//*[@id="printDiv"]/dl[1]/dd[2]/text()').extract()
        	ubi = sel.xpath('//*[@id="printDiv"]/dl[1]/dd[1]/text()').extract()
        	status = sel.xpath('//*[@id="printDiv"]/dl[1]/dd[3]/text()').extract()
        	category = sel.xpath('//*[@id="printDiv"]/dl[1]/dd[4]/text()').extract()
        	addressRegion = sel.xpath('//*[@id="printDiv"]/dl[1]/dd[5]/text()').extract()
        	dateOfIncorporation = sel.xpath('//*[@id="printDiv"]/dl[1]/dd[6]/text()').extract()
        	registeredAgentName = sel.xpath('//*[@id="printDiv"]/dl[2]/dd[1]/text()').extract()
        	registeredAgentAddress = sel.xpath('//*[@id="printDiv"]/dl[2]/dd[3]/text()').extract()
        	csz = sel.xpath('//*[@id="printDiv"]/dl[2]/dd[4]/text()').extract()

        	item['businessName'] = businessname
        	item['url'] = str(response.url)
        	if name_type <> []:
        		item['name_type'] = name_type[0].strip()
        	if ubi <> []:
        		item['ubi'] = ubi[0].strip()
        	if status <> []:
        		item["status"] = status[0].strip()
        	if category <> []:
        		item['category'] = category[0].strip()
        	if addressRegion <> []:
        		item['addressRegion'] = addressRegion[0].strip()
        	if dateOfIncorporation <> []:
        		item['dateOfIncorporation'] = dateOfIncorporation[0].strip()
        	if registeredAgentName <> []:
        		item['registeredAgentName'] = registeredAgentName[0].strip()
        	if registeredAgentAddress <> []:
        		item['registeredAgentAddress'] = registeredAgentAddress[0].strip()
        	if csz <> []:
        		csz_split = csz[0].strip().split("\n")
        		if len(csz_split) == 3:
        			item['registeredAgentCity']  = csz_split[0].strip()
        			item['registeredAgentState'] = csz_split[1].strip()
        			item['registeredAgentZip'] = csz_split[2].strip()
        			item['registeredAgentAddressFormat'] = item['registeredAgentAddress'] + ",\n" + item['registeredAgentCity'] + ", " + item['registeredAgentState'] + " " + item['registeredAgentZip']

        		elif len(csz_split) == 4:
        			item['registeredAgentCity']  = csz_split[0].strip() + csz_split[1].strip()
        			item['registeredAgentState'] = csz_split[2].strip()
        			item['registeredAgentZip'] = csz_split[3].strip()
        			item['registeredAgentAddressFormat'] = item['registeredAgentAddress'] + ",\n" + item['registeredAgentCity'] + ", " + item['registeredAgentState'] + " " + item['registeredAgentZip']


        	return item
