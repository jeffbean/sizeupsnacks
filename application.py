from flask import Flask, jsonify
from flask import render_template
from flask import abort

from VoteStats import VoteStats
import os
from WeightedAverage import WeightedAverage

import product
import logging

FORMAT = '%(asctime)-15s [%(levelname)s] %(message)s'
DATE_FMT = '%m/%d/%Y %H:%M:%S'

loglevel = logging.DEBUG if os.environ.get('FLASK_DEBUG') else logging.INFO
logging.basicConfig(format=FORMAT, datefmt=DATE_FMT, level=loglevel)

application = Flask(__name__)
stats = VoteStats([0, 0, 0, 0, 0])


@application.route('/')
def hello_world(name=None):
    return render_template('snacks.html', name=name, products=product.get_products())


@application.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(product.get_products())


@application.route('/api/products/<product_id>', methods=['GET'])
def get_product(product_id):
    products = product.get_products()
    if product_id in products.keys():
        return jsonify(product.get_products()[product_id])
    abort(404)


@application.route('/api/products/<product_id>/rank/<rank>', methods=['POST'])
def update_product(product_id, rank):
    products = product.get_products()
    if product_id in products.keys():
        item = product.get_products()[product_id]
        new_rank = WeightedAverage(float(item['rating']), int(item['votes'])).add_value(int(rank))
        item['rating'] = new_rank.rank
        item['votes'] = new_rank.count
        return jsonify(item)
    abort(404)


if __name__ == '__main__':
    application.debug = True
    application.run()
