# Simulation 15 - Day 4

num = [10,21,23,5123,5123,54]
for each_num in num :
    print(each_num)


myStr = 'ikennlouie'
for each_char in myStr :
    print(each_char)

#dict
myDict = {1: 24, 2: 33, 3: 54, 4: "wew"}
for each_dict in myDict.values() :
    print(each_dict)

for each_dict in myDict.items() :
    print(each_dict)

for each_dict in myDict.keys() :
    print(each_dict)

my_list = ['key1', 'key2', 'key3']
default_value = 0

# Using dict.fromkeys()
my_dict = dict.fromkeys(my_list, default_value)
print(my_dict)

