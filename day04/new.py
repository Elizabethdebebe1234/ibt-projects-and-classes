class Account:
    def __init__(self, owner, balance):
      self.owner = owner
      self.balance = balance
    def deposit(self, amount):
      self.balance += amount
    def withdraw(self, amount):
      self.balance -= amount
    def statement(self):
      print(f"{self.owner}: {self.balance} ETB")

almaz = Account("Almaz", 1500)
almaz.deposit(500)
almaz.statement()
almaz.withdraw(200)
almaz.statement()