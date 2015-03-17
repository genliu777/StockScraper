import urllib.request
import re


# Simple Yahoo Finance Web Scraper that retrieves current stock value for a company.
# Regex currently only works for NASDAQ stocks
# Linear implementation with 1 request made at a time, so cannot handle too many requests

symbolList = ["aapl", "goog", "nflx", "amzn"]
symbolList =  
valueDict = {}
i = 0
while(i < len(symbolList)):
    regStockValue= '<span id=\"yfs_l84_' + symbolList[i] + '\">'
    #print(regStockValue)
    url = "http://finance.yahoo.com/q?s=" + symbolList[i] 
    htmlfile = urllib.request.urlopen(url)
    htmltext = str(htmlfile.read())
    price = re.split(regStockValue, htmltext)[1]
    stockVal = price.split("</span>")[0]
    #valueDict[symbolList[i]] = stockVal

    i += 1

print(valueDict)
