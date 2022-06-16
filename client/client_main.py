from flask import Flask, url_for, render_template
from models import (Product, Price, db)
app = Flask(__name__)

@app.before_request
def before_request():
    db.connect()

@app.after_request
def after_request(response):
    db.close()
    return response

@app.route('/id/<id>')
def get_product_from_id(id):
    a = Product.get_by_id(id).name
    return a

if __name__ == '__main__':
    app.run(debug=True)
