import unittest
from models.product import Product
from models.manufacturer import Manufacturer
import repositories.product_repository as product_repository

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product("Iphone SE", "5.5 inches", "Rose Gold", 299, 399, 50, "Apple")
        self.manufacturer = Manufacturer("Apple", "USA")
    
    def test_product_has_description(self):
        self.assertEqual("5.5 inches", self.product.description)

    def test_product_has_colour(self):
        self.assertEqual("Rose Gold", self.product.colour)

    def test_product_has_buy_price(self):
        self.assertEqual(299, self.product.buy_price)

    def test_product_has_sell_price(self):
        self.assertEqual(399, self.product.sell_price)

