# Python Simulation 03
# Python Data Types and Casting

#casting to integer
print()
n1 = "78"; n2 = 5.32; n3 = 100
print(n1, type(n1), sep=" ==> ")
print(n2, type(n2), sep=" ==> ")
print(n3, type(n3), sep=" ==> ")

print()
m1 = int(n1)
m2 = int(n2)
print(m1, type(m1), sep=" is now a ")
print(m2, type(m2), sep=" is now a ")

m3 = int("100", 2)  #converting binary string to int
"""
                    1 0 0
                    4 2 1
                    4 only remains
"""
print(m3, type(m3), sep=" is now a ")

m4 = int("ABF", 16) #converting a hexadecimal string to int
"""
A=1010; B=1011; F=1111
ABF => 1010 1011 1111
        1+2+4+8+16+32+128+512+2048
        = 2751
"""
print(m4, type(m4), sep=" is now a ")

#casting to float
print()
f1=1.2; f2=123_345.23_423; f3=123
print(f1, type(f1), sep="\t\t")
print(f2, type(f2), sep="\t")
print(f3, type(f3), sep="\t\t")

print()
p1 = float(f3)
print(p1, type(p1), end="\n\n")

#used of scientific notation as a short representation
f4=1e3; f5=3e5
print(f4, type(f4), sep=" ==> ")
print(f5, type(f5), sep=" ==> ")

#more on float casting
print()
float1 = "5.32"
float2 = 123_456
print(float1, type(float1), sep="\t")
print(float2, type(float2), sep="\t", end="\n\n")

c_float1 = float(float1)
c_float2 = float(float2)
print(c_float1, type(c_float1), sep="\t")
print(c_float2, type(c_float2), sep="\t", end="\n\n")

#arithmetic operators
n1 = int(input("Enter 1st number: "))
n2 = float(input("Enter 2nd number: "))
add = n1 + n2
sub = add - n2
mul = sub * n2
div = add / sub
f_div = add // sub
print(f"{n1} + {n2} = {add}")
print(f"{add} - {n2} = {sub}")
print(f"{sub} * {n2} = {mul}")
print(f"{add} / {sub} = {div}")
print(f"{add} // {sub} = {f_div}")

#working with complex function
print()
c1 = 4 + 3j
c2 = 2 + 1j
c_add = c1 + c2
c_sub = c1 - c2
c_prod = c1 * c2
"""
remember that i^2 = -1
= 8 + 10j + 3j^2
= 8 + 10j + 3(-1)
= 8 + 10j -3
= 5 + 10j
"""
c_div = c1 / c2
print(f"\nGiven:\n\tc1 = {c1}\n\tc2 = {c2}\n")
print(f"Complex Addition Result: {c_add}")
print(f"Complex Subtraction Result: {c_sub}")
print(f"Complex Multiplication Result: {c_prod}")
print(f"Complex Division Result: {c_div}")

#working with the power function
print()
print(f"10 raised to the power of 2 is {pow(10,2)}")
print("100 raised to the power of 0.5 is", pow(100,0.5))
print("25 raised to the power of -2 is", pow(25,-2))

#working with the absolute value
print()
print("The absolute value of -5 is", abs(-5))
print("The absolute value of string 67 is", abs(int("67")))
print("The absolute value of -4.81 is", abs(-4.81))

#working with the round function
print()
print("1234.4351 rounded into 2 decimal places is", round(1234.4351, 2))
print("512.123124 rounded into 1 decimal place is", round(512.123124, 1))
print("21.925123 rounded into 0 decimal place is", round(21.925123, 0))
print("21.925123 rounded into -1 decimal place is", round(21.925123, -1))