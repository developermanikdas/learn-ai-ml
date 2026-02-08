#1 Practice Inheritace  
# class Teacher: 
#     def __init__(self, salary):
#         self.salary = salary

# class Student: 
#     def __init__(self, fees):
#         self.fees = fees

# class TA(Teacher, Student):
#     def __init__(self, salary, fees, name):
#         Teacher.__init__(self, salary)        
#         Student.__init__(self,fees)  
#         self.name = name
        
# ta1 = TA(20_000,4000, "Manik")  
# print(f"{ta1.name} earns {ta1.salary} and pays {ta1.fees}")


