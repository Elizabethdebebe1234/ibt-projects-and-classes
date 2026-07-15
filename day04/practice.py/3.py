class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity   # Private attribute

    @property
    def quantity(self):
        return self.__quantity

    def restock(self, n):
        self.__quantity += n
        print(f"{n} {self.name}(s) added. Current quantity: {self.__quantity}")

    def sell(self, n):
        if n > self.__quantity:
            print("Not enough products in stock.")
        else:
            self.__quantity -= n
            print(f"{n} {self.name}(s) sold. Current quantity: {self.__quantity}")


# Create a product
product1 = Product("Laptop", 50000, 10)

# Check quantity
print("Current quantity:", product1.quantity)

# Restock
product1.restock(5)

# Sell
product1.sell(8)

# Check quantity again
print("Final quantity:", product1.quantity)