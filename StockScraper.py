import urllib.request
import re

"""
Simple Yahoo Finance Web Scraper that retrieves current stock value for a company.
Regex currently only works for NASDAQ stocks
Linear implementation with 1 request made at a time, so cannot handle too many requests
"""

# Added comments below for Matt 
# This particular branch is obselete. Current version is multithreaded

# List of symbols for companies we want to scrape. In the updated version,
# the symbolList is populated from parsing an excel spreadsheet 
symbolList = ["aapl", "goog", "nflx", "amzn"]

# Declaration for value dictionary. Will eventually be populated in the format:
# {Key = Stock Symbol, Value = Stock Value}
valueDict = {}
i = 0
while(i < len(symbolList)):
    # The html string right before where the price is listed
    regStockValue= '<span id=\"yfs_l84_' + symbolList[i] + '\">'
    
    # Builds the url based on current 
    url = "http://finance.yahoo.com/q?s=" + symbolList[i] 

    # These two lines handle making a request to the url and retrieving page's HTML 
    htmlfile = urllib.request.urlopen(url)
    htmltext = str(htmlfile.read())

    # We are splitting on the pattern we declared above 
    # Since the price is AFTER the pattern, we grab the [1] element of the split 
    price = re.split(regStockValue, htmltext)[1]

    # After the split, we want to get rid of everything extra 
    # This command essentially gets rid of the </span> and everything after it  
    stockVal = price.split("</span>")[0]

    # Add the entry and its value to the dictionary we declared earlier 
    valueDict[symbolList[i]] = stockVal

    i += 1

""" 
Print for debugging. Run in IDLE if you want the command prompy to stay up.
Otherwise, the program will run and the print statement will only pop up
for a fraction of a second. 
"""
print(valueDict)
