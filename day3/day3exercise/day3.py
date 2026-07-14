#Read transactions.txt line by line (name,amount per line).
try:
    with open("transactions.txt") as file:
        text = file.read()

#Wrap the file read in try / except for a missing file.
except FileNotFoundError:
    print("File not found!")

#Build a dict mapping each customer to their total spend.
spending = {}
with open("transactions.txt") as file:
    for line in file:
        name, amount = line.strip().split(",")
        amount = int(amount)

        if name in spending:
            spending[name] += amount
        else:
            spending[name] = amount

#Print each customer and total, sorted highest first.
for name, total in sorted(spending.items(), key=lambda x: x[1], reverse=True):
    print(name, total)