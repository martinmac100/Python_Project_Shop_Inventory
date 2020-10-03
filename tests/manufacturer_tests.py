import unittest
from models.manufacturer import Manufacturer

class TestManufacturer(unittest.TestCase):
    def setUp(self):
        self.manufacturer = Manufacturer("Apple", "USA")
    
    def test_manufacturer_has_name(self):
        self.assertEqual("Apple", self.manufacturer.name)

    def test_manufacturer_has_country(self):
        self.assertEqual("USA", self.manufacturer.country)