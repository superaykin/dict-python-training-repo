# Problem Set # 2 - Day 1

# letter P is 16th alphabet
firstNumber = 16
secondNumber = float(input("Enter second no: "))

# add two numbers
addition_result = firstNumber + secondNumber

# get the half value of the second number
firstNumberHalf = firstNumber / 2

# less the result to the half of first number
subtraction_result = addition_result - firstNumberHalf

# multiply result b to the half value of the first number
multiplication_result = subtraction_result * firstNumberHalf

# division
division_result = subtraction_result / firstNumberHalf

# modulo
modulo_result = subtraction_result % firstNumberHalf

# exponents
exponent_result = subtraction_result ** firstNumberHalf

# display results
print ("\n=======\tResults\t=======")
print("Addition:\t\t", addition_result, "\t\t\t\tMemory Address:\t\t", id(addition_result))
print("Subtraction:\t\t", subtraction_result, "\t\t\t\tMemory Address:\t\t", id(subtraction_result))
print("Multiplication:\t\t", multiplication_result, "\t\t\t\tMemory Address:\t\t", id(multiplication_result))
print("Division:\t\t", division_result, "\t\t\t\tMemory Address:\t\t", id(division_result))
print("Modulo:\t\t\t", modulo_result, "\t\t\t\tMemory Address:\t\t", id(modulo_result))
print("Exponent:\t\t", exponent_result, "\t\tMemory Address:\t\t", id(exponent_result))
print ("\n=======\tEnd of Results\t=======")