# Problem Set 5 - Day 2

import datetime

textFile = open("PS05_ILP.txt", "w")

f_CDate = datetime.date.today()
day1 = datetime.date(2023,1,1)
day2 = datetime.date(2022,8,6)
day3 = datetime.date(2023,2,6)
day4 = datetime.date(2023,10,17)
day5 = datetime.date(2025,8,5)

object1 = str(input("Enter your top 5 objects: "))
object2 = str(input("Enter your top 4 objects: "))
object3 = str(input("Enter your top 3 objects: "))
object4 = str(input("Enter your top 2 objects: "))
object5 = str(input("Enter your top 1 objects: "))


hobby1 = str(input("Enter hobby or interest: "))
hobby2 = str(input("Enter hobby or interest: "))
hobby3 = str(input("Enter hobby or interest: "))

objectSet = {object1, object2, object3, object4, object5}
hobbySet = {hobby1, hobby2, hobby3}

print()

narrative = F'''
My favorite objects are {object1}, {object2}, {object3}, {object4}, and {object5}. \
I stored the objects individually using the type {type(object1)}.
The interest and hobbies are also stored individually using {type(hobby1)}.
I also stored them using the {type(objectSet)} datatype which looks like {objectSet} and {hobbySet} \
I think i have purchased the {object1} around {day1.strftime("%B %d of year %Y")}. A recent interest/hobby of mine is {hobby3} \
which started around {day5.strftime("%B of %Y")}.\n\n
The paragraph above is composed of 6 sentences.
'''

# Print on file
print(narrative, file=textFile)
# Print on console/terminal
print(narrative)