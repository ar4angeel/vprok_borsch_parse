from flask import Flask, render_template
from models import (Product, db)
from parse_from_table import get_data_list

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('about.html')

@app.route('/catalog')
def catalog():
    return render_template('catalog.html', title='Catalog')

@app.before_request
def before_request():
    db.connect()

@app.route('/id/<id>')
def get_product_from_id(id):
    a = Product.get_by_id(int(id)).name
    c = Product.get_by_id(int(id)).url
    d = get_data_list(id)
    return render_template('forms.html', name=f'{a}', caption=f'{a}', data_list=d, url=c)

@app.after_request
def after_request(response):
    db.close()
    return response

if __name__ == '__main__':
    app.run(debug=True)