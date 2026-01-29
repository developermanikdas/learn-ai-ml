#3 print digit of numbers 

# n = int(input("Enter number: "))

# while n>0:
#     last_digit = int(n%10)
#     n = int(n/10)
#     print(last_digit)       
    
    
    
#4 Count digits of a number

# n = int(input("Enter number: "))
# count = 0
# while n>0:
#     n = int(n/10)
#     count+=1
    
# print(count) 



#5 sum of digits

# n = int(input("Enter number: "))
# sum = 0
# while n>0:
#     last_digit = n%10
#     sum+=last_digit
#     n = int(n/10)
    
# print(sum) 




#6 divisable by 3 & 5

# n = int(input("Enter range: "))

# for i in range(1, n+1):
#     if i%15 == 0:
#         print(i)



#7 continuously print (+ve) or (-ve) until typed "Quit"


# while True:
#     n = (input("Enter number or ('quit' to exit) "))
    
#     if n == "quit":
#         break
#     try:
#         # Convert once and store it in a variable
#         num = float(n) 
        
#         if num > 0:
#             print("(+ve)")
#         elif num < 0:
#             print("(-ve)")
#         else:
#             print("Zero is neither (+ve) nor (-ve)")
            
#     except ValueError:
#         print("Invalid input! Please enter a number or 'quit'.")  
            