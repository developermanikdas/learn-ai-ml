#9 Find prime 

# n = int(input("Enter number: "))

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**(1/2))+1):
#         if n%i == 0:
#             return False
#     return True
# print(is_prime(n))  


 

#10 Guess the number

import random
secret_number = random.randint(1, 100)

while True: 
    my_guess = int(input("Guess the Number: "))

    if secret_number > my_guess:
        print("Try Bigger!")
    elif secret_number < my_guess:
        print("Try Smaller!")
    else:
        print("Congratulations! You found it.")
        break    


