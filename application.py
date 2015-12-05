from flask import Flask
from flask import render_template

from Product import Product


application = Flask(__name__)

@application.route('/')
@application.route('/<name>')
def hello_world(name=None):
    products = []
    products.append(Product("test", "http://myUrl", "http://myPicture", 5, 10))
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


if __name__ == '__main__':
    application.debug = True
    application.run()
