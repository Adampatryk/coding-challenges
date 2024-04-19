import pathlib
debug = False


def openFile(filename):
    currentPath = pathlib.Path(__file__).parent.resolve()
    filepath = pathlib.Path(currentPath, filename)
    return open(filepath)

def getNumberFromAddxInstruction(instruction):
    return int(instruction.split(" ")[-1])


def processInstructionStackAsync(x, instructionStack):
    print("before",instructionStack)
    currentInstructions = instructionStack[0]
    instructionStack[0] = instructionStack[1]
    instructionStack[1] = instructionStack[2]
    instructionStack[2] = []
    print("after",instructionStack)


    if len(currentInstructions) == 0:
        return x

    for instruction in currentInstructions:
        if instruction.startswith("addx"):
            numberToAdd = getNumberFromAddxInstruction(instruction)
            if debug: print("adding", numberToAdd)
            return x + numberToAdd
        else:
            return x

def isInterestingSignal(cycle):
    return cycle==20 or (cycle - 20) % 40 == 0

def mainAsync():
    x = 1
    cycle = 0
    instructionStack = [[],[],[]]
    runningSum = 0
    for line in openFile("test.txt"):
        cycle = cycle+1
        if debug: print(" Start of cycle", cycle, "x", x)

        instruction = line.strip()
        if instruction == "noop":
            instructionStack[0].append(line)
        elif instruction.startswith("addx"):
            instructionStack[2].append(instruction)

        x = processInstructionStackAsync(x, instructionStack)

        if debug: print(" End of cycle", cycle, "x", x)

        if isInterestingSignal(cycle):
            print("Cycle", cycle, "adding",x,"to total", runningSum)
            runningSum += x

def getInterestingSignal(x, cycle):
    print("Cycle",cycle,"*",x,"=",x*cycle)
    return  x*cycle

def isSpriteVisible(x, cycle):
    return x == cycle or x == cycle -1 or x == cycle + 1

def main():
    x = 1
    cycle = 1
    xValuesPerCycle = [1]
    file=openFile("input.txt")
    content = file.read().splitlines()
    runningTotal = 0
    for instruction in content:
        if debug: print("Starting cycle", cycle, "x",x)
        if isInterestingSignal(cycle):
            runningTotal += getInterestingSignal(x,cycle)
        if instruction == "noop":
            cycle += 1
            xValuesPerCycle.append(x)
        elif instruction.startswith("addx"):
            if isInterestingSignal(cycle+1): 
                runningTotal += getInterestingSignal(x,cycle+1)
            x += getNumberFromAddxInstruction(instruction)
            xValuesPerCycle.append(x)
            xValuesPerCycle.append(x)
            cycle += 2
        if debug: print("Ending cycle", cycle, "x", x)
    print(runningTotal)
    print(xValuesPerCycle, len(xValuesPerCycle))

main()
