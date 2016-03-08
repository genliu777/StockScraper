import urllib.request
import re
import csv

"""
Handles pulling company data from a source for the stock scraper to use
"""

def getList(mode):
    if (mode=='csv'):
        data = csv.reader(open('companylist.csv', 'r'), delimiter=",", quotechar='|')
        symbols, names = [], []
        for row in data:
            symbols.append(row[0].lower().strip())
            #names.append(row[1])

    if (mode=='xls'):
        # be able to read in excel spreadsheets eventually
        pass

    return(symbols)

def main():
    print('start')
    symbolList = getList('csv')
    print(symbolList)

if __name__ == "__main__":
    main()
