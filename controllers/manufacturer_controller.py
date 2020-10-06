from flask import Blueprint, Flask, redirect, render_template, request

from models.product import Product
import repositories.product_repository as product_repository
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)


@manufacturers_blueprint.route("/manufacturers")
def manufacturer():
    manufacturers = manufacturer_repository.select_all()
    return render_template("/manufacturers/index.html", manufacturers=manufacturers)

@manufacturers_blueprint.route("/manufacturers/new")
def new_manufacturer():
    manufacturers = manufacturer_repository.select_all()
    return render_template("/manufacturers/new.html", manufacturers = manufacturers)


@manufacturers_blueprint.route("/manufacturers", methods=["POST"])
def create_manufacturer():
    name = request.form["name"]
    country = request.form["country"]
    new_manufacturer = Manufacturer(name, country)
    manufacturer_repository.save(new_manufacturer)
    return redirect("/manufacturers")


@manufacturers_blueprint.route("/manufacturers/<id>/edit")
def edit_product(id):
    manufacturers = manufacturer_repository.select(id)
    products = product_repository.select_all()
    return render_template("manufacturers/edit.html", products=products, manufacturers=manufacturers)

@manufacturers_blueprint.route("/manufacturers/edit", methods=['POST'])
def update_manufacturer():
    name = request.form["name"]
    country = request.form["country"]
    new_manufacturer = Manufacturer(name, country)
    manufacturer_repository.update(manufacturer)
    return redirect("/manufacturers")


@manufacturers_blueprint.route("/manufacturers/<id>/delete", methods=["POST"])
def delete_manufacturers(id):
    manufacturer_repository.delete(id)
    return redirect("/manufacturers")