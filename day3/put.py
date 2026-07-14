total = 0
try:
 with open("telebirr.txt") as f:
  for line in f:
   total += int(line.strip())

except FileNotFoundError:
 print("No transaction file found")
else:
 print(f"Total: {total} ETB")
 