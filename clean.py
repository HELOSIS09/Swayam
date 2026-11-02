# import pandas as pd
# #read data file from desktop of type .csv
# df1= pd.read_csv(r'C:/Users/Dr. Shano/Desktop/moocs recording/files/csv.csv', 'r')
# # print(df1)
# import webbrowser
from urllib import error

# with open(r'C:\Users\apurv\Downloads\Swayam\text file.txt','a') as var:
#   var.write('I am adding new line into text line')


# with open(r'C:\Users\apurv\Downloads\Swayam\text file.txt', 'r') as f:
#  for line in f:
#   print(line)



with open(r'C:\Users\apurv\Downloads\Swayam\text file.txt', 'w') as f:
 f.write('I am learning Python\n')
 f.write('Python is free and open source\n')

with open(r'C:\Users\apurv\Downloads\Swayam\text file.txt', 'r') as f:
 for line in f:
  print(line)

# with open(r'C:\Users\apurv\Downloads\Swayam\text file.txt', 'w') as s:
#  for data in s:
#   print(data)

dict = {
 "name":"apurv",
 "age":"22",
"gender":"male"
}

import json

with open('data.json','w') as f:
 data = json.dump(dict,f)

print(dict)

list = [1,2,3,4]

print(list[3])

with open(r'bookings.txt','a') as f:
     f.write("pax no 1 - kartik\n")
     f.write('pax no 2 - lucy')

try:

        import webbrowse
    # webbrowser.open('youtube.com')

except ModuleNotFoundError:
  print('Please import the required module first')

try:
    divide = 10/0
    print(divide)

except Exception as e:
    print('It is not possible in python to divide by zero')

with open('bookings.txt','r') as f :
     data = f.read()
print(data)

x = 0
y = 4
try:
  if  eval('x==x'):
      print("x is equal to x")
except SyntaxError as e:
      print('not possible')

# import  webbrowser
# try:
#     if NameError:
#        webbrowser.open('helosis09.github.io/Tourcraft')
#
# except NameError as e:
#     print('unknown error')

list = ["apple","banana","kiwi"]

print('index of kiwi is ',list.index("kiwi"))
print(list[0])

# import webbrowser
# try:
#     if NameError:
#        webbrowser.open('helosis09.github.io/check')
#
# except NameError:
#     print('Unkown error')
#
# finally:
#       with open(r'bookings.txt','r') as f:
#        Final_var = f.read(56)
#        print(Final_var)

print('now this file is added to github')

try:
    if NameError:
       list = ["This","is","a","list"]
       print(list[0])
       print(list[1])
       print(list[2])
       print(list[3])

except NameError:
    print('There is some issue in syntax of list')

finally:
    print('This is finally statement mum❤️')

# set = {1,2,3}
#
# list = [1,2,3]
#
# tuple = (9,3,2)
#
# dict = {
#     "company":"Shubh yatra global",
#     "Purchase":"$4530"
# }
#
# print(tuple[0])
#
# print(list*2)

import numpy as np

array = [1,2,3,4,5]
array_2 = [[1,2],[3,4]]

print(array,array_2)
var_array=np.array([1,2,3,4,5])

print(np.array((1,2,3,4,5)*2))

type(var_array)
print(type(var_array))


import numpy
arraymc=np.ones((2,3))

print(arraymc)

np.arange(2,3,4)
 

import random

random_Var1=np.random.randint(1,10,(3,4),dtype=int)

print(random_Var1)
      





first_array = np.array(["sajan", "SAJAN", "teri", "dulhan"])
second_array = np.array(["tujhko", "pukare", "aaja"])
Gaana=print(first_array,second_array)
print(Gaana)
      
x = ([1,2],[3,4])

y = ([5,6],[7,8])

add = np.add(x,y)
print(add) 
 
Radian_values = np.array([0,np.pi/3,np.pi/6,np.pi/9]) 
Sine_val_func=np.sin(Radian_values)
print(Sine_val_func)     
      
# transpose = np.array([1,2,3,4],[5,6,7,8])
# Func_for_transposing = np.transpose(transpose) 
# print(Func_for_transposing) 
 
 
max_array = np.array([12,34,45,29,56])
Max_array_val = np.max(max_array)

print(Max_array_val) 
      
      
      
image = np.array([[10, 20, 30],
[40, 50, 60],
[70, 80, 90]])
#returns a copy of the array collapsed into one dimension
flat_image = image.flatten()
print("Original Image Matrix:\n", image)
print("\nFlattened Image:\n", flat_image)


sort_var = np.array([34, 94,23,89])
sort_func = np.sort(sort_var)

print(sort_func)
      
      
import pandas as pd

list_pd = [11,12,13,14]
my_series = pd.Series(list_pd)
print(my_series)      
      

import pandas as pd

list_pd = [11,12,13,14]
my_series = pd.Series(list_pd)
print(my_series)
# print(list_pd.Series(list_pd))

import rich


import pandas as pd
import numpy as np

df = pd.read_csv("csv.csv")
df.info()

df.isnull()












