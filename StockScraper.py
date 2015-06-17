import urllib.request
import re
import os.path
from threading import Thread
from GetCompanyData import getList
from DataOut import StockValuesOut

"""
Multithreaded Stock Scraper
"""

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
    #print(price)
    valueDict[symbol] = price

symbolList.sort()

# Currently limiting it to 100 requests to prevent Yahoo from yelling at us
for s in symbolList[0:100]:
    request = Thread(target=th,args=(s,))
    request.start()
    activeThreads.append(request)

for thread in activeThreads:
    thread.join()

# Make sure we are only passing the first 100 elements of symbolList in since we only
# populated the valueDict with those entries. 
StockValuesOut("Results/SampleOut.txt", valueDict, symbolList[0:100])
