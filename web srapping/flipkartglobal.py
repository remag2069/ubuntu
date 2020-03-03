import webbrowser as w
import csv
import requests as r
from bs4 import BeautifulSoup
from tkinter import *

def search():
    s=ent1.get()
    w.open("https://www.flipkart.com/search?q="+s+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off")





def save():
    s=ent1.get()
    html=r.get("https://www.flipkart.com/search?q="+s+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off")
    soup=BeautifulSoup(html.content,'html.parser')
    #print(soup.contents)
    #contents=soup.find_all("div",{"class":"sg-col-inner"})
    contents=soup.find_all("div",{"class":"_3liAhj _1R0K0g"})
    #print(len(contents))
    #print(contents[0])
    #v=contents[3].a
    #v=contents[3].a

    #print(contents[3].a.div.div.div.img["alt"])
    f=open("D:\\python projects\\web srapping\\data\\flipkartglobal.csv","w")
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
        print(i)
        f.write(s)


    '''
    for j in range(2,41):
        html=r.get("https://www.flipkart.com/search?q="+s+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page="+str(j))
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
            print(i)
            f.write(s)
    '''
    f.close()


window=Tk()
l1=Label(window,text='the item u want to search for on flipkart')
ent1=Entry(window)
b1=Button(window,text='search',command=search)
b2=Button(window,text='save data',command=save)
l1.pack()
ent1.pack(fill=X)
b1.pack()
b2.pack()

Tk.mainloop(window)