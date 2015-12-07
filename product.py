import fileio
from decorators import static_vars


@static_vars(products=None)
def get_products():
    if not get_products.products:
        file_handler = fileio.FileIO()
        get_products.products = file_handler.read()
    return get_products.products


def save_products():
    fileio.FileIO().write(get_products())
    return get_products()


@static_vars(apps=None)
def get_apps():
    if not get_apps.apps:
        file_handler = fileio.FileIO()
        get_apps.apps = file_handler.read_apps()
    return get_apps.apps


def save_apps():
    fileio.FileIO().write_apps(get_apps())


if __name__ == '__main__':
    print(get_products())
    for key, value in get_products().items():
        print(value)
