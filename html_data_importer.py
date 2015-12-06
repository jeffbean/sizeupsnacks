from abc import ABCMeta
from abc import abstractmethod
from lxml import html
from lxml import etree

import re
import fileio


class HtmlDataImporter(metaclass=ABCMeta):
    @abstractmethod
    def extract(self, static_html):
        pass


class CostcoDataImporter(HtmlDataImporter):
    def extract(self, static_html):
        tree = html.fromstring(static_html)
        new_products = {}
        for cartThumb in tree.xpath('//td[@class="cartItemThumbnail"]'):
            cartThumbTree = html.fromstring(etree.tostring(cartThumb))
            data = {}
            data['product_url'] = cartThumbTree.xpath("a/@href")[0]
            data['image_url'] = cartThumbTree.xpath("a/img/@src")[0]
            data['product_name'] = cartThumbTree.xpath("a/img/@alt")[0]
            data['votes'] = 0
            data['rating'] = 0
            key = re.search('(?<=\.)([0-9]*?)(?=\.)', data['product_url']).group(0)
            new_products[key] = data
        return new_products



if __name__ == '__main__':
    new_products = CostcoDataImporter().extract(fileio.read_file_as_string('shopping_cart.html'))
    fileio.FileIO().write(new_products)
