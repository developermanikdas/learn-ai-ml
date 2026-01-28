#1 calculate tax

# salary = int(input("Enter your salary: "))

# if(salary > 0):
#     if(salary < 30000):
#         tax = 5
#     elif (salary >= 30000 and salary <=70000):
#         tax = 15 
#     else:
#         tax = 25
        
#     tax_amount = salary*((tax)/100) 
#     print(f"Your tax {tax}% is  : {tax_amount}")    
# else: 
#     print("Please enter a valid salary.")


    
#2 Prints odds and evens within a range

start = int(input("Enter Start: "))
end = int(input("Enter End: "))

for i in range(start, end+1):
    if(i%2 == 0):
        print("Even: ", i)
    else:
        print("Odd: ", i)    
    


