from db.run_sql import run_sql
from models.product import Product
from models.manufacturer import Manufacturer

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, country) VALUES (%s, %s) RETURNING id"
    values = [manufacturer.name, manufacturer.country]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id