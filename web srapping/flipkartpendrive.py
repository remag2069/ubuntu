import csv
import requests as r
from bs4 import BeautifulSoup
html=r.get("https://www.flipkart.com/search?q=pendrive&sid=6bo%2Cjdy%2Cuar&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_2&otracker1=AS_QueryStore_OrganicAutoSuggest_0_2&as-pos=0&as-type=RECENT&as-backfill=on")
soup=BeautifulSoup(html.content,'html.parser')
#print(soup.contents)
#contents=soup.find_all("div",{"class":"sg-col-inner"})
contents=soup.find_all("div",{"class":"_3liAhj _1R0K0g"})
#print(len(contents))
#print(contents[0])
#v=contents[3].a
#v=contents[3].a

#print(contents[3].a.div.div.div.img["alt"])
f=open("D:\\python projects\\web srapping\\data\\pendriveflipkart.csv","w")
header="product name,sales price,off\n"
f.write(header)


for i in contents:
    brand=(i.a.div.div.div.img["alt"])
    sales_price=(i.find("div",{"class":"_1vC4OE"}).text[1:])
    if(i.find("div",{"class":"_3auQ3N"})==None):
        off="0"
    else:
        off=(i.find("div",{"class":"_3auQ3N"})).text[1:]
    s=brand.replace(",","|") + "," + sales_price.replace(",","") + "," + off.replace(",","") + "\n"
    print(s)
    f.write(s)



for j in range(2,41):
    html=r.get("https://www.flipkart.com/search?q=pendrive&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(j))
    soup=BeautifulSoup(html.content,'html.parser')
    #print(soup.contents)
    #contents=soup.find_all("div",{"class":"sg-col-inner"})
    contents=soup.find_all("div",{"class":"_3liAhj _1R0K0g"})
    #print(len(contents))
    #print(contents[0])
    #v=contents[3].a
    #v=contents[3].a

    #print(contents[3].a.div.div.div.img["alt"])
    #f=open("D:\\python projects\\web srapping\\data\\pendriveflipkart.csv","w")
    #header="product name,sales price,off\n"
    #f.write(header)


    for i in contents:
        brand=(i.a.div.div.div.img["alt"])
        sales_price=(i.find("div",{"class":"_1vC4OE"}).text[1:])
        if(i.find("div",{"class":"_3auQ3N"})==None):
            off="0"
        else:
            off=(i.find("div",{"class":"_3auQ3N"})).text[1:]
        s=brand.replace(",","|") + "," + sales_price.replace(",","") + "," + off.replace(",","") + "\n"
        print(s)
        f.write(s)
f.close()