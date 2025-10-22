# Python Simulation 07
# String Methods (Part 1)

#capitalizing the 1st letter and transforming the rest into lowercase
print()
text = "python programming"
print(f"Original Text: {text}")
print(f"Capitalized Text: {text.capitalize()}")
print()
tc1 = "pYthon is a Great Programming Language."
tc2 = tc1.capitalize()
print(f"Original Text: {tc1}")
print(f"Capitalized Text: {tc2}")

#converting strings into lowercase with casefold() method
print()
tcase1 = tc1
print(f"Casefolded String: {tcase1.casefold()}")
print("HElLo wORLd".casefold())

#returns a new centered-aligned string within a particular width
print()
message = "Hello"
print(message.center(2))
print(message.center(7))
print(message.center(19), "*")
print(message.center(17), "_")

#counting substring
print()
text = "I am learning python programming."
c1 = text.count('i')
c2 = text.count("python")
c3 = text.count("ng")
print(f"String: {text}")
print("The number of 'i' occurences is", c1)
print("The number of \"python\" occurences is", c2)
print("The number of \"ng\" occurences is", c3)
print()
t2 = text
c_text = 'n'
t_count1 = t2.count(c_text)
t_count2 = t2.count(c_text, 0, 24)
t_count3 = t2.count(c_text, 19, 32)
print(f"String: {t2}")
print(f"Number of '{c_text}' occurences: {t_count1}")
print(f"Number of '{c_text}' occurences from 0-24: {t_count2}")
print(f"Number of '{c_text}' occurences from 19-32: {t_count3}")

#identifying the end string
print()
e_text = "Python programming is easy to learn."
print(f"Original String: {e_text}")
print(f"String ends with a '.'? {e_text.endswith('.')}")
print(f"String ends with a earn.? {e_text.endswith("earn.")}")
print()
e_text2 = "Hello"
print(e_text2.endswith('o'))
print(e_text2.endswith('o', 0, 5))
print(e_text2.endswith('o', 0, 2))
print(e_text2.endswith('e', 1, 2))
print()
e_text3 = "Learning introduction to programming is best with python."
print(f"String: {e_text3}")
print(e_text3.endswith(("to", "is", "python."), 0, 19))
print(e_text3.endswith(("to", "is", "python."), 0, 62))
print(e_text3.endswith(("to", "is", "python."), 0, 39))
print(e_text3.endswith(("to", "is", "python."), 2, 35))
print(e_text3.endswith(("to", "is", "python."), 12, 62))

#defining the tab size for \t
print()
print("Hello")
print("Hel\tlo")
print("Hel\tlo".expandtabs())
print("Hel\tlo".expandtabs(3))
print("Hel\tlo".expandtabs(41))

#finding the index of a string
print()
message = "Hello World"
print(f"Message: {message}")
print("Index of H:", message.find('H'))
print("Index of e:", message.find('e'))
print(f"Index of o: {message.find('o')}")
print(f"Index of w: {message.find('w')}")
print("Index of \"World\":", message.find("World"))
print("Index of 'o':", message.find('o', 5, 8))
print("Index of 'x':", message.find('x'))

#returns the index of the first substring occurence
print()
letters = "RBGxZRRxY"
print(f"Index of 'R': {letters.index('R')}")
print(f"Index of 'B': {letters.index('B')}")
print(f"Index of 'G': {letters.index('G')}")
#print(f"Index of 'X': {letters.index('X')}") #results in error unable to index

#checking if all characters in a string are alphanumeric (letters and digits)
print()
str1 = "Hello123"
str2 = "123091"
str3 = "PythonProgramming"
print(f"String1: {str1}\nString2: {str2}\nString3: {str3}")
print(str1, str1.isalnum(), sep=" ==> ")
print(str2, str2.isalnum(), sep=" ==> ")
print(str3, str3.isalnum(), sep=" ==> ")
print()
str4 = "I am learning python programming language."""
str5 = "#15$"
str6 = "Hello\tWorld"
print(str4, str4.isalnum(), sep=" ==> ")
print(str5, str5.isalnum(), sep=" ==> ")
print(str6, str6.isalnum(), sep=" ==> ")

#checking if all characters in a string are alphabetic (letters)
print()
print(str1, str1.isalpha(), sep=" ----> ")
print(str2, str2.isalpha(), sep=" ----> ")
print(str3, str3.isalpha(), sep=" ----> ")
print(str4, str4.isalpha(), sep=" ----> ")
print(str5, str5.isalpha(), sep=" ----> ")
print(str6, str6.isalpha(), sep=" ----> ")

#identifying an ascii characters with isascii()
print()
ia1 = "こんにちは"   #sample of non-ascii characters
ia2 = "Python"
print(f"{ia1} is ASCII? {ia1.isascii()}")
print(f"{ia2} is ASCII? {ia2.isascii()}")

#check if all characters in a string are decimal digits (0-9)
print()
nstr1 = "12345"
nstr2 = "15.214"
nstr3 = "123ABC"
nstr4 = "Python"
print(nstr1, nstr1.isdecimal(), sep="\t")
print(nstr2, nstr2.isdecimal(), sep="\t")
print(nstr3, nstr3.isdecimal(), sep="\t")
print(nstr4, nstr4.isdecimal(), sep="\t")

#checks if string consists only of characters representing numerical digits (0-9)
print()
d1 = "123"
d2 = "abc"
d3 = "123abc"
print(f"{d1} is digit? {d1.isdigit()}")
print(f"{d2} is digit? {d2.isdigit()}")
print(f"{d3} is digit? {d3.isdigit()}")

#checks if string is a valid identifier or a variable name
print()
id1 = "3ABC"
id2 = "for_xyz"
id3 = "name"
id4 = "age"
print(f"Is {id1} a valid identifier? {id1.isidentifier()}")
print(f"Is {id2} a valid identifier? {id2.isidentifier()}")
print(f"Is {id3} a valid identifier? {id3.isidentifier()}")
print(f"Is {id4} a valid identifier? {id4.isidentifier()}")

#checking if all substring are in lowercase
print()
il1 = "java"
il2 = "PYTHON"
il3 = "python123"
print(f"{il1} is lower? {il1.islower()}")
print(f"{il2} is lower? {il2.islower()}")
print(f"{il3} is lower? {il3.islower()}")

#checks if all string is numeric or not
print()
in1 = "123"
in2 = "123abc"
in3 = "123 "
print(f"{in1} is a numeric string? {in1.isnumeric()}")
print(f"{in2} is a numeric string? {in2.isnumeric()}")
print(f"{in3} is a numeric string? {in3.isnumeric()}")

#checking if all characters in a string are printable (i.e., they can be
#displayed as-is, and they don't represent control characters)
print()
s1 = "HelloWorld"
s2 = "Hello World"
s3 = "Hello \tWorld"
s4 = "\"Hello World\""
s5 = "Hello World\n"
s6 = "Hello\
World"
print(f"{s1} ==>", s1.isprintable())
print(f"{s2} ==>", s2.isprintable())
print(f"{s3} ==>", s3.isprintable())
print(f"{s4} ==>", s4.isprintable())
print(f"{s5} ==>", s5.isprintable())
print(f"{s6} ==>", s6.isprintable())
