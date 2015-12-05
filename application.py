from flask import Flask
from flask import render_template

import test_product


application = Flask(__name__)

@application.route('/')
@application.route('/<name>')
def hello_world(name=None):
    return render_template('snacks.html', name=name, products=test_product.get_products())


if __name__ == '__main__':
    application.debug = True
    application.run()
