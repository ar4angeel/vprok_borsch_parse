# импорт, который надо добавить
# from datetime import datetime

from peewee import *

db = SqliteDatabase('vprok_borsh_kit.db')

class Product(Model):
    name = CharField()
    url = CharField(unique=True)
    amount = CharField()


    class Meta:
        database = db

class Price(Model):
    product = ForeignKeyField(Product,backref='prices')
    # кстати тут было бы неплохо исправить на price = FloatField()
    price = CharField()
    timestamp = DateTimeField()
    # Полe c дефолтным значением, соответственно дальше мы можем про него забыть, всякий раз когда новая цена будет добавляться в базу, автоматом будет вставляться время этого события
    # timestamp = DateTimeField(default=datetime.now)

    class Meta:
        database = db


def create_table():
    with db:
        Product.create_table()
        Price.create_table()

create_table()
