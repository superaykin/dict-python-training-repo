# Problem set 13

# Problem Set # 2 - Day 1

# letter P is 16th alphabet
firstNumber = 16
secondNumber = int(input("Enter second no: "))

# add two numbers
addition_result = firstNumber + secondNumber

# get the half value of the second number
firstNumberHalf = firstNumber / 2

# less the result to the half of first number
subtraction_result = addition_result - firstNumberHalf

# multiply result b to the half value of the first number
multiplication_result = subtraction_result * firstNumberHalf

# division
division_result = multiplication_result / firstNumberHalf

# modulo
modulo_result = division_result % firstNumberHalf

# exponents
exponent_result = modulo_result ** firstNumberHalf

# display vars and results
print("First number is:", firstNumber, "and is a", type(firstNumber))
print("Second number is:", secondNumber, "and is a", type(secondNumber))
print ("\n=======\tResults\t=======")
print("Addition:\t\t", addition_result, "\t\t\t\tMemory Address:\t\t", id(addition_result))
print("Subtraction:\t\t", subtraction_result, "\t\t\t\tMemory Address:\t\t", id(subtraction_result))
print("Multiplication:\t\t", multiplication_result, "\t\t\t\tMemory Address:\t\t", id(multiplication_result))
print("Division:\t\t", division_result, "\t\t\t\tMemory Address:\t\t", id(division_result))
print("Modulo:\t\t\t", modulo_result, "\t\t\t\tMemory Address:\t\t", id(modulo_result))
print("Exponent:\t\t", exponent_result, "\t\t\tMemory Address:\t\t", id(exponent_result))

print()

myDict = {id(addition_result) : addition_result,
          id(subtraction_result) : subtraction_result,
          id(multiplication_result) : multiplication_result,
          id(division_result) : division_result,
          id(modulo_result) : modulo_result,
          id(exponent_result) : exponent_result
        }

print(F"Dictionary: {myDict}")