stock = {}

# Read the file
try:
    with open("stock.txt") as f:
        for line in f:
            item, qty = line.strip().split(",")
            stock[item] = int(qty)

except FileNotFoundError:
    print("No stock file found.")

# Function to increase or decrease quantity
def adjust(item, amount):
    stock[item] = stock.get(item, 0) + amount

# Example: Add 5 Paracetamol
adjust("Paracetamol", 5)

# Example: Remove 2 Vitamin C
adjust("Vitamin C", -2)

# Print low stock items
print("Low stock items:")
for item, qty in stock.items():
    if qty < 10:
        print(item, qty)

# Save updated stock back to the file
with open("stock.txt", "w") as f:
    for item, qty in stock.items():
        f.write(f"{item},{qty}\n")