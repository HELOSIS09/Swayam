# a=5
# b=7
# add_num=a+b
# print("the addition of two vars",add_num)
# print("the type of variable add_num is",type(add_num))

# from array import array

# array = array('i', [1, 2, 3, 4, 5])

# print("the given array is",array[0:3])

# z = 81


# if z % 7:
#     print("z is not divisible by 7")

# elif z % 7 == 0:
#     print("z is divisible by 7")
# # print(z % 8)

# # if z > 2:
# #     print("z is greater than 2")
# # elif z == 2:
# #     print("z is equal to 2")
# # else:
# #     print("z is less than 2")

# print('helo')
# print('helo')
# print('helo')
# numbers = [1, 2, 3, 4]
# numbers.append(5)
# print(numbers)
# # Output: [1, 2, 3, 4]

# list = ["apple", "banana", "cherry"]
# print("the given list is",list[::-1])

import os
# import file handler

# file handler = open("text file.text", "w")

# print("helo","text file.text")
# open_file = open(r'C:\Users\apurv\Downloads\Swayam\text file.txt', 'r')

# var = input("enter name","") 

# print(var)

# read = open_file.read()

# print("the content of the file is",read)
    
    
# with open("text file.txt", "r") as open_file:
#     content = open_file.read()

# f = open("text file.txt", "a")
# print(f.read())
# print("the content of the file is",f)


# open('text file.txt', 'a').close()  # This will clear the content of the file


# with open(r'C:\Users\apurv\Downloads\Swayam\text file.txt', 'r') as open_file:
#     content = open_file.read()
#     print("the content of the file is",content
#           )

#     with open(r'C:\Users\apurv\Downloads\Swayam\var.txt','w') as var2:
#       var2.write('this ios a new line')
# # fine = var2.write('this is a new line')

import json

user_data = {
    "name": "Alice",
    "age": 30,
    "is_admin": False
}


 

# Open a file in write mode ('w')
with open("data.json", "w") as file:
    # Optional: use 'indent' to make the file human-readable
    json.dump(user_data, file, indent=4)

dash = {
   "name": "alice",
    "salary": "30,000",
   "mood": "confused"
} 
with open("prac.json","w") as dash:
    json.dump(dash, dash, indent=4)
