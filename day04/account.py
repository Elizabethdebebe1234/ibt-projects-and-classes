class Account:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self.__balance = balance
    @property
    def balance(self):
        return self.__balance
    def deposit(self, amount):
        if amount <= 0:
          raise ValueError("Must be positive")
        self.__balance += amount
    def withdraw(self, amount):
        if amount <= 0:
          raise ValueError("Must be positive")
        if amount > self.__balance:
          raise ValueError("Insufficient balance")
        self.__balance -= amount
    def statement(self):
       print("----- Addis Bank Statement -----")
       print(f"Owner: {self.owner}")
       print(f"Account Number: {self.account_number}")
       print(f"Balance: {self.__balance} ETB")

acc = Account( "Almaz", "CBE-1001", 1500)
acc.deposit(500)
acc.withdraw(300)
acc.statement()
print(acc.statement)
