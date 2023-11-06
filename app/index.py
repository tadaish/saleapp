from flask import Flask, render_template, request
import data
from app import app

app = Flask(__name__)


@app.route("/")
def index():
    kw = request.args.get('kw')
    cates = data.get_categories()
    prods = data.get_products(kw)

    return render_template('index.html', categories = cates, products = prods)


if __name__ == '__main__':
    app.run(debug=True)