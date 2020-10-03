from db.run_sql import run_sql
from models.product import Product
from models.manufacturer import Manufacturer

def save(product):
    sql = "INSERT INTO products (model, description, colour, buy_price, sell_price) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [product.model, product.description, product.colour, product.buy_price, product.sell_price]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id

def select_all():
    products =  []
    sql = "SELECT * FROM products"
    results = run_sql(sql)
    for result in results:
        product = Product(result["model"], result["description"], result["colour"], result["buy_price"], result["sell_price"], result["id"])
    return products

