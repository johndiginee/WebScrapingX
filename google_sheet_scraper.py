import requests
from bs4 import BeautifulSoup
import gspread
from datetime import datetime

def request():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}
    url = 'https://www.konga.com/product/apple-16-inch-macbook-pro-apple-m2-max-chip-with-12core-cpu-and-38core-gpu-1tb-ssd-space-grey-6303476'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def parse(soup):
    now = datetime.now()
    date = now.strftime("%m/%d/%Y")
    name = soup.find('h4').text.strip()
    product_code = soup.find('div', class_ = '_97fc0_3W515 b50e0_1HOLM').text.strip().replace('Product Code: ', '')
    brand = soup.find('div', class_ = '_71bb8_13C6j').text.strip().replace('Brand: ', '')
    price = soup.find('div', class_ = '_678e4_e6nqh').text.strip().replace('₦', '')
    quantity = soup.find('div', class_ = 'a03ba_1Zj-T').text.strip()
    product = {'date': date, 'name': name, 'product_code': product_code, 'brand': brand, 'price': price, 'quantity': quantity}
    return product

def output(product):
    # Connect Google credentials
    google_credentials = gspread.service_account(filename='credentials.json')
    # Connect Google Sheet
    google_sheet = google_credentials.open('webscrapingx').sheet1
    # Add data to Google Sheet Row
    google_sheet.append_row([str(product['date']), str(product['name']), str(product['product_code']), str(product['brand']), str(product['price']), str(product['quantity'])])
    return

data = request()
product = parse(data)
output(product)