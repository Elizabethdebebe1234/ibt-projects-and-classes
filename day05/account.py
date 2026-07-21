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
        print("Account Type: Regular Account")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance} ETB")
        print()


class SavingsAccount(Account):
    def __init__(self, owner, number, balance, rate):
        super().__init__(owner, number, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)

    def statement(self):
        print("----- Addis Bank Statement -----")
        print("Account Type: Savings Account")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance} ETB")
        print(f"Interest Rate: {self.rate * 100}%")
        print()


class CurrentAccount(Account):
    def __init__(self, owner, number, balance, overdraft_limit):
        super().__init__(owner, number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Must be positive")

        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Insufficient balance")

        self._Account__balance -= amount

    def statement(self):
        print("----- Addis Bank Statement -----")
        print("Account Type: Current Account")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance} ETB")
        print(f"Overdraft Limit: {self.overdraft_limit} ETB")
        print()


# Mixed list of accounts
bank = [
    SavingsAccount("Almaz", "CBE-1001", 1500, 0.05),
    CurrentAccount("Dawit", "CBE-1002", 800, 500)
]

# Perform some operations
bank[0].deposit(500)
bank[0].add_interest()

bank[1].deposit(200)
bank[1].withdraw(1200)

# Polymorphic loop
for acc in bank:
    acc.statement()