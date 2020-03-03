import webbrowser
import tkinter as tk
from tkinter import *

window=Tk()
window.state("zoomed")
#window.configure(background='green')
ent1=Entry(window)
window.title("my own search engine")
#window.wm_iconbitmap("D:\python projects\searcheingine\searchengine1.jpg")

im=PhotoImage(file='D:\\python projects\\searcheingine\\searchengine1.png')
#cv=tk.Canvas(im.width,im.height)
#cv.create_image(0,0,image=im,anchor='nw')
#cv.pack(side=TOP)
def google():
    s=ent1.get()
    webbrowser.open("https://www.google.com/search?rlz=1C1CHBF_enIN854IN854&ei=c7QkXevFH4GS9QOJz5_oAQ&q="+s.replace(' ','+')+"&oq="+s.replace(' ','+')+"&gs_l=psy-ab.3.0.0i71l8.0.0..9442...0.0..0.0.0.......0......gws-wiz.emd5wkM7emw")

def yahoo():
    s=ent1.get()
    webbrowser.open("https://in.search.yahoo.com/search?p="+s.replace(' ','+')+"&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8")

def bing():
    s=ent1.get()
    webbrowser.open("https://www.bing.com/search?q="+s.replace(' ','+')+"&qs=n&form=QBLH&sp=-1&pq="+s.replace(' ','+')+"&sc=8-9&sk=&cvid=1F8837CB00734285BC7A7990316E1D3C")

l1=Label(window,text='type the search term')

b1=Button(window,text='search on google',command=google)
b2=Button(window,text='search on yahoo',command=yahoo)
b3=Button(window,text='search on bing',command=bing)

l1.pack()
ent1.pack(fill=X)
b1.pack()
b2.pack()
b3.pack()

Tk.mainloop(window)