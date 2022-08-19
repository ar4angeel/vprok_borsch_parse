from models import Price, Product
import peewee

def get_data_list():
    a = Price.select(Price.timestamp, Price.price).where(Product.product_id='1')
    for data in a:
        print(data.timestamp)

get_data_list()
