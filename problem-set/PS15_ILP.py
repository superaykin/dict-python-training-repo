# Problem Set 15

lastName = "PALMA"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# =================================================================================
for eachLetter in lastName :
    letterCount = 1
    for eachChar in alphabet :
        if eachChar == eachLetter :
            print(F"{eachLetter} is number {letterCount}")
            break
        else :
            letterCount += 1
# =================================================================================
print("===============")
# =================================================================================
# convert alphabet into list
alphaList = list(alphabet)
for eachLetter in lastName :
    print(F"{eachLetter} is number {alphaList.index(eachLetter) + 1}")
# =================================================================================

        

