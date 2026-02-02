#1 Crete Class & Objects

class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance  = balance

user1 = BankAccount(647011, "Manik", 20_000)
print(user1.account_number, user1.owner_name, user1.balance)        