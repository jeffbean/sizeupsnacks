import fileio
from decorators import static_vars


@static_vars(products=None)
def get_products():
    if not get_products.products:
        get_products.products = fileio.FileIO.read()
        get_products.cached = True
    return get_products.products


def save_products():
    fileio.FileIO.write(get_products.products)


if __name__ == '__main__':
    print(get_products())
    for key, value in get_products().items():
        print(value)
