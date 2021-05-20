from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
import json

from utils import collections

app=Flask(__name__)
Bootstrap(app)

raw = open("data/products.json")
products = json.load(raw)

@app.route('/<type>/products')
def search_by_product(type):
    pass

@app.route('/')
def index():
    product_types = collections.unique_keys(products, "type")

    return render_template(
        "index.html", 
        products=products,
        types=product_types)

