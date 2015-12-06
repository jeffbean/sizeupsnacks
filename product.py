import fileio
from decorators import static_vars


__data_filename = 'data.json'


@static_vars(products=None)
def get_products():
    if not get_products.products:
        get_products.products = fileio.read_json(__data_filename)
    return get_products.products


def save_products():
    fileio.write_json(__data_filename, get_products.products)


if __name__ == '__main__':
    print(get_products())
    for key, value in get_products().items():
        print(value)
