# Python Simulation 08
# String Methods (Part 2)

#checks if strings has all whitespace
print()
isp1 = "A B C"
isp2 = "python "
isp3 = "    "
print(f"The 1st string has all whitespace: {isp1.isspace()}")
print(f"The 2nd string has all whitespace: {isp2.isspace()}")
print(f"The 3rd string has all whitespace: {isp3.isspace()}")

#checks whether the 1st character of a string is in uppercased
print()
st1 = "Hello World"
st2 = "Hello WORLD"
st3 = "hello world"
st4 = "HelloWorld"
st5 = "Hello world"
print(f"{st1} == {st1.istitle()}")
print(f"{st2} == {st2.istitle()}")
print(f"{st3} == {st3.istitle()}")
print(f"{st4} == {st4.istitle()}")
print(f"{st5} == {st5.istitle()}")

#checks if all characters are in uppercased or not
print()
sl1 = "HELLO WORLD"
sl2 = "Hello World"
sl3 = "HELLO_WORLD"
sl4 = "$!@a#!@%@##@!"
sl5 = "{}LASD><>)(AR"
print(f"{sl1} --> {sl1.isupper()}")
print(f"{sl2} --> {sl2.isupper()}")
print(f"{sl3} --> {sl3.isupper()}")
print(f"{sl4} --> {sl4.isupper()}")
print(f"{sl5} --> {sl5.isupper()}")

#iterable concatenation of a string
print()
sep1 = "__"
string = "HELLO"
print(f"{sep1}\t{string}")
print(sep1.join(string))
print()
sep2 = ", "
names = ["Matthew", "Mark", "John", "Luke"]
print(f"The gospel of {sep2.join(names)} all tells a unique story of Jesus.")

#left-justify a string within a specific width by padding it
#with spaces or any specified character.
print()
lj1 = "Python"
lj2 = "Hannah Azaliah"
print(f"Original Text: {lj1}\nPadded Text: {lj1.ljust(10)}") #10 is > Python string
print(f"Original Text: {lj2}\nPadded Text: {lj2.ljust(25, '&')}")

#converting string into lowercase
print()
orig_str = "HELLO WORLD"
my_str = orig_str.lower()
print(f"Original String: {orig_str}")
print(f"New String: {my_str}", end="\n\n")
print("JUNELL T. BOJOCAN".lower())

#removing the leading characters of a string
print()
st1 = "        Hello World        "
st2 = "HelloWorld"
st3 = "-------------Hello World-------------"
print(st1, st1.lstrip(" "), sep="\n")
print(st2, st2.lstrip(" "), sep="\n")
print(st3, st3.lstrip("-"), sep="\n")

#mapping substring for data manipulation
print()
trans_data = str.maketrans("aeiou", "AEIOU")
t1 = "Java"
t2 = "Python"
t3 = "I am learning python."
trans1 = t1.translate(trans_data)
trans2 = t2.translate(trans_data)
trans3 = t3.translate(trans_data)
print(f"Original Data: {t1}\nTranslated Data: {trans1}\n")
print(f"Original Data: {t2}\nTranslated Data: {trans2}\n")
print(f"Original Data: {t3}\nTranslated Data: {trans3}\n")

#spliting a string and returning a tuple
print()
sp1 = "Hello World"
print(f"String: {sp1}")
print(sp1.partition(" "))
sp2 = "Howareyou?"
print(f"String: {sp2}")
print(sp2.partition("are"))

#replacing a substring
print()
t1 = "Hello World!"
print(f"Original String: {t1}")
print("Replaced String:", t1.replace("Hello", "Hi"), end="\n\n")
t2 = "lemons, apples, bananas, apples, apples, cherries"
t3 = t2.replace("apples", "lemons")
print(f"Original Fruits: {t2}")
print("New Fruits:", t2.replace("apples", "lemons"))
print(f"Checking Fruits: {t2}") #proof of the immutable nature of a string
print(f"New Fruits: {t3}")
print(f"Fruits: {t2}")

#returns the highest index of a specified string
print()
hw = "Hello World"
print("Index of H:", hw.rfind('H'))
print("Index of o:", hw.rfind('o'))
print("Index of l:", hw.rfind('l'))

#Accessing the index of the last occurence of a substring in the given string
print()
ri1 = "Java"
ri2 = "Python is fun !!!"
print(f"Last Occurence of 'a': {ri1.rindex('a')}")
print(f"Last Occurence of ' ': {ri2.rindex(' ')}")

#right-justify a string within a specific width by padding it
#with spaces or any specified character.
print()
rj1 = "Python"
rj2 = "Hannah Azaliah"
print(f"Original Text: {rj1}\nPadded Text: {rj1.rjust(10)}") #10 is > Python string
print(f"Original Text: {rj2}\nPadded Text: {rj2.rjust(25, '&')}")

#last occurrence of the specified separator in the string and then
#splits the string into three parts; string before separator, separator, and
#the last string after the separator
print()
message = "Python is easy. Python is fun to learn. Python is a popular programming language."
parts = message.rpartition("Python")    #Python is the separator argument
print(f"Output: {parts}\nType: {type(parts)}")

#finds the last occurrence of a separator in the string and then splits the
#string into specified number of parts based on that separator. 
print()
message = "Python is easy. Python is fun to learn. Python is popular language."
parts = message.rsplit("Python", 2)    #Python is the separator argument
print(f"Output: {parts}\nType: {type(parts)}")

#removing the trailing characters
print()
str1 = "          Learning Python          "
str2 = "-------Learning Python-------"
print(str1, str1.rstrip(" "), sep="\n")
print(str2, str2.rstrip("-"), sep="\n")

#Splits the string from the specified separator and returns a
#list object with string elements
print()
sentence = "I am learning python"
sp = sentence.split('n')
print(f"Actual Sentence: {sentence}\nSplitted Sentence: {sp}\nType: {type(sp)}")

#splitting a string into a list of lines
print()
message = "Learning programming is fun.\nFor you to master programming requires focus\
 and dedication.\nI recommend starts with writting 10,000 lines of code."
print(message)
print(message.splitlines())

#checking if a string starts with a specific substring
print()
print(f"String: {hw}")
print(hw.startswith('e'))
print(hw.startswith('e', 1))
print(hw.startswith("ll", 2))
print(hw.startswith("World", 6))
print(hw.startswith("Wor", 6, 9))

#stripping specified substring or the leading and trailing substring
print()
t1 = "   Python is easy, I think.  "
t2 = "!@#Hannah*&^"
print(f"Original String: {t1}\nStripped String: {t1.strip()}")
print(f"Original String: {t2}\nStripped String: {t2.strip('!@#*&^')}")

#swapping of substring cases
print()
text = "pythonABC"
print(f"Original Text: {text}\nSwapcase Text: {text.swapcase()}")

#returning the uppercase of 1st letter of the string
print()
u_input = input("Enter a phrase: ")
print("Titled Phrase:", u_input.title())

#translate() use with maketrans()


#returns a string in uppercase
print("Uppercase:", u_input.upper(), end="\n\n")

#filling of zero in a string under a specified length
print()
contact = 9301235012
print(f"Contact Number: {contact}")
print(f"Complete Number: {str(contact).zfill(11)}")