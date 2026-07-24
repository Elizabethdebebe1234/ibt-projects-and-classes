from bank import Account


class AccountRegistry:
    def __init__(self):
        # Dictionary for O(1) lookup
        self.by_number = {}

        # List to preserve insertion order
        self.order = []

    def add(self, acc):
        self.by_number[acc.account_number] = acc
        self.order.append(acc.account_number)

    def find(self, number):
        return self.by_number.get(number)

    def list_all(self):
        accounts = []

        for number in self.order:
            accounts.append(self.by_number[number])

        return accounts