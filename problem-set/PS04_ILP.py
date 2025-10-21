# Problem Set 4 - Day 2

lname = str(input("Enter your last name: "))
limit = int(input("Enter index: "))

#sliced the lastname
slicedLname = lname[:limit]

print(f"Sliced Lastname: {slicedLname}")

vowels = ['a','A','e','E','i','I','o','O','u','U']

for target in slicedLname :
    result = 'a' if target in vowels else 'not a'
    print(f"{target} is {result} vowel")