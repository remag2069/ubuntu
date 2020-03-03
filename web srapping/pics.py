import urllib
from urllib import request
from bs4 import BeautifulSoup


url='https://www.flipkart.com/search?q=pendrive&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1'
rdata=request.urlopen(url)
soup=BeautifulSoup(rdata,'html.parser')