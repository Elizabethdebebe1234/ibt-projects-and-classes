price = [100, 250, 400, 80]

new_price= [p + (p*0.15) for p in price]

new_price.sort()

print(new_price)