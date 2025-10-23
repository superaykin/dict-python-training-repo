''' Problem Set 8 - Day 2

'''

defaultPassKey = 'NV#8dL4j!*KaP9$eJ#4dG8m!B3cH7aK$eM2'
myName = 'Ikenn'
myLastname = 'Palma'

# Birthday slice
bdaySlice = defaultPassKey[:6]
print(F"Birthday Slice: {bdaySlice}")

# iteration
iterName = '$'.join(myName)
print(F"Name Iteration: {iterName}")

# concat
withMyName = bdaySlice + iterName
print(F"Concat item + bday slice: {withMyName}")

# strip lastname
newLastName = myLastname.lstrip(myLastname[0]).rstrip(myLastname[-1])
print(F"New lastname: {newLastName}")

# concat
conWithLastName = withMyName + newLastName
print(F"Concat withname + newlastname: {conWithLastName}")

# birthday slice
bYearSlice = conWithLastName[-35:-2]
print(F"Birthyear Slice: {bYearSlice}")

spc = 10 * ";"

tm = str.maketrans("aAeEiIoOuU", spc)
noVowels = bYearSlice.translate(tm)
print(F"Remove vowels: {noVowels}")


print(F"Final Passcode: {noVowels}")