from flask import Blueprint, Flask, redirect, render_template, request

from models.product import Product
import repositories.product_repository as product_repository
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

products_blueprint = Blueprint("products", __name__)

# INDEX
@products_blueprint.route("/products")
def product():
    products = product_repository.select_all()
    return render_template("products/index.html", products=products)


# NEW
@products_blueprint.route("/products/new")
def new_products():
    manufacturers = manufacturer_repository.select_all()
    return render_template("products/new.html", manufacturers = manufacturers)


# CREATE
@products_blueprint.route("/products", methods=["POST"])
def create_product():
    model = request.form["model"]
    description = request.form["description"]
    colour = request.form["colour"]
    buy_price = request.form["buy_price"]
    sell_price = request.form["sell_price"]
    quantity = request.form["quantity"]
    manufacturer = request.form["manufacturer"]
    new_product = Product(model, description, colour, buy_price, sell_price, quantity, manufacturer)
    product_repository.save(new_product)
    return redirect("/products")


@products_blueprint.route("/products/<id>/edit")
def edit_product(id):
    product = product_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template("products/edit.html", product=product, manufacturers=manufacturers)

@products_blueprint.route("/products/edit", methods=['POST'])
def update_product():
    model = request.form["model"]
    description = request.form["description"]
    colour = request.form["colour"]
    buy_price = request.form["buy_price"]
    sell_price = request.form["sell_price"]
    quantity = request.form["quantity"]
    manufacturer = request.form["manufacturer"]
    update_product = Product(model, description, colour, buy_price, sell_price, quantity, manufacturer)
    product_repository.update(product)
    return redirect("/products")


# DELETE
@products_blueprint.route("/products/<id>/delete", methods=["POST"])
def delete_products(id):
    product_repository.delete(id)
    return redirect("/products")