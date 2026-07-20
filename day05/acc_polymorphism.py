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

class SavingsAccount(Account):
   def __init__(self, owner, number, balance, rate):
      self.rate=rate
     
      super().__init__(owner, number, balance)
   def add_interest(self):
       interest = self.balance * self.rate
       self.deposit(interest)

class currentAccount(Account):
    def __init__ (self, owner, number, balance, overdraft_limit):
        self.overdraft_limit = overdraft_limit
        super().__init__(owner, number, balance)# parent
    def withdraw(self, amount):
        if amount <= 0:
          raise ValueError("Must be positive")
        if amount > self.balance + self.overdraft_limit:
          raise ValueError("Insufficient balance")
        self._Account__balance -= amount

bank = [
  SavingsAccount("Almaz", "CBE-1", 1500),
  CurrentAccount("Dawit", "CBE-2", 800),
  ]
for acc in bank:
  acc.deposit(100) # shared behaviour
  acc.statement() # each its own way




