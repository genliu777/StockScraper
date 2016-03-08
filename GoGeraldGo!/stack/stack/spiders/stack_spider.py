from scrapy import Spider
from scrapy.selector import Selector
from stack.items import StackItem

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class StackSpider(CrawlSpider):
  name = 'stack'
  allowed_domains = ['cplfoundation.org']
  start_urls = ['http://www.cplfoundation.org/site/PageServer']

  rules = [
      #Rule(LinkExtractor(allow=r'/dispensaries/'), callback='parse_hours')
  ]

  def parse_hours(self, response):
    print response.url

"""
class StackSpider(Spider):
  name = "stack"
  allowed_domains = ["cplfoundation.org"]
  start_urls = ["http://www.cplfoundation.org/site/PageServer",]

  def parse(self, response):
    print("The URL is " + response.url)
    titles = Selector(response).xpath('//title')
    for title in titles:
      print("AHHHHH" + str(title))
"""
