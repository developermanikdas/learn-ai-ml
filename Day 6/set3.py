#6 Create dict from list

# my_list = ["Apple", "Banana", "Grape", "Cucumber", "Kiwi"]

# length_dict = dict()

# for item in my_list:
#     fruit_length = len(item)
#     length_dict.update({item: fruit_length})

# print(length_dict)



#7 input string and count Space 

# my_string = input("Enter String: ")
# space_count = 0

# for ch in my_string:
#     if ch == " ":
#         space_count+=1
# print(space_count)        



#8 check whether list share common elements

# list1 = [1,2,3,4,5]
# list2 = [4,5,6,7,8]

# set1 = set(list1)
# set2 = set(list2)

# print(set1.intersection(set2))
# print(set1.union(set2))



#9 Check duplicate elms in a set

# list1 = [1,2,3,4,5,2,4,8,1,2,4,4]

# seen = set()
# duplicate = set()

# for i in list1:
#     if i in seen:
#         duplicate.add(i)
#     else:
#         seen.add(i)    
# print(duplicate)    



#10 Input string and count unique character and their count

# my_string = input("Enter String: ")

# unique_char = set(my_string) 
# unique_char_count = dict()

# for ch in unique_char:
#     unique_char_count[ch] = (my_string.count(ch))

# print(unique_char_count)    
    