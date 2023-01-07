from models import Product


def get_data_list(id):
    data_list = []
    a = Product.get_by_id(id)
    for p in a.prices:
        dict_of_data = {'datetime': str(p.timestamp), 'price': p.price}
        data_list.append(dict_of_data)
    data_list.reverse()
    return data_list