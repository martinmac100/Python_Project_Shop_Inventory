import pdb
from db.run_sql import run_sql
from models.product import Product
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

def save(product):
    sql = "INSERT INTO products (model, description, colour, buy_price, sell_price, quantity, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s,%s) RETURNING *"
    values = [product.model, product.description, product.colour, product.buy_price, product.sell_price, product.quantity, product.manufacturer_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product



def select_all():
    products =  []
    sql = "SELECT * FROM products ORDER BY manufacturer_id"
    results = run_sql(sql)
    for result in results:
        manufacturer = manufacturer_repository.select(result['manufacturer_id'])
        product = Product(result["model"], result["description"], result["colour"], result["buy_price"], result["sell_price"], result["quantity"], manufacturer, result["id"])
        products.append(product)
    return products

def select(id):
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    manufacturer = manufacturer_repository.select(result['manufacturer_id'])
    product = Product(result["model"], result["description"], result["colour"], result["buy_price"], result["sell_price"], result["quantity"], manufacturer, result["id"])
    return product


def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# UPDATE FIRST THING
def update(product):
    sql = "UPDATE products SET (model, description, colour, buy_price, sell_price, quantity, manufacturer_id) = (%s, %s, %s, %s, %s, %s,%s) WHERE id = %s"
    values = [product.model, product.description, product.colour, product.buy_price, product.sell_price, product.quantity, product.manufacturer_id, product.id]
    run_sql(sql, values)
