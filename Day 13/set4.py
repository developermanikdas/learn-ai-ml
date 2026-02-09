#7 constructor overloading 

class Person:
    def __init__(self, name, age = 0, address = "Not provided"):
        self.name = name
        self.age = age
        self.address = address
        
    def display(self):
        print(f"Name: {self.name:8} | age: {self.age:2} | address: {self.address}")
        
p1 = Person("Manik")    
p2 = Person("Rahul", 23)    
p3 = Person("Podo", 23, "Patuli")    
p1.display()    
p2.display()    
p3.display()    