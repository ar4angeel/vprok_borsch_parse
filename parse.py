from telegram.ext import defaults

from links import *
from peewee import *
from bs4 import BeautifulSoup
from datetime import datetime
from models import Product,Price
import requests

test_url = "https://online.globus.ru/products/govyazhya-sheya-bez-kosti-1-upakovka-0-7-0-9-kg/"
default = datetime.now

def get_price(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, features="html.parser")
    name = soup.find('div', class_='item-card__content--right')
    name = name.find('h1', class_='js-with-nbsp-after-digit').text
    name_text = name.lstrip().rstrip()
    price = soup.find('div', class_='d-col d-col_xs_6 item-card__top--right')
    price_rub = price.find('span', class_='item-price__rub').text
    price_kop = price.find('span', class_='item-price__kop').text
    list_prices = [price_rub, price_kop]
    price_out = '.'.join(list_prices)
    dict_in = {'name': name_text, 'price': price_out, 'url': url}
    return dict_in


def delete_mark(dict_in):
    arr = []
    for i in dict_in['name']:
        if i != '\xa0':
           arr.append(i)
    new_arr = ''.join(arr)
    dict_in['name'] = new_arr
    return dict_in


def get_amount(dict_in):
    amount = dict_in['name'].split(',')
    dict_in['name'] = amount[0]
    dict_in['amount'] = amount[1].lstrip()
    print(dict_in)
    return dict_in


for i in list_products:
    a = get_amount(delete_mark(get_price(i)))
    Product.get_or_create(url = a['url'], name = a['name'], amount = a['amount'], defaults = a)
    Price.get_or_create(product= a['name'],price= a['price'],timestamp= default, defaults = a)


