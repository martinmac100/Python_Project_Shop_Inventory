class Product:
    def __init__(self, model, description, colour, buy_price, sell_price, quantity, manufacturer_id, id=None):
        self.model = model
        self.description = description
        self.colour = colour
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.quantity = quantity
        self.manufacturer_id = manufacturer_id
        self.id = id