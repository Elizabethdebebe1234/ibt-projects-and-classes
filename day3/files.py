# the with statement auto-closes
with open("customers.txt") as f:
   for line in f:
      print(line.strip())
# read everything at once
with open("customers.txt") as f:
   text = f.read()
