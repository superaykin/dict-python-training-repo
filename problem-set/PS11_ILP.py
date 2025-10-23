# Problem Set 11

words = []
answer = ""

while answer != "palma":
    word = input("Enter a word: ")
    words.append(word)

    answer = input("Do you want to add another word? Type 'IKENN' for Yes or 'PALMA' for No: ")
    answer = answer.strip().lower()

print("\nYour word bank:")
print(words)
