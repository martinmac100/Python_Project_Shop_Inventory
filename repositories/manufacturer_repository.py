from db.run_sql import run_sql
from models.product import Product
from models.manufacturer import Manufacturer

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, country) VALUES (%s, %s) RETURNING *"
    values = [manufacturer.name, manufacturer.country]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id
    return manufacturer

def select_all():
    manufacturers =  []
    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)
    for result in results:
        manufacturer = Manufacturer(result["name"], result["country"], result["id"])
        manufacturers.append(manufacturer)
    return manufacturers

def select(id):
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    manufacturer = Manufacturer(result["name"], result["country"], result["id"])
    return manufacturer


def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(manufacturer):
    sql = "UPDATE manufacturers SET (name, country) = (%s, %s) WHERE id = %s"
    values = [manufacturer.name, manufacturer.country, manufacturer.id]
    run_sql(sql, values)