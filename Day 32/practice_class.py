#practice Question 1

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
        
        
#     def description(self):
#         return f"{self.title} by {self.author}, {self.pages} pages"
            
# b1 = Book("Atomic Habits", "James Clear", 300)            
# b2 = Book("Zero to One", "Peter Thiel", 200)            

# print(f"The book {b1.title} by {b1.author} has {b1.pages} pages.")
# print(f"The book {b2.title} by {b2.author} has {b2.pages} pages.")


#practice Question 2

# class BankAccount:
#     def __init__(self, owner, ):
#         self.balance = 0
#         self.owner = owner
    
#     def show_balance(self):
#         print(f"Your balance is ${self.balance}")            
        
#     def deposit(self, amount):
#         self.balance += amount
#         return f"Amount ${amount} deposited successfully" 
       
#     def withdraw(self, amount):
#         print(f"Trying to withdraw {amount}")
#         if self.balance >= amount:
#             self.balance -= amount  
#             return f"Amount ${amount} withdarw successful"                     
#         else:
#             return f"Insufficient funds! Your balance is only {self.balance}."    
            
# sb1 = BankAccount("Manik")   

# print(sb1.deposit(100))         
# sb1.show_balance()  
# print(sb1.withdraw(50))       
# sb1.show_balance()  
# print(sb1.withdraw(150))       
  

#practice Question 3
import numpy as np

class DataModel:
    def __init__(self, data):
        self.data = data
        
    def get_mean(self):
        return np.mean(self.data)
            
    def scale_data(self, factor):
        self.data = [x*factor for x in self.data]
        return self.data
        
    def find_outliers(self, threshold):
        self.outliers = [x for x in self.data if x > threshold]  
        return self.outliers




dm = DataModel([10, 20, 30, 40, 50])
print(dm.get_mean())
print(dm.scale_data(2))
print(dm.find_outliers(50))










