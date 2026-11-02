# # with open('bookings.txt', 'w') as f:
# #  f.write('I am learning Python\n')
# #  f.write('Python is free and open source\n')

# # import json

# # with open(r'C:\Users\apurv\Downloads\Swayam\data.json','r') as f :
# #     data=json.load(f)
# #     print(data)

# # print("the content of the file is")

# exit(


# )
# print('lsdks'
      
#       )

# print('helo')










import pandas as pd
print('helo')

# dict_ = {
#     'item1': 'apple',
#     'item2': 'banana'
# }

# df = pd.DataFrame(dict_)

# print(df)

item18 = [1, 2, 3]
item28 = [4, 5, 6]

# 1. Pack your lists into a dictionary so Pandas can map them as columns
data = {
    'item1': item18,
    'item2': item28
}

# 2. Pass the dictionary into the DataFrame
fd = pd.DataFrame(data)
print(fd)

item3 = [7 ,8 ,9]

fd['item3'] = item3


print(fd)

with open(f'sex.csv','w') as f:
    f.write('item1,item2,item3\n')
    print(f)





