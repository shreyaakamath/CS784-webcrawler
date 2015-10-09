import scrapy
from scrapy.utils.response import open_in_browser
from tutorial.items import DmozItem
import logging
import os

class DmozSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.com"]
    start_urls = [
        "http://www.amazon.com/s/ref=lp_2650363011_nr_p_n_feature_four_bro_1?fst=as%3Aoff&rh=n%3A2625373011%2Cp_n_theme_browse-bin%3A2650363011%2Cp_n_feature_four_browse-bin%3A2650442011&bbn=2650363011&ie=UTF8&qid=1444429468&rnid=2650439011",
    ]

    def parse(self, response):
        #open_in_browser(response)
        for href in response.css("div.a-row.a-spacing-small > a::attr('href')"):
            if href:
                #url = response.urljoin(href.extract())
                url =  href.extract()
                logging.warning(' item received for %s', url)
                yield scrapy.Request(url, callback=self.parse_dir_contents)
            else:
                logging.warning('No item received for ', href)
        

    def parse_dir_contents(self, response):
        logging.warning('reponse.url before splitting %s', response.url)
        str1 = response.url.split("/")[3]
        #str1 = str1.split("?")[0]
        filename = 'output/'+str1+ '.html'
        #os.path.exists(str1+'.html')
        logging.warning('No item received for %s', filename)
        with open(filename, 'wb') as f:
            f.write(response.body)


