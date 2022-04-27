from peewee import *
main_kit = SqliteDatabase('vprok_borsh_main_kit.db')
second_kit = SqliteDatabase('vprok_borsch_second_kit.db')

class Product(Model):
    ID = AutoField()
    NAME = TextField()
    URL = BareField()
    AMOUNT = AutoField()

    class Meta:
        database = main_kit

class Price(Model):
    ID = AutoField()
    PRODUCT_ID = Product.ID
    PRICE = FloatField()
    TIMESTAMP = BareField

    class Meta:
        database = second_kit


