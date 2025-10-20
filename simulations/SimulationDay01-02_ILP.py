# python simulation day 1 - file 02


name = input ( "enter your name:" )
print(f"Hello {name}")

decimal_number = 10
binary_string = bin(decimal_number)[2:]
print(binary_string)


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


#same literal value sharing memory address for small integers for efficiency
print()
num1 = 4
num2 = num1
num3 = 26-22
print(num1, id(num1), sep=" is at ")
print(num2, id(num2), sep=" is at ")
print(num3, id(num3), sep=" is at ")