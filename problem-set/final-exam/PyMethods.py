def checkWinner(p1:str, p2:str) :
    # combinations and winners
    if p1 == "aliza" and p2 == "maki":
        winner = 1
    elif p1 == "maki" and p2 == "aliza":
        winner = 2
    elif p1 == "maki" and p2 == "diego":
        winner = 1
    elif p1 == "diego" and p2 == "maki":
        winner = 2
    elif p1 == "diego" and p2 == "mingkay":
        winner = 1
    elif p1 == "mingkay" and p2 == "diego":
        winner = 2
    elif p1 == "mingkay" and p2 == "aykin":
        winner = 1
    elif p1 == "aykin" and p2 == "mingkay":
        winner = 2
    elif p1 == "aykin" and p2 == "aliza":
        winner = 1
    elif p1 == "aliza" and p2 == "aykin":
        winner = 2
    elif p1 == "aliza" and p2 == "mingkay":
        winner = 1
    elif p1 == "mingkay" and p2 == "aliza":
        winner = 2
    elif p1 == "mingkay" and p2 == "maki":
        winner = 1
    elif p1 == "maki" and p2 == "mingkay":
        winner = 2
    elif p1 == "maki" and p2 == "aykin":
        winner = 1
    elif p1 == "aykin" and p2 == "maki":
        winner = 2
    elif p1 == "aykin" and p2 == "diego":
        winner = 1
    elif p1 == "diego" and p2 == "aykin":
        winner = 2
    elif p1 == "diego" and p2 == "aliza":
        winner = 1
    elif p1 == "aliza" and p2 == "diego":
        winner = 2
    else :
        winner = 0

    return winner


def printToText(strToPrint) :
    # args {round, winner, total score}
    with open("ScoreBoard.txt", "a") as file:
        file.write(strToPrint + "\n")



