class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seat):
        # Pass brand and model to Vehicle
        super().__init__(brand, model) 
        self.seat = seat        
        
class Bike(Vehicle):
    def __init__(self, engine, brand, model):
        # Added () to super and kept brand/model
        super().__init__(brand, model)
        self.engine = engine        
                
s1 = Bike("125CC", "Hero", "Honda Model")
print(f"Brand: {s1.brand}, Engine: {s1.engine}")