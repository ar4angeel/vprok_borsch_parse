from datetime import datetime

import requests
from bs4 import BeautifulSoup
from peewee import *
from telegram.ext import defaults

from links import *
from models import Price, Product

test_url = "https://online.globus.ru/products/govyazhya-sheya-bez-kosti-1-upakovka-0-7-0-9-kg/"
default = datetime.now

# get price - надо переминовать в get_product_item, потому что название функции должно отражать, что функция делает. ЭТО ВАЖНО. Ты через 10 дней сам не вспомнишь, что это за функция была.
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


# Здесь на вход лучше подавать строку, а не весь словарь, потому что операция производится только с одним полем
# ну и проще просто написать - name.replace('\xa0', '').strip()
# За изобретательность - 5, за знание библиотек - двойка (:
def delete_mark(dict_in):
    arr = []
    for i in dict_in['name']:
        if i != '\xa0':
           arr.append(i)
    new_arr = ''.join(arr)
    dict_in['name'] = new_arr
    return dict_in


# Вот это неплохо
def get_amount(dict_in):
    amount = dict_in['name'].split(',')
    dict_in['name'] = amount[0]
    dict_in['amount'] = amount[1].lstrip()
    print(dict_in)
    return dict_in


# Это надо переделать
# for i in list_products:
#     a = get_amount(delete_mark(get_price(i)))
#     Product.get_or_create(url = a['url'], name = a['name'], amount = a['amount'], defaults = a)
#     Price.get_or_create(product= a['name'],price= a['price'],timestamp= default, defaults = a)

# я перепишу за тебя, а ты разберись, что и почему
for product_url in list_products:
    # вот этот вызов конечно все равно не особо хороший получился, но согласись - понятнее, что происходит, когда ты читаешь get_price(product_url)
    product_item = get_amount(delete_mark(get_price(product_url)))
    # не знаю, насколько peewee понравятся такие дефолты, потому что там есть лишие поля, если будет ломаться в этом месте - поправишь
    # подчеркивание - это значок неиспользуемой переменной, в этом месте еще возвращается булеан, создан ли новый объект в базе(или мы взяли имеющийся)
    product, _ = Product.get_or_create(url=product_item['url'], defaults=product_item)
    
    Price.create(product=product, price=product_item['price'])

