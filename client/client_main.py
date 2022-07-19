from flask import Flask, url_for, render_template
from models import (Product, Price, db)
from links import *
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
    b = Price.get_by_id(int(id)).price
    return render_template('forms.html', name=f'{a}',price=f'{b}',ref=f'{c}')

@app.after_request
def after_request(response):
    db.close()
    return response

if __name__ == '__main__':
    app.run(debug=True)