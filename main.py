from flask import Flask, render_template, request, url_for, redirect
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products/<product>')
def product(product):
    with open('data/products.json', encoding='utf-8') as f:
        try:
            product_data = json.load(f)
            product_image_path = product_data[product]['image_path']
            product_name = product_data[product]['name']
            product_price = product_data[product]['price']
            product_desc = product_data[product]['desc']
        except KeyError:
            product_image_path = 'static/images/not-found.jpg'
            product_name = 'Товар не найден'
            product_price = '0.00₽'
            product_desc = ''
    return render_template('product.html',
        product_image_path = product_image_path,
        product_name = product_name,
        product_price = product_price,
        product_desc = product_desc,
    )

if __name__ == "__main__":
    app.run()