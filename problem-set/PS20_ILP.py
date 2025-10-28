# PROBLEM SET [20] - Modules of Problem Set Application

import auth
import filemngr
import calculate

print()
print("Check credentials on db.config file or use admin, python")
print()
userName = str(input("Enter username: "))
password = str(input("Enter password: "))

isAllowed = auth.authenticateUser(userName, password)
if isAllowed :
    print("Authentication success. Welcome!")
else :
    print("Ooopss. Invalid credentials")
    exit()

print()

print('''\n===================================================
Menu:
1 - Calculate Gross
2 - Calculate Total Deductions
3 - Calculate Tax
4 - Calculate Net Income
===================================================
\n''')
answer = int(input("Enter choice: "))
print()
daysOfWork = int(input("Enter days of work: "))

if answer == 1 :
    result = calculate.gross(daysOfWork)
    menu = 'Gross'
elif answer == 2 :
    result = calculate.deduction()
    menu = 'Total Deductions'
elif answer == 3 :
    result = calculate.tax(daysOfWork)
    menu = 'Tax'
else :
    result = calculate.net(daysOfWork)
    menu = 'Net Income'

print(F"Result: {menu} : {result}")
print()
saveData = str(input(F"Do you want to save it to text file? yes or no: "))
if saveData == 'yes' :
    details = F"Result: {menu} : {result}"
    filemngr.logToFile(details)
