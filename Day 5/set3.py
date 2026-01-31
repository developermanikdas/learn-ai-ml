#2 avg of ints in a list

# list1 = [] 

# avg = 0
# total = 0

# if len(list1) == 0:
#     print("Enter valid list.") 
# else:
#     for i in list1:
#         total = total + i
#     avg = total/len(list1)   
#     print("The average is ", avg) 



#3 input and merge 2 lists

# list1 = []
# list2 = []

# for i in range(5):
#     elm = int(input("Enter element: "))
#     list1.append(elm)
# for i in range(5):
#     elm = int(input("Enter element: "))
#     list2.append(elm)

# list1.extend(list2)    
# print(list1)




#4 Create odd & even tuple list from random tuple

# my_tuple = (1,2,3,4,5,6,7,8,9,10)

# odd_list = list()
# even_list = list()

# for i in my_tuple:
#     if i%2 == 0:
#         even_list.append(i)
#     else:
#         odd_list.append(i)    

# print(tuple(odd_list))        
# print(tuple(even_list))        



#5 Dictionary operation add update search display all keys

# data = {
#     "Manik": 99,
#     "Rahul": 71,
#     "Vanshi": 100
# }

# selection = input("Enter Operation name: (A - add student, B - update marks, C - Search, D - display all key & values): ").lower()

# match selection:
#     case "a":
#        student_name = input("Enter student name: ") 
#        student_mark = input("Enter student mark: ") 
#        data.update({student_name: student_mark})
#     case "b":
#        student_name = input("Enter student name to Update mark: ") 
#        student_mark = input("Enter student updated mark: ") 
#        data.update({student_name: student_mark})
#     case "c":
#        student_name = input("Enter student name to find: ") 
#        print(data[student_name])
#     case "d":
#         print(data.items())   
           
           

