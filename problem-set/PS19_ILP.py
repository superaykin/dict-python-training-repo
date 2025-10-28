# PROBLEM SET [19] - Multiple List of Number Application

num = int(input("Enter a number: "))

myList = [x + 1 for x in range(num) for x in range(5)]
print(F"\nMy List: {myList}")