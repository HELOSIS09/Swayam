# import json

# # Your Python dictionary
# data = {
#     "name":"apurv",
#     "age":"22",
#     "city":"New York"
# }
# # 
# # Open a file in write mode and use json.dump() to save it
# with open(r"C:\Users\apurv\Downloads\Swayam\data.json", "w") as file:
#     json.dump(data, file, indent=4)


list = ["This","is","a","list"]

print(list[0],[1],[2],[3])  

# # import json
# # import csv
# # with open('sex.txt','w') as f:
# #     f.write('file')



# with open(r'sex.txt','a') as f:
#     # f.write('Voila')
# data = f.write('syn')
# print(data)
import json

my_dict = {
    "name": "alice",
    "age": "23"
}

with open('sex.txt', 'w') as f:
    json.dump(my_dict, f, indent=4)

print(my_dict)

