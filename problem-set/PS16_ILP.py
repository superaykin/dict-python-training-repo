# PROBLEM SET [16] 

lastName = "PALMA"

def printAlphaSequence(char) :
    ''' This method print the alphabet character sequence number '''
    alphaList = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print(F"{char} is number {alphaList.index(char) + 1}")

for eachChar in lastName :
    printAlphaSequence(eachChar)


