from flask import Flask
from flask import render_template

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
@application.route('/<name>')
def hello_world(name=None):
    return render_template('snacks.html', name=name, products=product.get_products())


@application.route('/test/vote/<key>/<vote>')
def vote_test(key, vote):
    found = product.get_products()[key]
    if found:
        rank = WeightedAverage(float(found['rating']), int(found['votes'])).add_value(int(vote))
        found['rating'] = rank.rank
        found['votes'] = rank.count
        return "<div>{0}</div>".format(rank.rank)
    # else: need to warn but not on the main page
    return "<div>{0}</div>".format("Cannot find product with ID " + key)


if __name__ == '__main__':
    application.debug = True
    application.run()
