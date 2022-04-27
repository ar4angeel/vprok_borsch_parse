from peewee import *
db = SqliteDatabase('vprok_borsh_kit.db')

class Product(Model):
    name = CharField()
    url = CharField()
    amount = FloatField()

    class Meta:
        database = db

class Price(Model):
    product_id = Product.ID
    price = FloatField()
    timestamp = DateTimeField()

    class Meta:
        database = db


