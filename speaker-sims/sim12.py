# Python Simulation 12
# Tuple in Python

#declaring a tuple
print()
tpl = ()        #an empty tuple
print(f"Empty Tuple: {tpl}")

print()
names = ("John", "Paul", "Joseph", "Peter", "Simon")
print(f"Tuple Names: {names}")

print()
nums = (1,2,3,4,5)
print(f"Tuple Numbers: {nums}")

print()
employee = (4, "Elisha", True, 26.2312, 2023)
print(f"Tuple Employee Details: {employee}")

#uniqueness of tuple from a string
print()
name = ("Junell")
print(name, type(name), sep=" ==> ")

name = ("Maria",)
print(name, type(name), sep=" ==> ")

name = "Hannah"
print(name, type(name), sep=" ==> ")

name = "Elisha",
print(name, type(name), sep=" ==> ")

#accessing tuple elements
print()
names = ("John", "Paul", "Joseph", "Peter", "Simon")
print(f"Names: {names}")
print(f"Name at Index 0: {names[0]}")   #prints John
print(f"Name at Index 3: {names[3]}")   #prints Peter
print(f"Name at Index 4: {names[4]}")   #prints Simon

print()
nums = (1,2,3,4,5)
print(f"Tuple Numbers: {nums}")
print(f"Num at 3: {nums[3]}")       #4
print(f"Num at 1: {nums[1]}")       #2

print()
names = ("John", "Paul", "Joseph", "Peter", "Simon")
print(f"Names: {names}")
print(f"Index -1 Name: {names[-1]}")    #Simon
print(f"Index -3 Name: {names[-3]}")    #Joseph
print(f"Index -4 Name: {names[-4]}")    #Paul

#unpacking a tuple
print()
names = ("John", "Paul", "Joseph", "Peter", "Simon")
print(f"Names: {names}\n")
n1, n2, n3, n4, n5 = names
print(f"Name1: {n1}")
print(f"Name2: {n2}")
print(f"Name3: {n3}")
print(f"Name4: {n4}")
print(f"Name5: {n5}")

#more on tuple
print()
tpl = tuple("Hello")
print(f"Casted to Tuple: {tpl}")
print(f"Tuple Type: {type(tpl)}")
print()
tpl_num = tuple([1,2,3,4,5])
print(f"Converted Tuple: {tpl_num}")
print(f"Converted Type: {type(tpl_num)}")
print()
tpl_numNames = tuple({1:"One", 2:"Two", 3:"Three"})
print(f"New Tuple Nums: {tpl_numNames}")
print(f"Num Names Type: {type(tpl_numNames)}")
print()