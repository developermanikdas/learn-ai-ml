# #1 Practice Abstraction 
# # from abc import ABC, abstractmethod

# # class Animal(ABC):
# #     @abstractmethod 
# #     def make_sound(self):
# #         pass

# # class Dog(Animal):    
# #     def make_sound(self):
# #         print("Bark...")

# # dogesh = Dog()    
# # dogesh.make_sound()


# #2 Practice Polymorphism 
#     # Function Overriding 
# class Parent:
#     def operation(self, a, b):
#         return a+b 
    
# class Child(Parent):
#     def operation(self, a, b):
#         return a*b 

# c1 = Child()    
# print(c1.operation(1,2))

#     #Duck Typing

# class Parent:
#     def operation(self):
#        print("Hello World")
# class Child:
#     def operation(self):
#           print("Hello World")

# p1 = Parent()       
# c1 = Child()       

# p1.operation()
# c1.operation()

#Q6 Abstraction

# class Employee:
#     def calculate_salary(self):
#         pass

# class Intern(Employee):    
#     def calculate_salary(self):
#         print("I have 20K salary!")

# class FullTimeEmployee(Employee):    
#     def calculate_salary(self):
#         print("I have 40K salary!")
        
# class ContractEmployee(Employee):
#       def calculate_salary(self):
#         print("I have 50K salary!")      
        
        
# i1 = Intern()        
# f1 = FullTimeEmployee()
# c1 = ContractEmployee()

# i1.calculate_salary()
# f1.calculate_salary()
# c1.calculate_salary()


#7 Constructor overloading with default parameters 