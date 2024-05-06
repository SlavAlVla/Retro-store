from flask import Flask, render_template, request, url_for, redirect
import json
import random

# Автоматическое добавление пути картинки товара
# with open('data/assort.json', 'r', encoding='utf-8') as f :
#     assort = json.load(f)
# for category in assort:
#     for product in assort[category]['products']:
#         assort[category]['products'][product]['image_path'] = f'static/images/{category}/{product}.png'
# with open('data/assort.json', 'w', encoding='utf-8') as f :
#     json.dump(assort, f, ensure_ascii=False, indent=2)

app = Flask(__name__)

@app.route('/')
def index():
    with open('data/assort.json', 'r', encoding='utf-8') as f:
        assort = json.load(f)
        popular = []
        for i in range(6):
            rand_category = random.choice(list(assort.keys()))
            rand_product = random.choice(list(assort[rand_category]['products'].keys()))
            popular.append({'category': rand_category, 'product': assort[rand_category]['products'][rand_product], 'id': rand_product})
            assort[rand_category]['products'].pop(rand_product)
            if assort[rand_category]['products'] == {}:
                assort.pop(rand_category)
    return render_template('index.html', popular=popular)

@app.route('/shop')
def shop():
    with open('data/assort.json', 'r', encoding='utf-8') as f:
        assort = json.load(f)
    return render_template('shop.html', assort=assort)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products/<category>/<product>')
def product(category, product):
    with open('data/assort.json', encoding='utf-8') as f:
        try:
            assort = json.load(f)
            product = assort[category]['products'][product]
        except KeyError:
            product = {
                "image_path" : "static/images/not-found.jpg",
                "name" : "Товар не найден",
                "price": "₽0.00",
                "desc" : ""
            }
    return render_template('product.html',
        product = product
    )

if __name__ == "__main__":
    app.run()