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
        products.append(product)
    return products

def select(id):
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    product = Product(result["model"], result["description"], result["colour"], result["buy_price"], result["sell_price"], result["id"])
    return product


def delete_all():
    sql = "DELETE FROM product"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM product WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(product):
    sql = "UPDATE products SET model = %s WHERE id = %s"
    values = [product.model, product.id]
    run_sql(sql, values)
