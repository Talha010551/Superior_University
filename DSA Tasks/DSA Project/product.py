class Product:
    def __init__(self, product_id, name, price, rating, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.rating = rating
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} | ₹{self.price} | Rating: {self.rating}/5 | In stock: {self.quantity}"