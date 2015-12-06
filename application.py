from flask import Flask, jsonify
from flask import render_template
from flask import abort
from votestats import VoteStats
from weightedaverage import WeightedAverage
import os
import product
import logging
import threading

FORMAT = '%(asctime)-15s [%(levelname)s] %(message)s'
DATE_FMT = '%m/%d/%Y %H:%M:%S'

loglevel = logging.DEBUG if os.environ.get('FLASK_DEBUG') else logging.INFO
logging.basicConfig(format=FORMAT, datefmt=DATE_FMT, level=loglevel)

t = threading.Timer(60 * 5, product.save_products)
t.start()  # after 5 minutes products will be saved
application = Flask(__name__)
application.jinja_env.globals.update(min=min)


@application.route('/')
def hello_world(name=None):
    return render_template('snacks.html', name=name, products=product.get_products())


@application.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(product.get_products())


@application.route('/api/products/fix', methods=['GET'])
def fill_in_vote_stats():
    products = product.get_products()
    for item in products.values():
        if 'votes_by_star' not in item.keys():
            vote_stats = VoteStats(None, item['rating'], item['votes'])
            item['votes_by_star'] = vote_stats.votes_by_star
            item['rating'] = vote_stats.rank()
    return jsonify(products)


@application.route('/api/products/<product_id>', methods=['GET'])
def get_product(product_id):
    products = product.get_products()
    if product_id in products.keys():
        item = product.get_products()[product_id]
        if 'votes_by_star' not in item.keys():
            vote_stats = VoteStats(None, item['rating'], item['votes'])
            item['votes_by_star'] = vote_stats.votes_by_star
        return jsonify(item)
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
