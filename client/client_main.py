from flask import Flask, url_for, render_template
from models import (Product, Price, db)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('about.html')

@app.route('/catalog')
def catalog():
    return render_template('forms.html', title='Catalog')

@app.before_request
def before_request():
    db.connect()

@app.route('/id/<id>')
def get_product_from_id(id):
    a = Product.get_by_id(id).name
    return a

@app.after_request
def after_request(response):
    db.close()
    return response

if __name__ == '__main__':
    app.run(debug=True)