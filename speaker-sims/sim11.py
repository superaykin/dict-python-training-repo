# Python Simulation 11
# Python List

#working with list
print()
mylist = []
print(mylist)

names = ["John", "Luke", "Matthew", "Mark"]
print("List of Names:", names)

item = [1, "Maria", "Specialist", 81.21, True]
print("Raw List:", item)

#indexing a list
print()
print("List:", names)
print(f"At Index[0]: {names[0]}")
print(f"At Index[1]: {names[1]}")
#print(f"At Index[4]: {names[4]}")  IndexError: list index out of range

#list within a list
print()
num = [1, 2, 3, [4, 5, 6, [7, 8, [9]]], 10]
print(f"Num List: {num}")
print(num[0])               #returns 1
print(num[1])               #returns 2
print(num[3])               #returns [4, 5, 6, [7, 8, [9]]]
print(num[4])               #returns 10
print(num[3][0])            #returns 4
print(num[3][3])            #returns [7, 8, [9]]
print(num[3][3][2])         #returns [9]
print(num[3][3][2][0])      #returns 9

#class list
print()
nums = [1,2,3,4]
print(f"Num List: {nums}\nType List: {type(nums)}")

print()
nums = list({1:"one", 2:"two"})
print(nums)

#iterate a list
print()
list_names = ["John", "Luke", "Matthew", "Mark"]
print(f"List Names: {list_names}")

for name in list_names:
    print(f"Name: {name}")

print()
list_num = [1,2,3,4,5,6,7,8,9]
print(f"List Num: {list_num}")

count = 0
for num in list_num:
    count+=1
    print(f"Num = {num}")
    if count==6:
        print(f"It ends at {count}")
        break

#update a list
print()
names = ["Stephen", "Bill", "Steve", "Albert"]
print(f"Names: {names}")
names[0] = "Junell"
names[1] = "Elon"
print(f"Names: {names}")

names.append("Issac")
print(f"Names: {names}")

#removing, deleting, and popping item in the list
print()
names = ["Jeff", "Bill", "Steve", "Mohan"]
print(f"Names: {names}")

del names[0]
print(f"Updated Names: {names}")
names.remove("Bill")
print(f"Updated Names: {names}")

even = [2,4,6,8,10,12,14,16]
print(f"Even Numbers: {even}")
print(f"1st Odd Popping: {even.pop()}")     #removing 16
print(f"2nd Odd Popping: {even.pop(3)}")    #removing 8
print(f"Updated Even Numbers: {even}")
r1 = even.pop(0)
print(r1)
r2 = even.remove(12)
print(r2)

#exploring some more list methods
print()
x = [1,2,3,4,5]
print(f"List Num: {x}")
x.append(6)
print(f"Updated List Num: {x}")
x.insert(3,-1)     #inserting -1 at index 3
print(f"With Inserted Num: {x}")
x.remove(6)
print(f"New Num List: {x}")
x.remove(3)
print(f"Final List: {x}")

print()
print(f"There is a 4 in the list: {4 in x}")
print(f"List Num: {x}")
print(f"List Length: {len(x)}")
x.clear()
print(f"Cleared List: {x}")

#reversing a list
print()
my_name = ['J','u','n','e','l','l']
mn = []
count_name = len(my_name)
num = 1
print(my_name[len(my_name)-1:])
print(f"My Name: \t{my_name}")
while num<=count_name:
    mn.append(my_name[len(my_name)-num])
    num += 1
print("Reversed Name:  {}".format(mn))

print()
pope = ['F','r','a','n','c','i','s']
print(f"Pope's name: {pope}")
pope.reverse()                      #returns a None
print(f"Reverse name: {pope}")

#accessing a sliced list
print()
num = [11,22,33,44,55,60,70,80]
print(num)
print(num[0:3])     #starts at index 0 and stop at 3(excluded element)
print(num[:])       #not defined start and stop, prints all
print(num[3:])      #starts at index 3 up to the last element
print(num[0::2])    #defining step of 2 slice
print(num[::-1])    #reversing with negative step

print()
num_list = [2, 4, 6, 8, 10, 11, 12, 13, 14, 15]
print(f"List of Numbers: {num_list}")
del num_list[3:6]   #deleting 8, 10, 11
print(f"New List Numbers: {num_list}")

#extending a list
print()
n1 = [2,4,6]
n2 = [8,10,12]
print(f"1st List: {n1}\n2nd List: {n2}")
n1.extend(n2)
print(f"Extended List: {n1}\nN2 = {n2}")
n2.extend(range(3))
print(f"Extended N2 List: {n2}")
print(f"Concatenated List: {n1+n2}")

#counting list value
print()
c_list = ['H','A','N','N','A','H']
print(f"List Name: {c_list}")
print(f"Count 'H': {c_list.count('H')}")
print(f"Count 'A': {c_list.count('A')}")
print(f"Count 'N': {c_list.count('N')}")
print(f"Count 'j': {c_list.count('j')}")

#copying a list
print()
odd = [1,3,5,7]
copy_odd = odd.copy()
print(f"Odd Numbers: {odd}\nCopied Odd: {copy_odd}")
copy_odd.append(9)
copy_odd.append(11)
print(f"Updated Odd Numbers: {copy_odd}")

print()
name = "Hannah"
list_name = list(name)
print(f"Name: {name}\nList Name: {list_name}")
copied_name = list_name.copy()
n_name = list("Azaliah")
copied_name.append(n_name)
print(f"Copied List Name: {copied_name}")

print()
n2 = list("Elisha")
print(f"Name: {str(n2)}\nList Name: {n2}")
c_n2 = n2.copy()
n3 = list("Dinah")
c_n2.extend(n3)
print(f"Extended Copy of a Name List: {c_n2}")

#sorting a list (sorting by its ascii decimal)
print()
my_name = list("Junell")
"""
J=74  u=117   n=110   e=101   l=108   l=108
J  e  l  l  n  u
"""
print(f"My Name: {my_name}")
my_name.sort()                  #argument-less means ascending by default
print(f"Sorted Name: {my_name}")
my_name.sort(reverse=True)
print(f"Sorted Name: {my_name}")