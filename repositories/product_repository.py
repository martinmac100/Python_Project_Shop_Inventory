from db.run_sql import run_sql
from models.product import Product
from models.manufacturer import Manufacturer

def save(product):
    sql = "INSERT INTO products (model, description, colour, buy_price, sell_price) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [product.model, product.description, product.colour, product.buy_price, product.sell_price]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id