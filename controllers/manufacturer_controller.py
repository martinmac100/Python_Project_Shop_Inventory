from flask import Blueprint, Flask, redirect, render_template, request

from models.product import Product
import repositories.product_repository as product_repository
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

# INDEX
@manufacturers_blueprint.route("/manufacturers")
def manufacturer():
    manufacturers = manufacturer_repository.select_all()
    return render_template("/manufacturers/index.html", manufacturers=manufacturers)

# NEW
@manufacturers_blueprint.route("/manufacturers/new")
def new_manufacturer():
    manufacturers = manufacturer_repository.select_all()
    return render_template("/manufacturers/new.html", manufacturers = manufacturers)


# CREATE
# @manufacturers_blueprint.route("/products", methods=["POST"])
# def create_product():
#     model = request.form["model"]
#     description = request.form["description"]
#     colour = request.form["colour"]
#     buy_price = request.form["buy_price"]
#     sell_price = request.form["sell_price"]
#     quantity = request.form["quantity"]
#     manufacturer = request.form["manufacturer"]
#     new_product = Product(model, description, colour, buy_price, sell_price, quantity, manufacturer)
#     product_repository.save(new_product)
#     return redirect("/products")


# @manufacturers_blueprint.route("/products/<id>/edit")
# def edit_product(id):
#     product = product_repository.select(id)
#     manufacturers = manufacturer_repository.select_all()
#     return render_template("products/edit.html", product=product, manufacturers=manufacturers)

# @manufacturers_blueprint.route("/products/edit", methods=['POST'])
# def update_product():
#     model = request.form["model"]
#     description = request.form["description"]
#     colour = request.form["colour"]
#     buy_price = request.form["buy_price"]
#     sell_price = request.form["sell_price"]
#     quantity = request.form["quantity"]
#     manufacturer = request.form["manufacturer"]
#     product = Product(model, description, colour, buy_price, sell_price, quantity, manufacturer)
#     product_repository.update(product)
#     return redirect("/products")


# DELETE
# @manufacturers_blueprint.route("/products/<id>/delete", methods=["POST"])
# def delete_products(id):
#     product_repository.delete(id)
#     return redirect("/products")