''' Problem Set 7 - Day 2
PROBLEM SET [07] - Stringing Method (Free Format Application)

Develop a python script that exemplifies at least seven (7) distinct string methods. 
Utilize personalized information within the data inputs or variable data.
It is important that these methods exhibit an interdependent operation, 
illustrating their connection and sequential execution. 
Alongside your code, include a detailed description of the application’s purpose and functionality.
'''

print('===== STRING METHODS =====')
print()

string = "I'm Ikenn Louie. I'm at DICT office for Python Programming Essentials Training"

print(f"Original String: {string}")
print()

print("1. isupper()")
print("Description: Returns True if all characters are uppercase and False even if one character is not in uppercase.")
print("Result:")
print(string.isupper())
print()

print("2. lower()")
print("Description: Returns the copy of the original string wherein all the characters are converted to lowercase.")
print("Result:")
print(string.lower())
print()

print("3. upper()")
print("Description: Returns a string in the upper case. Symbols and numbers remain unaffected.")
print("Result:")
print(string.upper())
print()

print("4. startswith()")
print("Description: Returns True if a string starts with the specified prefix. If not, it returns False.")
print("Result:")
print(f"String starts with \"T\"", {string.startswith("T")}, sep="=====> result:")
print(f"String starts with \"Python\"", {string.startswith("Python")}, sep="=====> result:")
print()

print("5. rstrip()")
print("Description: Returns a copy of the string by removing the trailing characters specified as argument.")
print("Result:")
print(string.rstrip("Training"))
print()

print("6. swapcase()")
print("Description: Returns a copy of the string with uppercase characters converted to lowercase and vice versa. Symbols and letters are ignored.")
print("Result:")
print(string.swapcase())
print()

print("7. split()")
print("Description: Splits the string from the specified separator and returns a list object with string elements.")
print("Result:")
print(string.split())
print()