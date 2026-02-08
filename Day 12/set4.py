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