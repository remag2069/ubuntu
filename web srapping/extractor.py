from bs4 import BeautifulSoup
import requests as r

url='https://www.youtube.com/watch?v=VMtarj8Ua0s'

html=r.get(url)

soup=BeautifulSoup(html.content,'html.parser')

f=open('soup.txt','w')
f.write(soup.contents)