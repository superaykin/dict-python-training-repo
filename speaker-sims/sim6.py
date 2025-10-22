# Python Simulation 06
# Python Operators

#using the operator module and its methods for arithmetic operation
print()
import operator

n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
print("The sum is", operator.add(n1,n2))
print("The difference is", operator.sub(n1,n2))
print("The product is", operator.mul(n1,n2))
print("The power is", operator.pow(n1,n2))

#exploring the assignment operators
print()
x1 = 5
x2 = 2
print(f"x1 = {x1}\nx2 = {x2}")
print()
print("{0} += {1} is".format(x1,x2), operator.iadd(x1,x2))
print("{} -= {} is".format(x1,x2), operator.isub(x1,x2))
print("{} *= {} is".format(x1,x2), operator.imul(x1,x2))
print(f"{x1} /= {x2} is {operator.itruediv(x1,x2)}")
print(f"{x1} //= {x2} is {operator.ifloordiv(x1,x2)}")

#working with comparison operators
print()
n1 = int(input("Enter num1: "))
n2 = int(input("Enter num2: "))
print("{} > {} evaluated as".format(n1,n2), n1>n2)
print("{} < {} evaluated as".format(n1,n2), n1<n2)
print("{} == {} evaluated as".format(n1,n2), n1==n2)
print(f"{n1} != {n2} evaluated as {n1!=n2}")
print(f"{n1} >= {n2} evaluated as {n1>=n2}")
print(f"{n1} <= {n2} evaluated as {n1<=n2}")

#exploring the logical operators
print()
l1 = 3
l2 = 5
print("{}>{} and {}<{} evaluated as".format(n1,n2,l1,l2), (n1>n2 and l1<l2))
print(f"{n1}<{n2} or {l1}<{l2} evaluated as {n1<n2 or l1<l2}")
print(f"{l1} > {l2} != {not l1>l2}") #3>5 = False since NOT therefore TRUE

#checking for similar id value with identity operator
print()
i1 = 3
i2 = 5 - 2
print(f"{i1} ID = {id(i1)}\n{i2} ID = {id(i2)}")
print(f"{i1} and {i2} has similar id value. {i1 is i2}")
print(f"{i1*3} ID = {id(i1*3)}\n{i2**3} ID = {id(i2**3)}") #9  id(9)     27 id(27)
print(f"{i1*3} and {i2**3} does not have a similar id value. {(i1*3) is not {i2**3}}")

#working with membership operator
print()
t1 = 'e'
t2 = "Hello"
print(t1, "is in", t2, "--->", t1 in t2)
print("{} is not in {} --->".format(t1,t2), t1 not in t2, end="\n\n")

#working with bitwise operator
"""
When working with coded file systems that say has 644 file permission
which constitutes a groupings for file owner, group category, everyone else
6 = 110 means you can read file, write file, but not execute a file for the owner
4 = 100 means you can read file, but not write and execute a file for the category
4 = 100 means you can read file, but not write and execute a file for everyone else
"""

b1 = int(input("First Number: "))   #assuming 5 is inputted
b2 = int(input("Second Number: "))  #assuming 10 is inputted
print("{} & {} the result is".format(b1,b2), operator.and_(b1,b2))
"""
    5  = 0101
  & 10 = 1010
  res  = 0000 = 0
"""
print(f"{b1} | {b2} the result is {operator.or_(b1,b2)}")
"""
    5   = 0101
 |  10  = 1010
  res   = 1111 = 8+4+2+1 = 15
"""
print(f"{b1+1} XOR {b2} = {(b1+1)^b2}")
"""
    6   = 0110
 ^  10  = 1010
  res   = 1100 = 8+4+0+0 = 12
"""
print(f"The invert of {b1} is {~b1}.")
"""
2s complement with 8 bit representation
 5 = 0000 0101
 ~ = 1111 1010 where leftmost bit is treated with sign (1 negative / 0 positive)
 therefore -128+64+32+16+8+0+2+0 = -6
"""