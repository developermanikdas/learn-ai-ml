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

n = int(input("Enter number: "))
sum = 0
while n>0:
    last_digit = n%10
    sum+=last_digit
    n = int(n/10)
    
print(sum) 
