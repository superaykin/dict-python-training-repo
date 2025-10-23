#working with set
print()
even_nums = {2,4,6,8,10}
emp_data = {1, "Junell", 5.5, True, 1.1}    #True and 1 are treated the same
num = {1,2,3,2,1,4,5,5,4,6,7}
raw_num = {(10,10), 20, 30}
m = {False, True, 0}

print(f"Set of Even Numbers: {even_nums}")
print(f"Employee Data: {emp_data}")
print(f"Numbers: {num}")
print(f"Raw Number: {raw_num}")
print(f"Boolean: {m}")

#create a set
print()
s = set()
print(s, type(s), sep=" --> ", end="\n\n")

#transforming into set
print()
s1 = set("Hello")
print(s1)
s2 = set((1,2,3,4,5))
print(s2)
my_dict = {1:"One", 2:"Two", 3:"Three"}
s3 = set(my_dict)
print(s3)


#modifying a set
print()
set1 = set()
print(set1)
set1.add(10)
print(set1)
set1.add(20)
set1.add(30)
print(set1)
raw_num = {21, 13,5, 7, 9}
print(raw_num)
set1.update(raw_num)
print(f"New Set of Numbers: {set1}")