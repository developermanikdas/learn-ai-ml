# #7 constructor overloading 

# class Person:
#     def __init__(self, name, age = 0, address = "Not provided"):
#         self.name = name
#         self.age = age
#         self.address = address
        
#     def display(self):
#         print(f"Name: {self.name:8} | age: {self.age:2} | address: {self.address}")
        
# p1 = Person("Manik")    
# p2 = Person("Rahul", 23)    
# p3 = Person("Podo", 23, "Patuli")    
# p1.display()    
# p2.display()    
# p3.display()    



#8 Instance and class attributes.

# class Player:
    
#     player_count = 0

#     def __init__(self, name, level):
#         self.name = name
#         self.level  = level 
#         Player.player_count += 1

# def display_info(self):         
#     print(f"Player: {self.name} | Level: {self.level}")
    
    
# p1 = Player("Manik", 99)    
# p2 = Player("Rahul", 99)    
# p3 = Player("Rahul", 99)    

# print(f"Total player created {Player.player_count}")

        
        
#9 Multiple inheritance       

# class Herbivore:
#     def eat_plants(self):
#         print(f"I eat gree grass. 'Cause I am Herbivore ")

# class Carnivore:
#     def hunt(self):
#         print(f"I eat Flesh. 'Cause I am Carnivore ")
        
# class Omnivore:
#     def variety_diet(self):
#         print(f"I eat both grass & Flesh. 'Cause I am Omnivore ")        
        
        
# class Bear(Herbivore, Carnivore, Omnivore):
#     def __init__(self, name):
#         self.name  = name

#     def roar(self):
#         print("I Roar!!!")             
        
        
# bear = Bear("Baloo")        
# bear.roar()
# bear.eat_plants()
# bear.hunt()
# bear.variety_diet()