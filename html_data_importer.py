from abc import ABCMeta
from abc import abstractmethod
from lxml import html
import fileio


class HtmlDataImporter(metaclass=ABCMeta):
    @abstractmethod
    def extract(self, static_html):
        pass


class CostcoDataImporter(HtmlDataImporter):
    def extract(self, static_html):
        tree = html.fromstring(static_html)
        print(tree)

        for cartThumb in tree.xpath('//td[@class="cartItemThumbnail"]'):
            print(html.fromstring(cartThumb.tostring()))
        # print(/a/@href'))
        # print(tree.xpath('//td[@class="cartItemThumbnail"]/a/img/@src'))
        # print(tree.xpath('//td[@class="cartItemThumbnail"]/a/img/@alt'))



if __name__ == '__main__':
    CostcoDataImporter().extract(fileio.read_file_as_string('shopping_cart.html'))
