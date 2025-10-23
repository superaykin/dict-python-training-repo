# PROBLEM SET [18] - Calculated Errors Application
from datetime import datetime

print()
print("PROBLEM SET [18] - Calculated Errors Application\n")

def getInput() :
    while True:
        try:
            num1 = int(input("Enter 1st number: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    while True:
        try:
            num2 = int(input("Enter 2nd number: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    return [num1, num2]

def divide(a:int, b:int) :
    try :
        result = a / b
    except ZeroDivisionError :
        print("Unable to divide zero.")
    finally :
        errorLogFile = open("PS18_ILP.txt", "w")
        logDate = datetime.now()
        print(F"{logDate} | Division by zero error.", file=errorLogFile)


numbers = getInput()

# perform arithmetic addition
result = divide(numbers[0], numbers[1])
print("Qoutient is:", result)
