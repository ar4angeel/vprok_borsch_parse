from models import *
from peewee import *
from models import (Product, Price)
from links import list_products

def get_id_name(id):
    a = Product.get_by_id(id)
    return a




