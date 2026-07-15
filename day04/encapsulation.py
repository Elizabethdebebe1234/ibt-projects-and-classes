class Account:
    def __init__(self, owner, balance=0):
      self.owner = owner # public
      self.__balance = balance # private
    @property
    def balance(self):
     return self.__balance
    def deposit(self, amount):
       if amount <= 0:
         raise ValueError("Must be positive")
       self.__balance += amount


a = Account("Almaz", 1500)
a.deposit(500)
a.balance # 2000
a.deposit(10) # ValueError
a.balance = -5 # AttributeError