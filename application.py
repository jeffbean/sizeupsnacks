from flask import Flask
from flask import render_template

from Product import Product
from VoteStats import VoteStats


application = Flask(__name__)
stats = VoteStats([0, 0, 0, 0, 0])


@application.route('/')
@application.route('/<name>')
def hello_world(name=None):
    products = []
    products.append(Product("test", "http://myUrl", "https://images.costco-static.com/image/media/80-810983-847__1.jpg", 5, 10))
    products.append(Product("test2", "http://myUrl", "http://myPicture", 4, 10))
    products.append(Product("test3", "http://myUrl", "http://myPicture", 3, 10))
    products.append(Product("test4", "http://myUrl", "http://myPicture", 2, 10))
    products.append(Product("test5", "http://myUrl", "http://myPicture", 1, 10))
    products.append(Product("test6", "http://myUrl", "http://myPicture", 0, 0))
    products.append(Product("test7", "http://myUrl", "http://myPicture", .5, 10))
    products.append(Product("test8", "http://myUrl", "http://myPicture", 1.5, 10))
    products.append(Product("test9", "http://myUrl", "http://myPicture", 2.5, 10))
    products.append(Product("test10", "http://myUrl", "http://myPicture", 3.5, 10))
    products.append(Product("test11", "http://myUrl", "http://myPicture", 4.5, 10))
    return render_template('snacks.html', name=name, products=products)


@application.route('/test/vote/<vote>')
def vote_test(vote):
    stats.vote(int(vote))
    return "<div>{0}</div>".format(stats)


if __name__ == '__main__':
    application.debug = True
    application.run()