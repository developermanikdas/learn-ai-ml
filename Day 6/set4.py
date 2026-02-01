###1 Practice 

# class Student:
#     school = "PHS",
#     section = "A"
    
#     def __init__(self, name):
#         self.name = name
#     def print_section(self):
#         print(self.section)
#     def set_section(self, new_section):
#         self.section = new_section

# s1 = Student("Rahul")    

# print(s1.name)
# s1.print_section()
# s1.set_section("B")
# s1.print_section()



###2 Practice


class Store:
    product_count = 0
    
    
    def __init__(self, product, price):
        self.product = product
        self.price = price
        Store.product_count+=1
    
    @classmethod
    def print_count(cls):
        print(f"There are {cls.product_count} Products")
        
    @staticmethod    
    def calc_discount(price, disount):
        return (price - (price*(disount/100)))

product1 = Store("Laptop", 40_000)
product2 = Store("Keyboard", 6_000)
product3 = Store("Mouse", 1_000)

print(Store.calc_discount(1000,10))
Store.print_count()