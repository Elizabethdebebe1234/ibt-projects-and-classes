try:
  f = open("log.txt")
except FileNotFoundError:
  print("File is missing")
else:
  print("Opened OK") # no error
finally:
   print("Done") # always runs