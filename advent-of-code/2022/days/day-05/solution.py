import pathlib

def openFile(filename):
    currentPath = pathlib.Path(__file__).parent.resolve()
    filepath = pathlib.Path(currentPath, filename)
    return open(filepath)

def splitRawInputToStacksAndInstructions(filename):
    f = openFile(filename)

    stackLines = []
    instructionLines = []

    lineType = "stack"
    for line in f:
        if (line.strip() == "" and len(stackLines) > 0):
            lineType = "instruction"
        elif (lineType == "stack"):
            stackLines.append(line)
        else:
            instructionLines.append(line.strip())

    return stackLines, instructionLines

def initialiseStacksArray(lastStackLine):
    numberOfStacks = len(lastStackLine)//4

    stacks = []
    for _ in range(numberOfStacks):
        stacks.append([])
    return stacks

def parseStackLinesToLists(stackLines):
    
    stacks = initialiseStacksArray(stackLines[-1])

    for line in reversed(stackLines[:-1]):
        stackIndex = 0
        for i in range(1, len(line), 4):
            container = line[i]
            if (container.strip() != ""):
                stacks[stackIndex].append(container)

            stackIndex += 1
    return stacks

def getHeightOfStacks(stacks):
    maxHeight = 0
    for stack in stacks:
        if (len(stack) > maxHeight):
            maxHeight = len(stack)
    return maxHeight

def printStacks(stacks): 
    height = getHeightOfStacks(stacks)
    for currentHeight in range(height, 0, -1):
        for stack in stacks:
            if (len(stack) >= currentHeight):
                print("[" + stack[currentHeight-1] + "]", end=" ")
            else:
                print("   ", end=" ")
        print()
    for stackNumber in range(1, len(stacks)+ 1):
        print(" " + str(stackNumber) + " ", end=" ")
    print()
    print()
    
def parseInstruction(instructionText):
    instructionTokens = instructionText.split(" ")
    numberOfThingsToMove = int(instructionTokens[1])
    fromStack = int(instructionTokens[3]) -1
    toStack = int(instructionTokens[5]) -1
    return numberOfThingsToMove, fromStack, toStack
    
def applyInstructionToStacksWithCrateMover9000(numberOfThingsToMove, fromStack, toStack, stacks):
    for i in range(numberOfThingsToMove):
        container = stacks[fromStack].pop()
        stacks[toStack].append(container)
    
    return stacks

def applyInstructionToStacksWithCrateMover9001(numberOfThingsToMove, fromStack, toStack, stacks):
    containersMoving = reversed([stacks[fromStack].pop() for x in range(numberOfThingsToMove)])
    stacks[toStack] += containersMoving
    
    return stacks

def parseAndApplyInstruction(instruction, stacks):
    numberOfThingsToMove, fromStack, toStack = parseInstruction(instruction)
    stacks = applyInstructionToStacksWithCrateMover9001(numberOfThingsToMove, fromStack, toStack, stacks)
    return stacks
    

def applyInstructions(instructionLines, stacks):
    for instruction in instructionLines:
        parseAndApplyInstruction(instruction, stacks)
    return stacks

def printTopContainers(stacks):
    message = ""
    for stack in stacks:
        message += stack[len(stack)-1]
    print(message)

def main():
    stackLines, instructionLines = splitRawInputToStacksAndInstructions("input.txt")
    stacks = parseStackLinesToLists(stackLines)
    printStacks(stacks)

    stacksAfterInstructions = applyInstructions(instructionLines, stacks)
    printStacks(stacksAfterInstructions)

    printTopContainers(stacks)

main()