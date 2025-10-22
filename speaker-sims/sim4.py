# Python Simulation 04
# Python String

#valid string literals in python
#"literal" refers to a value that is directly written into the code
print()
print('This is a pair of single quoted string')
print("This is a pair of double quoted string")
print('''This is a triple-paired single quoted string!''')
print("""This is a triple-paired double quoted string!""")

#assigning string literal value to a variable
print()
name="Junell";  text="I am learning python programming."
print("Hello, I am", name, "and", text, end="\n\n")

#multi-line string wrapped with triple quotes
sml1 = '''This is
the first multi-line
string.'''
sml2 = """This is the 2nd
multi-line string."""
print(sml1, sml2, sep="\n\n")

#embedding quotes into a string literal
print()
e_str1 = 'The movie "The Lord of the Rings" is the best franchise movie.'
e_str2 = "I like watching 'The Big Bang Theory' tv-series."
print(e_str1, e_str2, sep="\n\n")

#indentifying the length of a string
print()
l1 = len(e_str1)
l2 = len(e_str2)
print(f"{e_str1} = {l1}")
print(f"{e_str2} = {l2}")

#fetching a character from a string with its index, starts at 0
print()
u_text = input("Enter a text: ")
print("Index 0 is", u_text[0])
print("Index 1 is", u_text[1])
print("Index 3 is", u_text[3], end="\n\n")
#print("Index 6 is", u_text[6]) #"python"==IndexError: string index out of range

#negative indexing of string, starts -1
print("u_text[-1] =", u_text[-1])   #n
print("u_text[-2] =", u_text[-2])   #o
print("u_text[-5] =", u_text[-5])   #y

#casting into a string
print()
n1=100; n2=23.12; n3=0xAB1
print(f"{n1} --> {type(n1)}")
print(f"{n2} --> {type(n2)}")
print(f"{n3} --> {type(n3)}")
print(f"Total = {n1+n2+n3}")
print()
ns1 = str(n1)
ns2 = str(n2)
ns3 = str(n3)
print(ns1, ns2, ns3, sep="\t\t")
print(type(ns1), type(ns2), type(ns3), sep="\t")
s_total = ns1+ns2+ns3
print(f"\nString Total = {s_total}\t{type(s_total)}")

#using escape character to include quotes similar to its outer wrap
print()
ms1 = 'I\'m Batman!'
ms2 = "\"Avengers: Endgame\" is an epic finale."
print("String 1 =", ms1)
print("String 2 =", ms2)

#backspace character control
name = "Hanna\bh"
print(f"Name: {name}")
print("Hanna\bh")
"""
Printing in an IDE or terminal: Some integrated development environments
(IDEs) or terminals may not interpret the backspace character correctly.
The behavior of backspace might vary depending on the environment.
"""

#working with string operators
print()
a = "Hello"
b = "World"
print(a+b)      #HelloWorld
print(a*3)      #HelloHelloHello
print(a[2])     #l
print(b[0:3])   #Wor
print("Is r in World?", ('r' in b))         #True
print("Is k NOT IN Hello?", ('k' not in a)) #True

#more on string indexing and slicing
print()
language = "Python"
print(f"At index 2 = {language[2]}")    #t
print(f"At index 0 = {language[0]}")    #P
print(f"At index -5 = {language[-5]}")  #y
print(f"At index 1 = {language[1]}")    #y
print(f"At index -4 = {language[-4]}")  #t
print(f"At index 3 = {language[3]}")    #h

print()
print("At range 0:2 =", language[0:2])      #Py
print(f"At range 1:5 = {language[1:5]}")    #ytho

print()
result = language[1:5]
print(f"Original String: {language}")
print(f"Sliced String: {result}")
print(f"Is 'x' in Sliced String? {'x' in result}")  #False
print(f"Is 'a' in Sliced String? {'a' in result}")  #False
print(f"Is 'b' in Sliced String? {'b' in result}")  #False
print(f"Is 'c' in Sliced String? {'c' in result}")  #False
print(f"Is 'P' in Sliced String? {'P' in result}")  #False
print(f"Is 'y' in Sliced String? {'y' in result}")  #True

#Python
print()
print("Range :2 =", language[:2])           #Py
print("Range 4: =", language[4:])           #on
print("\nCombined Range:")
print(language[:2] + language[2:])          #Py+thon = Python
print(language[:4] + language[1:])          #Pythython
print(language[2:4] + language[-1:-4])      #th
print(f"What is the output? {language[-1:-2]}")
#starting index is greater than or equal to the ending index.
#Therefore, the output is an empty string
print()
print(language[-5:-2])      #yth
print(language[-3:])        #hon
print(language[-4:-3])      #t

#checking for the existence of specific character or sequence within a string
print()
es = "I am learning python programming!"
verify1 = 'n' in es
print("String Verification [True or False]:", verify1)
verify2 = "x1das" not in es
print("String Verification [True or False]:", verify2, end="\n\n")