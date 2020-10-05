from flask import Flask, render_template, redirect, request, Blueprint

from controllers.product_controller import products_blueprint
from controllers.manufacturer_controller import manufacturers_blueprint


app = Flask(__name__)

app.register_blueprint(products_blueprint)
app.register_blueprint(manufacturers_blueprint)


@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()