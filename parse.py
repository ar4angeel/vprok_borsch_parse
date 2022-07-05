from datetime import datetime

import requests
from bs4 import BeautifulSoup
from peewee import *
from telegram.ext import defaults

from links import *
from models import Price, Product

test_url = "https://online.globus.ru/products/govyazhya-sheya-bez-kosti-1-upakovka-0-7-0-9-kg/"
default = datetime.now


def get_product_item(url):
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
    dict_in['name'].replace('\xa0','').strip()
    return dict_in


def get_amount(dict_in):
    amount = dict_in['name'].split(',')
    dict_in['name'] = amount[0]
    dict_in['amount'] = amount[1].lstrip()
    print(dict_in)
    return dict_in



for product_url in list_products:
    # вот этот вызов конечно все равно не особо хороший получился, но согласись - понятнее, что происходит, когда ты читаешь get_price(product_url)
    product_item = get_amount(delete_mark(get_product_item(product_url)))
    # не знаю, насколько peewee понравятся такие дефолты, потому что там есть лишие поля, если будет ломаться в этом месте - поправишь
    # подчеркивание - это значок неиспользуемой переменной, в этом месте еще возвращается булеан, создан ли новый объект в базе(или мы взяли имеющийся)
    Product, _ = Product.get_or_create(url=product_item['url'], defaults=product_item)
    Price.create(product= Product, price=product_item['price'])

