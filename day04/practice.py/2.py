class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

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

# Restock
product1.restock(5)

# Sell
product1.sell(8)

# Try selling more than available
product1.sell(10)