#5 Inheritance

class Vehicle:
    def  __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, seat):
        self.seat = seat        
        
class Bike(Vehicle):
    def __init__(self, engine):
        self.engine = engine        
                
s1 = Bike("125CC")