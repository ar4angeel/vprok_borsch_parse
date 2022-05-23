from flask import Flask, url_for, render_template
from models import (Product, Price)
app = Flask(__name__)

@app.route('/<id>')
def get_product_from_id(id):
    a = Product.get_by_id(int(id)).name
    return '<h1>%s</h1>' % a

if __name__ == '__main__':
    app.run(debug=True)
