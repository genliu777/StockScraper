import urllib.request
import re
from GetCompanyData import getList
from threading import Thread

# Simple Yahoo Finance Web Scraper that retrieves current stock value for a company.
# Regex currently only works for NASDAQ stocks
# Linear implementation with 1 request made at a time, so cannot handle too many requests

#symbolList = ["aapl", "goog", "nflx", "amzn"]
symbolList = getList('csv')[1:]
valueList = []
valueDict = {}
activeThreads = []
def th(symbol):
    regStockValue= '<span id=\"yfs_l84_' + symbol + '\">'
    url = "http://finance.yahoo.com/q?s=" + symbol
    htmlfile = urllib.request.urlopen(url)
    htmltext = str(htmlfile.read()) 
    price = re.split(regStockValue, htmltext)[1].split("</span>")[0]
    print(price)

for s in symbolList:
    request = Thread(target=th,args=(s,))
    request.start()
    activeThreads.append(request)

for b in activeThreads:
    b.join()
