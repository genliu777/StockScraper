import urllib.request
import urllib.parse

from bs4 import BeautifulSoup

url = 'http://www.cplfoundation.org/'
urls = [url] 
visited = [url] 
htmltext = urllib.request.urlopen(urls[0]).read()

# While stack of urls is greater than 0, keep scraping for links
while len(urls) > 0:
  try:
    with urllib.request.urlopen(urls[0]) as url:
      htmltext = url.read()
  except:
    print(urls[0])  

# Get and Print Information
  soup = BeautifulSoup(htmltext)
  urls.pop(0) 
  info = soup.findAll("title")
  #print(info)
  for tag in soup.findAll('a',href=True): 
    tag['href'] = urllib.parse.urljoin(str(url),str(tag['href']))
    print(tag['href'])
    if url in tag['href'] and tag['href'] not in visited:
      urls.append(tag['href'])
      visited.append(tag['href'])

