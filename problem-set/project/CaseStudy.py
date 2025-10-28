# case-study

import Methods
from datetime import datetime

print('''\n
===========================================
========= BLOOD TYPING SIMULATION =========
===========================================

This program is a simulation of a blood typing...
      
''')

print()
lastname = str(input("Enter lastname: "))
firstname = str(input("Enter firstname: "))
# handle dob
dob = Methods.handleDob()

dobObject = datetime.strptime(dob, "%Y-%m-%d")  # convert string to datetime
today = datetime.today()
age = today.year - dobObject.year
if (today.month, today.day) < (dobObject.month, dobObject.day) :
    age -= 1

print("\n====================================\nPerforming blood extraction...")
# extract blood
bloodSample = Methods.extractBlood(lastname, firstname, dob)

print(F"Patient {lastname.upper()}, {firstname.upper()} Blood sample: {bloodSample}")
print("\n====================================\nPerforming testing...")

result = Methods.identifyBlood(bloodSample)

print("\n====================================\n")

print(F'''
Patient Name: {lastname.upper()}, {firstname.upper()}
Date of Birth: {dobObject.month} {dobObject.day}, {dobObject.year}
Age: {age}

-------------------------------------------------
''')

print(F"Interpretations:\n* Type: {result["REMARKS"]}\n* Result Set{result["RESULTSET"]}")