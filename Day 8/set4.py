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

# class Book:
#     def __init__(self, title, author, review):
#         self.title = title
#         self.author = author
#         self.review = review
        
#     def add_review(self, new_review):
#         self.review.append(new_review)
    
#     def count_review(self):
#         print(len(self.review))
        
#     def show_review(self):
#         print(self.review)    
        
# book1 = Book("The Secret", "Rhonda Byrne", ["It Was superb", "Page Turner", "Really Secret inside"])            


# book1.show_review()



#3 Encapsulation

# class Student:
#     def __init__(self, name, roll, mark):  
#         self.set_name(name)
#         self.set_roll(roll)
#         self.set_mark(mark)
    
#     def set_name(self, name):
#         if not name and name.stripe() == "":
#             print("Name cannot be empty")
#         else:    
#             self._name = name    
            
#     def set_roll(self, roll):        
#         if roll > 100 and self._roll < 0:
#             print("Roll must be within 1 - 100")
#         else:
#             self._roll = roll    
            
#     def set_mark(self, mark):
#         if mark < 0:
#             print("Name cannot be negative")      
#         else:
#             self._mark = mark   
            
#     def get_name(self):
#         return self._name
#     def get_roll(self):
#         return self._roll
#     def get_mark(self):
#         return self._mark          
            
# s1 = Student("Manik", 12, 99)     

# print(s1._name, s1._roll, s1._mark)
# print(s1.get_name())       
# print(s1.get_roll())       
# print(s1.get_mark())       



#4 Function Overriding 

class Shape:
    def area(self):
        print("I'll be overridden") 

class Circle(Shape):
    
    def __init__(self, name , radious):
        self.name  = name
        self.radious = radious
        
    def area(self):
        return (22/7 * self.radious**2)     

class Rectangle(Shape):
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
    
    def area(self):    
        return (self.length * self.width)
                
class Triangle(Shape):
    def __init__(self, name,  base, height):
        self.name = name
        self.base = base
        self.height = height
        
    def area(self):
        return (1/2 * self.base * self.height)
    
shapes = [Circle("Circle", 1), Rectangle("Rectangle", 10, 5), Triangle("Triangle",10, 5)]

for s in shapes:
    print(s.area())        
        
    