# Python Simulation Day 01
# Python General Syntax

#print() display text or values to console terminal with comma separated objects
print("Hello World!")
print("Employee ID:", 912)
print("First Name:", "Junell")
print("Second Name:", "Bojocan")

#calling argument-less print() resulting in a blank line output
print()
print()

#splitting a long line of code into multiple lines treated as single statement
print("I am learning python programming!!! \
Python is fun and easy to learn.")

#breaking code statement into multiple code lines for readability using \
print()
if (100>99) and \
   (200<=500) and \
   (True!=False):
    print("That's nice!")

#using semicolon ; to separate statements in a single code line
print()
print("num1 =", 2); print("num2 =", 21); print("num3 =", 8)

#populating data collection over multiple lines for readability
print()
myNumList = [1, 2, 3,
             4, 5, 6,
             7, 8, 9,
             10]
print(myNumList, type(myNumList), sep="\t")

print()
myItems = ("MacBook Air", "Iphone 8+",
           "Technopack", "Umbrella")
print(myItems, type(myItems), sep="\t")

#python indentation with if statement
print()
if (10>5):
    print("This is a code block.")
    print("10 is greater than 5.")
    print("Checking if 20 is greater than 10.")
    if (20>10):
        print("Another level of code block.")
        print("That is correct!")
else:
    print("10 is less than 5.")

#python indentation with function statement
print()
def your_name(name):
    print("Start of a function block.")
    print("Hello", name)
    print("Welcome to python programming essentials!!!")

your_name("Junell")
print()
your_name("Maria Rosario")

#working with comments
print()
print("Comments are use to label code statements or blocks.")
print("Use the # to denote a comment.") #this here is a comment

#working with multi-line comments
"""
In python, there is no provision to write multi-line
comments, or a block comment. A triple quoted multi-line string
is also treated as a comment if it is not a docstring of the
function or the class.
"""

print() #this is an inline comment
"""
this is a type of spanning multi-line
comment enclosed in a tripled pairing
of double quotes 
"""
'''
this is another type of spanning multi-line
comment enclosed of a tripled pairing of
single quotes
'''

#docstrings stored as an attribute accessed programmatically
print()
def myDocFunction():
    """this is an example of a docstrings."""
    return
#accessing docstring using the __doc__ attribute
print(myDocFunction.__doc__)
#help(myDocFunction)    #accessing the details of function using help()

#more on the docstring the help function
print()
def message(name, greetings="Welcome to python"):
    """
        printing of greetings to the user names
        the greetings here has an initial string data.
    """
    print("{} {}.".format(greetings, name))

message("Junell")
print(message.__doc__)

#docstring syntax conventions
print()
def learning(name, message):
    """This function prints the name and a message.
    
    Arguments:
    name: the name of the person
    message: text message for the person
    """
    print(f"Hello {name}, {message}.")
    
print(learning.__doc__)
learning("Junell", "you are learning python")
learning("Maria", "python is fun to learn")

#Sphinx formatting of a docstring
print()
def favFruits(name, fruit, quantity):
    """This function prints a person's favorite fruit.
    
    :param name: the name of the person
    :type name: str
    :param fruit: the favorite fruit of the person
    :type name: str
    :param quantity: the number of fruits eaten by the person
    :type name: int
    """
    print(f"{name} likes to eat {quantity} {fruit}.")

print(favFruits.__doc__)
favFruits("Hannah", "Mango", 3)
favFruits("Elisha", "Grapes", 2)

#Google Python Style Guide formatting of a docstring
print()
def myBDay(name, month, day, year):
    """This function prints the birthday details of a person.
    
    Args:
        name: the name of the person
        month: the birthday month
        day: the day of birth
        year: the birth year

    Returns:
        A birthday details.
    """
    birth = f"{name} birthdate is on {day}:{month}:{year}."
    return birth

print(myBDay.__doc__)
print(myBDay("Junell", 6, 24, 1987))

#the print() function for display and more...
print()
name = "Junell"
print(name)         #calling the name variable to display its data
age=35
print(name, age)    #calling multiple variable to display data
print("\nName:", name, "\nAge:", age)   #printing objects data w/ descriptor
print(f"My name is {name}, and I am {age} years old.")

#content control display under the print() function
print("\nI am learning python programming essentials.")
print("\nI \nam \nlearning \npython \nprogramming \nessentials.\n")
print("A text apart?")
print("A \ttext \tapart \tindeed!")

#treating escape sequences as literal characters
print()
print("c:\some_file\name")
print(r"c:\some_file\name")

#working with other parameters under the print() function
print()
print("I am", name, "python is new to me.")
print("I am", name, "python is new to me.", sep="-->", end="\n\n")
print("I am", name, "python is new to me.", sep="_____", end="\n\n")


#multiple variable data calls to be printed
print("", "PERSONAL PROFILE", sep="\t", end="\n\n")
c_name = "Junell T. Bojocan"
gender = "Male"
age = 38
mob_num = 12312412313
print("Name:", c_name, sep="\t\t", end="\n\n")
print("Gender:", gender, sep="\t\t", end="\n\n")
print("Age:", age, sep="\t\t", end="\n\n")
print("Mobile Number:", mob_num, sep="\t", end="\n\n")

#displaying output data into a text file with the print() function
text_print = open("sample.txt", "w")                #opens file in write mode
print("Good morning everyone! Ayaw bah!!!", file=text_print)    #printing to specified file parameter
text_print.close()

content = "Tingpaniudto na karon!!!"
text_print2 = open("sample2.txt", "w")
print("Hi, I am\n", c_name, "and I am", \
      age, "years old.", content, sep=" ", \
      file=text_print2)
text_print2.close()