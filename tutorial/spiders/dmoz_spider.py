import scrapy
from scrapy.utils.response import open_in_browser
from tutorial.items import DmozItem
import logging

class DmozSpider(scrapy.Spider):
    name = "google"
    allowed_domains = ["play.google.com"]
    start_urls = [
        "https://play.google.com/store/apps/collection/topselling_paid?hl=en",
    ]

    def parse(self, response):
        #open_in_browser(response)
        for href in response.css("div.details > a::attr('href')"):
            if href:
                #url = response.urljoin(href.extract())
                url = response.url[0:23] + href.extract()
                logging.warning(' item received for %s', url)
                yield scrapy.Request(url, callback=self.parse_dir_contents)
            else:
                logging.warning('No item received for ', href)

    def parse_dir_contents(self, response):
        logging.warning('reponse.url before splitting %s', response.url)
        str1 = response.url.split("=")[-1]
        filename = 'output/'+str1+ '.html'
        logging.warning('No item received for %s', filename)
        with open(filename, 'wb') as f:
            f.write(response.body)
