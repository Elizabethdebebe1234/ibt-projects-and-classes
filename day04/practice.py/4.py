class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self.__quantity = value

    def restock(self, n):
        self.quantity += n
        print(f"{n} {self.name}(s) added. Current quantity: {self.quantity}")

    def sell(self, n):
       if n > self.quantity:
        print("Not enough products in stock.")
       else:
        self.quantity -= n
        print(f"{n} {self.name}(s) sold. Current quantity: {self.quantity}")

# Create a product
product1 = Product("Laptop", 50000, 10)

print(product1.quantity)

product1.restock(5)
product1.sell(8)

# This will raise a ValueError
product1.sell(10)