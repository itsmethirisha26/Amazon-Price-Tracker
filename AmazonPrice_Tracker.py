import requests
import bs4
import pandas as pd
from datetime import datetime
import time
import schedule
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

product_list = {"B0744GC2CK":"L'Oreal Professionnel Absolut Repair Shampoo","B07NDXJGF8":"L'Oreal Professionnel Absolut Repair Mask","B07YSY6S6F":"Love Beauty & Planet Argan Oil","B093LMJFVH":"Minimalist Hair Growth Serum"}
base_url = 'https://www.amazon.in'
url = 'https://www.amazon.in/dp/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}
base_response = requests.get(base_url,headers=headers)
cookies = base_response.cookies

def track_prices():
    price_message = "Price updates as of " + str(datetime.now()) + ":\n\n"
    for product in product_list:
        response = requests.get(url+product, headers=headers, cookies=cookies)
        soup = bs4.BeautifulSoup(response.text , features ='lxml')
        prices = soup.findAll(class_ = "a-price-whole")

        final_price = str(prices[0])
        final_price = final_price.replace('<span class="a-price-whole">','')
        final_price = final_price.replace('<span class="a-price-decimal">.</span></span>','')
        #print(url+product,"-",product_list[product],":",final_price)
        price_message += product_list[product] + ": " + final_price + "\n"
    return price_message



def email_price(price):


    from_addr = "2k21ece112@kiot.ac.in"
    to_addrs = ["2k21ece112@kiot.ac.in"]
    subject = "Amazon Price Details"
  
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = ", ".join(to_addrs)
    msg['Subject'] = subject
    msg.attach(MIMEText(price, 'plain'))

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    password = "Thirisha@2607"  

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  
        server.login(from_addr, password)
        server.sendmail(from_addr,to_addrs,msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

def job():
    price_message = track_prices()
    print(price_message)
    email_price(price_message)

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)