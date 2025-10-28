# Problem Set 9 - Day 3
import PyMethods

maxRounds = 5
gameRound = 1 #inital game round

gameType = 0
while True:
    try:
        gameType = int(input("Game Types:\n* Enter 1 for 1 Player\n* Enter 2 for 2 Players.\nEnter selection: "))
        if gameType not in range(1, 3):
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please try again.")
    
    finally :
        if gameType == 1 :
            print("\nPlayer VS BOT selected...")
        else :
            print("\nPlayer 1 vs Player 2 selected...")

        print("------")


# ask player names
player1 = str(input("Enter Player 1 name: "))

if gameType == 1 :
    player2 = 'GAME BOOOOT'
else :
    player2 = str(input("Enter Player 2 name: "))

# initialize scores
p1Score = 0
p2Score = 0

print()
print("*********** GAME START **************\n")
choices = '''====================================
----------- CHOICES -----------
-- Aykin, Aliza, Maki, Diego, Mingkay --
====================================
'''

choiceList = ['aliza', 'aykin', 'maki', 'diego', 'mingkay']

# print initial print header
PyMethods.printToText(">> GAME START")

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
    winner = PyMethods.checkWinner(p1, p2)

    roundWinner = ''
    winnerLabel = 'DRAW'
    # draw scores
    if winner == 0 :
        print(F"Result: Draw")
        print(F"Result: Round {gameRound} is a draw!")
    else :
        if winner == 1 :
            p1Score += 1
            roundWinner = player1
            
            
        elif winner == 2 :
            p2Score += 1
            roundWinner = player2

        print(F"Result: Round {gameRound} - {roundWinner} wins.")
        winnerLabel = roundWinner

    # check current scores
    sb = F'''
    ========== SCORE BOARD ===========
    Round: {gameRound} \t\t Winner: {winnerLabel}
    Player "{player1}" : {p1Score}
    Player "{player2}" : {p2Score}
    ==================================
    '''
    PyMethods.printToText(sb)

    if p1Score >= 3 :
        #print(F"Game Over. Player {player1} wins.")
        break
    elif p2Score >= 3 :
        #print(F"Game Over. Player {player2} wins.")
        break
    else :

        if gameRound < maxRounds :
            # display scoreboard
            print(sb)
            
        # else do nothing
    
    if gameRound < 5 :
        gameRound += 1
    else :
        break
    # else do noting


print(F'''\n
                ========== FINAL SCORE BOARD ===========
                Round: {gameRound}\n
                Player "{player1}" : {p1Score}\n
                Player "{player2}" : {p2Score}\n
                ==================================
            ''')
# end of 5 rounds identify winner
finalResult = "End of rounds."

if p1Score > p2Score :
    finalResult += " Winner is " + player1
elif p2Score > p1Score :
    finalResult += " Winner is " + player2
else :
    finalResult += " Game is Draw!!!"

# print text
PyMethods.printToText('--- ' + finalResult + ' ----')
PyMethods.printToText("<< GAME END\n\n")