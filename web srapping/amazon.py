import requests
from bs4 import BeautifulSoup
import smtplib
def check():
    URL="https://www.amazon.in/HP-FD236W-32GB-Drive-Gray/dp/B01L8ZL3X8/ref=sr_1_2?crid=23F36AX22U8A9&keywords=pendrive+32gb&qid=1562409284&refinements=p_89%3AHP&rnid=3837712031&s=gateway&sprefix=pend%2Caps%2C328&sr=8-2"

    headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

    page=requests.get(URL,headers=headers)

    s=BeautifulSoup(page.content,'html.parser')


    price=(s.find(id="priceblock_ourprice").get_text()).strip()

    p=''
    for i in range(1,6):
        p+=price[i]
        #print(p)
    #print(float(p))
    price=float(p)

    if price<200.0:
        send_mail(price)
def send_mail(price):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('remag2069@gmail.com','rlgvidqpktobqfgk')

    subject='price<200'
    body='https://www.amazon.in/HP-FD236W-32GB-Drive-Gray/dp/B01L8ZL3X8/ref=sr_1_2?crid=23F36AX22U8A9&keywords=pendrive+32gb&qid=1562409284&refinements=p_89%3AHP&rnid=3837712031&s=gateway&sprefix=pend%2Caps%2C328&sr=8-2'

    msg=f"subject:{subject}\n\n {body}"
    server.sendmail('remag2069@gmail.com','dharshan2609@gmail.com',msg)
    print('price fell and email sent')
    server.quit()

check()




