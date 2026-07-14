try:
    number = int(input("Enter a number: "))
    result = 1000 / number
    print("Answer:", result)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")
