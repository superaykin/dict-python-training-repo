# Python Simulation 02
# Working with Data Types and Operators

#getting the user input
print()
text = input()      #reading line of text from user via console terminal
print("You've entered:", text)

print()
name = input("Enter name: ")
print("Hello", name, end="\n\n")

#taking string then converting to int
n1 = int(input("Enter 1st number: ")) 
n2 = int(input("Enter 2nd number: "))
result = n1 + n2
print("Result =", result, end="\n\n")

#returning type from the input function
print("Data Type of name is", type(name))
age = input("Enter age: ")
print("Age data type is", type(age))
age_ = int(input("Age: "))
print("Age data type is", type(age_))

#identify class name or data types
print()
print(type(26))
print(type(2.51231))
print(type("Azaliah"), end="\n\n")

#exploring python's dynamic data types
a = 43
b = 4123.41231232
c = "42"
d = True
print(a, type(a), sep=" is a ")
print(b, type(b), sep=" is a ")
print(c, type(c), sep=" is a ")
print(d, type(d), sep=" is a ")

#working with the + operator
print()
num1 = 5
num2 = 3
print(num1, " + ", num2, " = ", num1+num2)  #addition
str1 = "Hello"
str2 = "World"
print(str1, " + ", str2, " = ", str1+str2)  #concatenation
#print(str1, " + ", num2, " = ", str1+num2) TypeError: can only
#concatenate str (not "int") to str

#examining data types of mathematical operation
print()
n1 = 23
n2 = 3
r1 = n1 + n2
r2 = n1 - n2
r3 = n1 * n2
r4 = n1 / n2
r5 = n1 // n2
r6 = n1 % n2    #calculating the remainder with modulo %
r7 = n1 ** n2
print(n1, type(n1), n2, type(n2), sep="\n")
print(n1, "+", n2, "=", r1, " is a ", type(r1))
print(n1, "-", n2, "=", r2, " is a ", type(r2))
print(n1, "*", n2, "=", r3, " is a ", type(r3))
print(n1, "/", n2, "=", r4, " is a ", type(r4))
print(n1, "//", n2, "=", r5, " is a ", type(r5))
print(n1, "%", n2, "=", r6, " is a ", type(r6))
print(n1, "**", n2, "=", r7, " is a ", type(r7))

#using a digit grouping symbol in numeric literals to enhance readability
print()
n1 = 1231241231231
print("n1 is equal to", n1, type(n1))
n2 = 1_231_241_231_231
print("n2 is equal to", n2, type(n2))

#identifying object's location (object's unique identifier - memory address)
print()
name = "Maria"
age = 35
print(name, id(name), sep=" ==> ")
print(age, id(age), sep=" ==> ")

#same literal value sharing memory address for small integers for efficiency
print()
num1 = 4
num2 = num1
num3 = 26-22
print(num1, id(num1), sep=" is at ")
print(num2, id(num2), sep=" is at ")
print(num3, id(num3), sep=" is at ")

#exploring the number systems
print()
binary_num = 0b1001     #1001 = (8*1)+(4*0)+(2*0)+(1*1) = 8+0+0+1 = 9
print(binary_num, " is equal to 1001 binary and type is ", type(binary_num))
octal_num = 0o212   #010 001 010 = 128+8+2 = 138
print(octal_num, " is equal to 212 octal and type is ", type(octal_num))
hex_num = 0xA1      #1010 0001 = 128+32+1 = 161
print(hex_num, " is equal to A1 hexadecimal and type is ", type(hex_num))

#single line statement with multiple variable assignment under similar class type
print()
d1, d2, d3 = 24, 14, 16
print("d1 =", d1)
print("d2 =", d2)
print("d3 =", d3, end="\n\n")

#single line statement with multiple variable assignment under different class type
d4, d5, d6 = 21, "Hello", False
print("d4 =", d4, "\nd5 =", d5, "\nd6 =", d6, end="\n\n")