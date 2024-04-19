import pathlib

currentPath = pathlib.Path(__file__).parent.resolve()
filepath = pathlib.Path(currentPath, "input.txt")

#open file
f = open(filepath)

opponentOptionPoints = {
    "A": 1, #opponent rock
    "B": 2, #opponent paper
    "C": 3, #opponent scissors
}

yourOptionPoints = {
    "X": 1, #you rock
    "Y": 2, #you paper
    "Z": 3  #you scissors
}

#"opponentHand yourHand" 
# 1 is a win to you
# 0 is a draw
# -1 is a loss to you
yourHandWins = {
    "A X": 0,   #rock rock
    "A Y": 1,   #rock paper
    "A Z": -1,  #rock scissors
    "B X": -1,  #paper rock
    "B Y": 0,   #paper paper
    "B Z": 1,   #paper scissors
    "C X": 1,   #scissors rock
    "C Y": -1,  #scissors paper
    "C Z": 0,   #scissors scissors
}

def getPointsFromHands(yourHand, opponentHand):
    code = " ".join([opponentHand, yourHand])

    resultCode = yourHandWins[code]

    if resultCode == 1: #you win
        return 6
    elif resultCode == 0: #draw
        return 3
    elif resultCode == -1: #you lose
        return 0

    print("Something went wrong")
    return 0

def getRockPaperScissorsResult(yourHand, opponentHand):
    #determine what score you get for picking the hand you picked
    yourScore = yourOptionPoints[yourHand] 

    #determine who wins and add points
    pointsFromHand = getPointsFromHands(yourHand, opponentHand)

    yourScore += pointsFromHand
    return yourScore

totalScore = 0

#for each line
for line in f:
    opponentHand, yourHand = [hand.strip() for hand in line.split(" ")]
    pointsForThisGame = getRockPaperScissorsResult(yourHand, opponentHand)
    print(pointsForThisGame)
    totalScore += pointsForThisGame

print(totalScore)