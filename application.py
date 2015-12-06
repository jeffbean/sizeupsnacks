from flask import Flask, jsonify
from flask import render_template
from flask import abort
from votestats import VoteStats
from weightedaverage import WeightedAverage
from collections import OrderedDict

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
application.logger.addHandler(logging.StreamHandler())
application.logger.setLevel(logging.INFO)
application.jinja_env.globals.update(min=min)


@application.route('/')
def home_page():
    products_dict = product.get_products()
    return render_template('snacks.html', products=(OrderedDict(sorted(products_dict.items(), key=lambda x: -x[1]['rating']))))


@application.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(product.get_products())


@application.route('/api/products/fix', methods=['GET'])
def fill_in_vote_stats():
    products = product.get_products()
    for item in products.values():
        ensure_vote_stats(item)
    return jsonify(products)


def ensure_vote_stats(item):
    if 'votes_by_star' not in item.keys():
        vote_stats = VoteStats(None, item['rating'], item['votes'])
        item['votes_by_star'] = vote_stats.votes_by_star
        item['rating'] = vote_stats.rank()


@application.route('/api/products/<product_id>', methods=['GET'])
def get_product(product_id):
    products = product.get_products()
    if product_id in products.keys():
        item = product.get_products()[product_id]
        ensure_vote_stats(item)
        return jsonify(item)
    abort(404)


@application.route('/api/products/<product_id>/rank/<rank>', methods=['POST'])
def update_product(product_id, rank):
    if not rank.isdigit():
        abort(401)
    elif int(rank) > 5 or int(rank) < 1:
        abort(400)
    products = product.get_products()
    if product_id in products.keys():
        item = product.get_products()[product_id]
        ensure_vote_stats(item)
        item['votes_by_star'][int(rank)-1] += 1
        new_rank = WeightedAverage(float(item['rating']), int(item['votes'])).add_value(int(rank))
        item['rating'] = new_rank.rank
        item['votes'] = new_rank.count
        return jsonify(item)
    abort(404)


if __name__ == '__main__':
    application.debug = True
    application.run()
