''' Problem Set 8 - Day 2

'''

defaultPassKey = 'G#8dL4j!*KaP9$eJ#4dG8m!B3cH7aK$eM2'
myName = 'Ikenn'
myLastname = 'Palma'

bdaySlice = defaultPassKey[:6]

iterName = '$'.join(myName)

withMyName = bdaySlice + iterName

newLastName = myLastname.lstrip(myLastname[0]).rstrip(myLastname[-1])

conWithLastName = withMyName + newLastName

bYearSlice = conWithLastName[-2:-35]

vowels = 'aeiouAEIOU'

for target in vowels :
    noVowels = bYearSlice.replace(target, '$')

print(noVowels)