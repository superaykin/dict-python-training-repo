# Python Simulation 09
# Selection with If

#working with if condition
print()
x = 10
if x<50:
    print("{} is less than 50.".format(x), end="\n\n")

#multiple statements in the if block
quantity = 5
price = 50
if (price*quantity < 500):
    print(f"{price} * {quantity} is less than 500")
    print(f"Price = {price}")
    print(f"Quantity = {quantity}", end="\n\n")

#out of if block execution
import operator
price = 50
quantity = 5

if price*quantity < 100:
    print(f"{price} * {quantity} is less than 500")
    print(f"Price = {price}")
    print(f"Quantity = {quantity}", end="\n\n")

print("{}*{} is".format(price,quantity), operator.mul(price,quantity), \
"and is not less than 100.")

#running through multiple statements
print()
price = 100
if price>100:
    print(f"{price} is greater than 100.")
if price==100:
    print(f"{price} is equal to 100.")
if price<100:
    print(f"{price} is less than 100.")

#if-else condition
print()
age = int(input("Enter age: "))
print(f"You are now {age} years old.")

if age>=18:
    print("You are qualified to vote!")
else:
    print(f"You are still {age} years old and not qualified to vote.")

#working with if-elif
print()
price = int(input("Enter price: "))

if price>100:
    print(f"You entered {price} and is greater than 100.")
elif price==100:
    print(f"The amount you entered, {price}, is the same.")
elif price<100:
    print(f"{price} is less than 100.")
else:
    print(f"{price} is invalid.")

#nested if-elif-else condition
print()
price = 50
quantity = 5
amount = price*quantity #250

if amount>100:
    if amount>500:
        print(f"{amount} is greater than 500.")
    else:
        if ((amount<500) and (amount>400)):             #T and F => F
            print(f"{amount} is between 400 to 500.")
        elif ((amount<500) and (amount>300)):           #T and F => F
            print(f"{amount} is between 300 to 400.")
        else:
            print(f"{amount} is between 200 and 500.")
elif amount==100:
    print(f"{amount} is 100.")
else:
    print(f"{amount} is less than 100.")

#working with string data in if-else statement
print()
username = "jtbojocan"
password = "admin"

uname = input("Enter username: ")
pword = input("Enter password: ")

if ((uname==username) and (pword==password)):
    print(f"Hello {uname}, welcome to Python.")
else:
    print("Invalid user input!")

#working with Ramdom module
print()
import random   #shuffling a list or selecting random elements from a sequence

rand_num = random.randint(1,3)
guessnum = int(input("Enter a guess number [1-3]: "))
print(f"Generated Random Number: {rand_num}")

if (rand_num==guessnum):
    print("Congratulations!!! you've guessed it right!!!")
else:
    print("Try again next time!!!")

#more on random numbers
print()
rand_grade = random.random()
print(f"Random Value = {rand_grade:.2%}")

if (rand_grade >= 0.75):
    print("PASSED!!!")
else:
    print("FAILED!!!")
print()

#ternary operator in python
print()
num = 7
print("Greater than 5." if num>5 else "Smaller than 5.")

language = "python!"
ter_result = "You are learning python" if language=="python" else "!!!!!"
print(f"Result: {ter_result}")

#nested ternary operator
print()
n = 6
res = "python" if n>10 else "java" if n>5 else "keep learning!!!"
print(f"Result: {res}")