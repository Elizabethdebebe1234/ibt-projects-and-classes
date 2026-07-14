prices = {"Bread": 50, "Milk": 80,
"Eggs": 120} # ETB
for item, price in prices.items():
    print(f"{item}: {price} ETB")
# Bread: 150 ETB
# Milk: 180 ETB
# Eggs: 20 ETB
print("prices.items() returns a list of tuples, each containing a key-value pair from the dictionary.")