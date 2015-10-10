import scrapy
from scrapy.utils.response import open_in_browser
from tutorial.items import DmozItem
import logging
import os
import scrapy
from scrapy.utils.response import open_in_browser
from tutorial.items import DmozItem
import logging
import os
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.spider import Spider
from scrapy import Request

class DmozSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.com"]
    start_urls = [
        "http://www.amazon.com/s/ref=sr_pg_1?fst=as%3Aoff&rh=n%3A2625373011%2Cp_n_theme_browse-bin%3A2650363011%2Cp_n_feature_four_browse-bin%3A2650442011&bbn=2650363011&ie=UTF8&qid=1444512697",
    ]

    '''var1  = "http://www.amazon.com/s?bbn=2650363011&ie=UTF8&page="
    var2  = "&rh=n%3A2625373011%2Cp_n_theme_browse-bin%3A2650363011%2Cp_n_feature_four_browse-bin%3A2650442011"
    for i in range(2,3):
        var3 = var1 + `i` + var2
        print(var3)
        start_urls.append(var3)'''


    def parse(self, response):
        for href in response.css("div.a-row.a-spacing-small > a::attr('href')"):
            if href:
                url =  href.extract()
                yield scrapy.Request(url, callback=self.parse_dir_contents)
            else:
                logging.warning('No item received for ', href)

    def parse_dir_contents(self, response):
        str1 = response.url.split("/")[3]
        filename = 'output/'+str1+ '.html'
        '''hxs = HtmlXPathSelector(response)
        director_list = hxs.xpath('//*[@id="dv-center-features"]/div[1]/div/table/tbody')'''
        #director = director_list.extract()
        print(director_list[0])
        with open(filename, 'wb') as f:
            f.write(response.body)


