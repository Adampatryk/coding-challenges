import pathlib

currentPath = pathlib.Path(__file__).parent.resolve()
filepath = pathlib.Path(currentPath, "input.txt")

#open file
f = open(filepath)

optionPoints = {
    "A": 1, #opponent rock
    "B": 2, #opponent paper
    "C": 3, #opponent scissors
}

instructionCodes = {
    "X": -1, #you need to lose
    "Y": 0, #you need to draw
    "Z": 1  #you need to win
}


#"opponentHand yourHand" 
# 1 is a win to you
# 0 is a draw
# -1 is a loss to you
yourHandWins = {
    "A A": 0,   #rock rock
    "A B": 1,   #rock paper
    "A C": -1,  #rock scissors
    "B A": -1,  #paper rock
    "B B": 0,   #paper paper
    "B C": 1,   #paper scissors
    "C A": 1,   #scissors rock
    "C B": -1,  #scissors paper
    "C C": 0,   #scissors scissors
}

scenarios = {
    "A X": "C",   #rock lose
    "A Y": "A",   #rock draw
    "A Z": "B",  #rock win
    "B X": "A",  #paper lose
    "B Y": "B",   #paper draw
    "B Z": "C",   #paper win
    "C X": "B",   #scissors lose
    "C Y": "C",  #scissors draw
    "C Z": "A",   #scissors win
}

def findHandToPlay(instruction, opponentHand):
    code = " ".join([opponentHand, instruction])
    return scenarios[code]

def getPointsFromHands(yourHand, opponentHand):
    code = " ".join([opponentHand, yourHand])

    resultCode = yourHandWins[code]

    if resultCode == 1: #you win
        return 6
    elif resultCode == 0: #draw
        return 3
    elif resultCode == -1: #you lose
        return 0

def getRockPaperScissorsResult(instruction, opponentHand):
    #determine what hand you need to play
    yourHand = findHandToPlay(instruction, opponentHand)
    yourScore = optionPoints[yourHand] 

    #determine who wins and add points
    pointsFromHand = getPointsFromHands(yourHand, opponentHand)

    yourScore += pointsFromHand
    return yourScore

totalScore = 0

#for each line
for line in f:
    opponentHand, instruction = [hand.strip() for hand in line.split(" ")]
    pointsForThisGame = getRockPaperScissorsResult(instruction, opponentHand)

    totalScore += pointsForThisGame

print(totalScore)