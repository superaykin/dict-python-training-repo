# Problem Set 10

print("SET A:\n")
numList = [5, -5, 15, -15, -20, 6, -2, -3, -10, -100]

originalSum = 0
newNumList = []
newListSum = 0

i = 0
while i <= len(numList) - 1 :
    # sum up originals
    originalSum += numList[i]

    # check number if negative and add to list
    if numList[i] < 0 :
        newNumList.append(0)
    else :
        newNumList.append(numList[i])
        # perform addition
        newListSum += numList[i]

    # increment index
    i += 1


print(F"Original List: {numList} | Total: {originalSum}")
print(F"Original List: {newNumList} | Total: {newListSum}")

print()

print("SET B:\n")

prog_language = ["Python", "C++", "C", "PHP", ".NET", "Java", "Flask", "DJango"]

userInput = str(input("Enter programming language: "))
cleanStr = userInput.strip().lower()

i = 0
found = False

while i <= len(prog_language) - 1 :
    if cleanStr == prog_language[i].lower() :
        print(F"{prog_language[i]} - index: {i}")
        found = True
        break
    else :
        i += 1

if not found :
    print(F"Nothing found with the keyword \"{userInput}\"")