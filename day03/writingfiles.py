with open("customers.txt", "w") as f:
    f.write("Daily Report\n")
    f.write("Total: 1500 ETB\n")
# append instead of overwrite
with open("log.txt", "a") as f:
   f.write("New entry\n")