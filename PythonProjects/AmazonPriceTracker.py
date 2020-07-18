import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = input("Enter the amazon link of the product ")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    cost = float("".join(x for x in ((price[2:]).split(","))))
    print(cost)
    if float(cost) < breakprice:
        send_email()


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(email, password)
    subject = 'Price fell down!'
    body = f'Check the amazon link {URL}'

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        email,
        'vidhi11@somaiya.edu',
        msg
    )

    print('HEY EMAIL IS SENT')
    server.quit()


email = input("Enter you email id").strip()
password = input("Enter your password")
breakprice = int(input("Enter the break point price"))



while True:
    check_price()
    time.sleep(60*60)
