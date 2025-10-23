# Problem Set 17
print()
val = None

# local function variable
def printValue() :
    val = "PYTHON PROGRAMMING"
    print(F"local function value of variable val: {val}")

print(F"First value of variable val: {val}")

# call the variable
print("Calling method...")
printValue()


print('==================================\n')
myGlobalVar = "IKENN"

def myLocalFunction() :
    # change it to something
    global myGlobalVar
    myGlobalVar = 'PYTHON'
    print(F"Variable changed to global and value changed to: {myGlobalVar}")

print(F"Global variable myGlobalVar value: {myGlobalVar}")

print("Call Method...")
# call the method
myLocalFunction()

# print again the global variable
print(F"Outside function printing of Global Var value: {myGlobalVar}")
