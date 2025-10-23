# Problem Set 9 - Day 3

maxRounds = 5
gameRound = 1

gameType = int(input("Game Types:\n* Enter 1 for 1 Player\n* Enter 2 for 2 Players.\nEnter selection: "))
if gameType != 1 and gameType != 2 :
    print("Invalid game type")


# ask player names
player1 = str(input("Enter Player 1 name: "))

if gameType == 1 :
    player2 = 'GAME BOOOOT'
else :
    player2 = str(input("Enter Player 2 name: "))

p1Score = 0
p2Score = 0

print()

choices = ''' ===================================
----------- CHOICES -----------
-- Aykin, Aliza, Maki, Diego, Mingkay --
====================================
'''

choiceList = ['aliza', 'aykin', 'maki', 'diego', 'mingkay']

while gameRound <= maxRounds :
    # print choices
    print(choices)
    print(F"Round {gameRound} -------------")

    player1Input = 0
    while player1Input == 0 :
        p1 = str(input("Player 1 turn..\nSelect one from choices: ")).lower().rstrip(' ').lstrip(' ')
        if p1 in choiceList :
            player1Input = 1
            break
        else :
            print("Invalid choice... please try again")

    print()

    # exclusive for two players
    if gameType == 2 :
        player2Input = 0
        while player2Input == 0 :
            p2 = str(input("Player 2 turn..\nSelect one from choices: ")).lower().rstrip(' ').lstrip(' ')
            if p2 in choiceList :
                player2Input = 1
                break
            else :
                print("Invalid choice... please try again")

    else :
        import random
        p2 = random.choice(choiceList)
        print(F"Bot choose: {p2}")

    # check winner
    if p1 == "aliza" and p2 == "maki":
        winner = player1
        p1Score += 1
    elif p1 == "maki" and p2 == "aliza":
        winner = player2
        p2Score += 1
    elif p1 == "maki" and p2 == "diego":
        winner = player1
        p1Score += 1
    elif p1 == "diego" and p2 == "maki":
        winner = player2
        p2Score += 1
    elif p1 == "diego" and p2 == "mingkay":
        winner = player1
        p1Score += 1
    elif p1 == "mingkay" and p2 == "diego":
        winner = player2
        p2Score += 1
    elif p1 == "mingkay" and p2 == "aykin":
        winner = player1
        p1Score += 1
    elif p1 == "aykin" and p2 == "mingkay":
        winner = player2
        p2Score += 1
    elif p1 == "aykin" and p2 == "aliza":
        winner = player1
        p1Score += 1
    elif p1 == "aliza" and p2 == "aykin":
        winner = player2
        p2Score += 1
    elif p1 == "aliza" and p2 == "mingkay":
        winner = player1
        p1Score += 1
    elif p1 == "mingkay" and p2 == "aliza":
        winner = player2
        p2Score += 1
    elif p1 == "mingkay" and p2 == "maki":
        winner = player1
        p1Score += 1
    elif p1 == "maki" and p2 == "mingkay":
        winner = player2
        p2Score += 1
    elif p1 == "maki" and p2 == "aykin":
        winner = player1
        p1Score += 1
    elif p1 == "aykin" and p2 == "maki":
        winner = player2
        p2Score += 1
    elif p1 == "aykin" and p2 == "diego":
        winner = player1
        p1Score += 1
    elif p1 == "diego" and p2 == "aykin":
        winner = player2
        p2Score += 1
    elif p1 == "diego" and p2 == "aliza":
        winner = player1
        p1Score += 1
    elif p1 == "aliza" and p2 == "diego":
        winner = player2
        p2Score += 1
    else :
        winner = "Draw"


    if winner == "Draw" :
        print(F"Result: Draw")
    else :
        print(F"Result: {winner} wins.")

    if p1Score >= 3 :
        print(F"Game Over. Player {player1} wins.")
        break
    elif p2Score >= 3 :
        print(F"Game Over. Player {player2} wins.")
        break
    else :

        if gameRound <= 4 :
            # display scoreboard
            print(F'''
                ========== SCORE BOARD ===========
                Round: {gameRound}\n
                Player "{player1}" : {p1Score}\n
                Player "{player2}" : {p2Score}\n
                ==================================
            ''')
        # else do nothing
    
    gameRound += 1


print(F'''"\n
                ========== SCORE BOARD ===========
                Round: {gameRound}\n
                Player "{player1}" : {p1Score}\n
                Player "{player2}" : {p2Score}\n
                ==================================
            ''')
# end of 5 rounds identify winner
finalResult = player1 if p1Score > p2Score else player2 if p1Score < p2Score else 'DRAW!!!' 
print(F"End of rounds. Winner is {finalResult}")