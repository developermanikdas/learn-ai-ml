#1 Creating a programme that opens a file, write five names Then print the Name from the file. 

# with open("name.txt", "w") as f:
#     print("Enter 5 names: ")
#     for i in range(5):
#         name = input("Enter name: ")
#         f.write(name + "\n") 
        
# with open ("name.txt", "r") as f:
#     print(f.read())        


#2 Creating a file that opens Are failing in a pend mode. Add the new log entry And opens the file again in read mode and print all logs. 

# with open("log.txt", "a") as f:
#     f.write("\nProgramme run successfully. ")
    
# with open("log.txt", "r") as f:
#     data = f.read()
#     print(data)
    

#3 List comprehension.

# my_list = [1,14,63,2,27,37,9]  

# new_list = [x for x in my_list if x > 15]

# print(new_list)  


#4 Create a dictionary and save it in a json file.

# city_population = {
#     "kolkata": 10000,
#     "mumbai": 20000,
#     "karnataka": 40000,
# }

# import json
# # with open("cities.json", "w") as f:
# #     json.dump(city_population, f, indent = 4)

# with open("cities.json", "r") as f:
#     loaded_data = json.load(f)
    
#     # for city, pop in loaded_data.items():
#     #     print(f"{city}: {pop}")
    
#     new_city = input("Enter new city: ")
#     new_pop = int(input(f"Enter new population of {new_city}: "))
    
#     loaded_data[new_city] = new_pop
    
#     with open("cities.json", "w") as f:
#         json.dump(loaded_data,f, indent=4 )
        
#     print(f"Successfully updated {new_city} in cities.json!")



#5 handle unknown file opening error 
try: 
    with open("data.txt", "r") as f:
        f.read()
except FileNotFoundError:
      print("File not found!")  