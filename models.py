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
    price = CharField()
    timestamp = DateTimeField()

    class Meta:
        database = db


def create_table():
    with db:
        Product.create_table()
        Price.create_table()

create_table()