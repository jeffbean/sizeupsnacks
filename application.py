from flask import Flask
from flask import render_template

from VoteStats import VoteStats
import product


application = Flask(__name__)
stats = VoteStats([0, 0, 0, 0, 0])


@application.route('/')
def hello_world(name=None):
    return render_template('snacks.html', name=name, products=product.get_products())


# @application.route('/test/vote/<vote>')
# def vote_test(vote):
#     stats.vote(int(vote))
#     return "<div>{0}</div>".format(stats)


@application.route('/vote/<key>')
def vote_test(key, rating=None):
    # stats.vote(int(vote))
    product.get_products()[key]['rating'] = newRating
    product.get_products()[key]['votes'] += 1
    return "<div>{0}</div>".format(stats)


if __name__ == '__main__':
    application.debug = True
    application.run()
