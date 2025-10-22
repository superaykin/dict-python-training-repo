# Python Simulation 05
# Output Formatting and Datetime

#string format() and the {} placeholder
print()
message = "The price of that shirt is only {price:.2f} pesos."
print(message.format(price=745))

#multiple strings utilizing the format() within the declaration
print()
m1 = "Hi!, I'm {name}, and I am {age} years old.".format(name="Junell", age="38")
print(m1)       #defining the variable with the format()

m2 = "My name is {1}, and I am {0} years old.".format(38, "Maria")
print(m2)       #defining the index with specific sequence

m3 = "I like {}, {}, {}, and watching {} tv-series."
print(m3.format("Apple", "Mango", "Grapes", "The Big Bang Theory"))
        #defining sequence based on the literal value arrangement inside format()

#formatting string with alignment specifier
print()
fs1 = "I will be watching {:<9} movies tonight." 
print(fs1.format(5))    #value 5 is left-aligned within a 9-character wide space
fs2 = "I will be singing {:>4} songs at the karaoke bar."
print(fs2.format(2))

#formatting string with percentage formatted values
print()
score1 = "You scored {:%}.".format(0.37)
print(score1)
score2 = "You scored {:.2%}."
print(score2.format(0.81), end="\n\n")

#formatted string literal using f-string
print()
name = "Junell T. Bojocan"
age = 38
status = "Married"
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Status: {status}")
print(f"I will be {age+2} years old two years from now.")
#print(f"Inputted Text:{input("Enter a text: ")}")

#working with datetime class module
print()
import datetime     #importing python's built-in datetime module

today = datetime.date.today()       #creating a date object
print(f"Today is {today}.")
bdate = datetime.date(1987,6,24)    #specifying year, month, day parameter
print(f"I was born on {bdate}.")    #referencing the entire bdate object
print(f"\nBirth Year: {bdate.year}")    #accessing year parameter of bdate object
print(f"Birth Month: {bdate.month}")
print(f"Birth Day: {bdate.day}")

#formatting datetime with string format time method / strftime()
print()
elishas_bdate = datetime.date(2023,8,17)
print(f"Elisha's Birthday: {elishas_bdate}")

format_e_bdate = elishas_bdate.strftime("%B %d, %Y")
print(f"\nElisha is born on {format_e_bdate}.")

#more on datetime formatting and basic datetime calculation
print()
f_today = datetime.date.today().strftime("%dst day of %B, %Y.")
print(f"Today is the {f_today}")
Christmas = datetime.date(2025,12,25)
f_CDate = Christmas.strftime("The %dth day of %B %Y")
print("{} is Christmas day.".format(f_CDate))

print()
this_day = datetime.date.today()
days_left = (Christmas - this_day).days

print(f"There are only {days_left} days left before Christmas.")

#calculating the number of months and days and years with a birthday
print()
date_today = datetime.date.today()
print(date_today)
dt1 = datetime.date.today().strftime("%Y")
print(dt1, type(dt1), sep="\t")
dt2 = datetime.date.today().strftime("%B")
print(dt2, type(dt2), sep="\t")
dt3 = datetime.date.today().strftime("%d")
print(dt3, type(dt3), sep="\t")

my_bday = datetime.date(1987,6,24)
calc_year = date_today.year - my_bday.year
calc_month = abs(date_today.month - my_bday.month)
calc_day = abs(date_today.day - my_bday.day)
print()
print(calc_year, type(calc_year))
print(calc_month, type(calc_month))
print(calc_day, type(calc_day))
print(f"I am {calc_year} years, {calc_month} months, and {calc_day} days old.")

#working with simple date arithmetic
print()
#import datetime                        #importing datetime module
#from datetime import date, timedelta   #importing timedelta and date class

today = datetime.date.today()
print(f"Today is {today}.")

#calculating time intervals with timedelta class
yesterday = today - datetime.timedelta(days=1)
print(f"Yesterday was {yesterday}.")
five_days_ago = yesterday - datetime.timedelta(days=4)
print(f"Five days ago was {five_days_ago}.")

print()
tomorrow = today + datetime.timedelta(days=1)
print(f"Tomorrow is {tomorrow}.")
print(f"Datetime between tomorrow and yesterday is {(tomorrow-yesterday)}.")

#more on timedelta class arguments
print()
from datetime import timedelta

# Creating timedelta objects with different arguments
dur1 = timedelta(days=18, hours=14)
dur2 = timedelta(hours=6, minutes=35, seconds=15)

print(f"Duration Details (Days/Hours): {dur1}\tType{type(dur1)}")
# Represents a duration of 18 days and 14 hours
print(f"Duration Details (Hours/Minutes/Secods): {dur2}\tType{type(dur2)}")
# Represents a duration of 6 hours, 35 minutes, and 15 seconds