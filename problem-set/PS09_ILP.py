# Problem Set 9 - Day 3
'''
PROBLEM SET [09] - Rock-Paper-Scissor-Lizard-Spock Game Application

Write a program that simulates the Rock-Paper-Scissor-Lizard-Spock game using if-elif-else statements. Replace the name play with a personalized data or value, e.g. Rock ==> Junell, Paper ==> Surigao, Scissor ==> CSU, etc.
Rules:
[min. of 2 players game]
Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
Rock crushes Scissors

Aliza > Maki
Maki > Diego
Diego > Mingkay
Mingkay > Aykin
Aykin > Aliza
Aliza > Mingkay
Mingkay > Maki
Maki > Aykin
Aykin > Diego
Diego > Aliza
'''

player1 = str(input("Enter Player 1: "))
player2 = str(input("Enter Player 2: "))

print()
choices = ''' ===================================
----------- MOVE CHOICES -----------
====================================
* Aykin
* Aliza
* Maki
* Diego
* Mingkay
====================================
'''

print(choices)
p1input = str(input("Player 1 turn..\nSelect one from choices: "))
p1 = p1input.lower()

print()

p2input = str(input("Player 2 turn..\nSelect one from choices: "))
p2 = p2input.lower()

gamePlay = '''
"aliza" cuts "maki"
"maki" covers "diego"
"diego" crushes "mingkay"
"mingkay" poisons "aykin"
"aykin" smashes "aliza"
"aliza" decapitates "mingkay"
"mingkay" eats "maki"
"maki" disproves "aykin"
"aykin" vaporizes "diego"
"diego" crushes "aliza"
'''

winner = ''
desc = ''

if p1 == "aliza" and p2 == "maki":
    winner = player1
elif p1 == "maki" and p2 == "aliza":
    winner = player2
elif p1 == "maki" and p2 == "diego":
    winner = player1
elif p1 == "diego" and p2 == "maki":
    winner = player2
elif p1 == "diego" and p2 == "mingkay":
    winner = player1
elif p1 == "mingkay" and p2 == "diego":
    winner = player2
elif p1 == "mingkay" and p2 == "aykin":
    winner = player1
elif p1 == "aykin" and p2 == "mingkay":
    winner = player2
elif p1 == "aykin" and p2 == "aliza":
    winner = player1
elif p1 == "aliza" and p2 == "aykin":
    winner = player2
elif p1 == "aliza" and p2 == "mingkay":
    winner = player1
elif p1 == "mingkay" and p2 == "aliza":
    winner = player2
elif p1 == "mingkay" and p2 == "maki":
    winner = player1
elif p1 == "maki" and p2 == "mingkay":
    winner = player2
elif p1 == "maki" and p2 == "aykin":
    winner = player1
elif p1 == "aykin" and p2 == "maki":
    winner = player2
elif p1 == "aykin" and p2 == "diego":
    winner = player1
elif p1 == "diego" and p2 == "aykin":
    winner = player2
elif p1 == "diego" and p2 == "aliza":
    winner = player1
elif p1 == "aliza" and p2 == "diego":
    winner = player2
else :
    winner = "Draw"

winDisplay = ''

if winner == "Draw" :
    winDisplay = "No winners. Draw"
else :
    winDisplay = F"Player \"{winner}\" win."

# identify winner
print()
print("================================")
print(F"{winDisplay}")
print()

print(F"=========== Game Rules =========== \n{gamePlay}")
