import pdb

from models.product import Product
import repositories.product_repository as product_repository

from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

manufacturer_repository.delete_all()
product_repository.delete_all()

manufacturer_1 = Manufacturer("Apple", "USA")
manufacturer_repository.save(manufacturer_1)

manufacturer_2 = Manufacturer("Samsung", "South Korea")
manufacturer_repository.save(manufacturer_2)

manufacturer_3 = Manufacturer("Google", "USA")
manufacturer_repository.save(manufacturer_3)

product_1 = Product("iPhone 11", "6.1 inches", "Black", 679.00, 779.00, 60, manufacturer_1.id)
product_repository.save(product_1)

product_2 = Product("iPhone X", "6.1 inches", "Space Grey", 379.00, 479.00, 70, manufacturer_1.id)
product_repository.save(product_2)

product_3 = Product("Galaxy S20", "6.2 inches", "Cloud Navy", 550.00, 799.00, 100, manufacturer_2.id)
product_repository.save(product_3)

product_4 = Product("Galaxy S10", "6.1 inches", "Ceramic Black", 450.00, 600.00, 30, manufacturer_2.id)
product_repository.save(product_4)

product_5 = Product("Pixel 5", "6.0 inches", "Sorta Sage", 499.00, 599.00, 20, manufacturer_3.id)
product_repository.save(product_5)

product_6 = Product("Pixel 4", "6.2 inches", "Just Black", 299.00, 349.00, 40, manufacturer_3.id)
product_repository.save(product_6)

pdb.set_trace()