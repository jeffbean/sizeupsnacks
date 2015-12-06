import fileio
from decorators import static_vars


@static_vars(products=None)
def get_products():
    if not get_products.products:
        file_handler = fileio.FileIO()
        get_products.products = file_handler.read()
    return get_products.products


def save_products():
    fileio.FileIO().write(get_products.products)


if __name__ == '__main__':
    print(get_products())
    for key, value in get_products().items():
        print(value)
