#1 Crete Class & Objects

# class BankAccount:
#     def __init__(self, account_number, owner_name, balance):
#         self.account_number = account_number
#         self.owner_name = owner_name
#         self.balance  = balance
        
#     def deposit(self, add_balance):
#         self.balance = add_balance+self.balance
    
#     def withdraw(self, withdral_amount):    
#          self.balance = self.balance -withdral_amount
    
#     def check_balance(self):     
#         print(self.balance)

# user1 = BankAccount(647011, "Manik", 20_000)
# user1 = BankAccount(647011, "Manik", 20_000)
# user1.check_balance()    



#2 Class & Objects

class Book:
    def __init__(self, title, author, review):
        self.title = title
        self.author = author
        self.review = review
        
    def add_review(self, new_review):
        self.review.append(new_review)
    
    def count_review(self):
        print(len(self.review))
        
    def show_review(self):
        print(self.review)    
        
book1 = Book("The Secret", "Rhonda Byrne", ["It Was superb", "Page Turner", "Really Secret inside"])            


book1.show_review()
