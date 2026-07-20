class Account:
   def __init__(self, owner, balance=0):
       self.owner = owner
       self.balance = balance
   def deposit(self, amount):
       self.balance += amount

class SavingsAccount(Account):
   def __init__(self, owner, number,
       balance=0, rate=0.05):
       super().__init__(owner, number, balance)
       self.rate = rate
   def add_interest(self):
       interest = self.balance * self.rate
       self.deposit(interest) # reuse parent method

s = SavingsAccount("Almaz", 1500, 0.1)
s.deposit(500)
print(s.balance) # 2000

