from datetime import datetime
from peewee import *

db = SqliteDatabase('D:/Питон/vprok_borsch_parse/vprok_borsh_kit.db')

class Product(Model):
    name = CharField()
    url = CharField(unique=True)
    amount = CharField()


    class Meta:
        database = db

class Price(Model):
    product = ForeignKeyField(Product,backref='prices')
    price = FloatField()
    timestamp = DateTimeField(default=datetime.now)

    class Meta:
        database = db


def create_table():
    with db:
        Product.create_table()
        Price.create_table()

create_table()
