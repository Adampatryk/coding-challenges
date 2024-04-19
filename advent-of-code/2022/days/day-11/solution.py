import pathlib


class Monkey:
    def __init__(self,id, items, operation, testDivisibleBy, ifTrueThrowTo, ifFalseThrowTo):
        self.id = id
        self.items = items
        self.operation = operation
        self.testDivisbleBy = testDivisibleBy
        self.ifTrueThrowTo = ifTrueThrowTo
        self.ifFalseThrowTo = ifFalseThrowTo
        self.inspectCount = 0 

    def worryLevelAfterBeingBored(self, old):
        return old // 3

    def inspectItems(self, monkeys):
        lcm = 1
        for monkey in monkeys:
            lcm = lcm * monkey.testDivisbleBy
        numberOfItems = len(self.items)
        for _ in range(numberOfItems):
            self.inspectNextItem(monkeys, lcm)


    def inspectNextItem(self, monkeys, lcm):
        debug = False
        if len(self.items) == 0:
            print(" No items to inspect")
            return
        
        self.inspectCount += 1

        # if debug: print(" Monkey",self.id,"inspects an item with worry level of", self.items[0])
        old = self.items[0]
        new = applyOperation(self.items[0], self.operation) % lcm
        self.items[0] = new
        if debug: print(" Worry level goes from", old, "to", new)
        # self.items[0] = self.worryLevelAfterBeingBored(self.items[0])
        # if debug: print(" Monkey gets bored with item. Worry level divided by 3 to", self.items[0])

        testPassed = self.items[0] % self.testDivisbleBy == 0
        strNot = "" if testPassed else "not"
        if debug: print(" Current worry level is", strNot, "divisible by", self.testDivisbleBy)

        if testPassed: 
            if debug: print(" Item with worry level", self.items[0],"is thrown to monkey", self.ifTrueThrowTo)
            monkeys[self.ifTrueThrowTo].items.append(self.items[0])
            self.items = self.items[1:]
        else:
            if debug: print(" Item with worry level", self.items[0],"is thrown to monkey", self.ifFalseThrowTo)
            monkeys[self.ifFalseThrowTo].items.append(self.items[0])
            self.items = self.items[1:]


def openFile(filename):
    currentPath = pathlib.Path(__file__).parent.resolve()
    filepath = pathlib.Path(currentPath, filename)
    return open(filepath)

def parseMonkeyId(line):
    return int(line[:-1].split(" ")[-1])

def parseMonkeyItems(line):
    numbers = line.split(":")[-1]
    numberList = [int(x.strip()) for x in numbers.split(",")]
    return numberList

def applyOperation(x, expression):
    old = x 
    return eval(expression)

def parseMonkeyOperation(line):
    operationStr = "".join([x.strip() for x in line.split("=")[-1]])
    return operationStr

def parseMonkeyTestDivisibleBy(line):
    return int(line.split(" ")[-1])

def praseMonkeyTrueThrowTo(line):
    return int(line.split(" ")[-1])

def praseMonkeyFalseThrowTo(line):
    return int(line.split(" ")[-1])

def getMonkeys(filename):
    monkeys = []
    file=openFile(filename)
    content = file.read().splitlines()
    for i in range(0, len(content), 7):
        monkeyId = parseMonkeyId(content[i])
        monkeyItems = parseMonkeyItems(content[i+1])
        monkeyOperation = parseMonkeyOperation(content[i+2])
        monkeyTestDivisbleBy = parseMonkeyTestDivisibleBy(content[i+3])
        monkeyTrueThenThrowTo = praseMonkeyTrueThrowTo(content[i+4])
        monkeyFalseThenThrowTo = praseMonkeyFalseThrowTo(content[i+5])
        monkeys.append(Monkey(monkeyId, monkeyItems, monkeyOperation, monkeyTestDivisbleBy, monkeyTrueThenThrowTo, monkeyFalseThenThrowTo))
    return monkeys

def printMonkeyItems(monkeys):
    for monkey in monkeys:
        print("Monkey",monkey.id, ":", monkey.items)

def getMonkeyInspectCounts(monkeys):
    counts = []
    for monkey in monkeys:
        counts.append(monkey.inspectCount)
    return sorted(counts)


#print("Monkey", monkey.id,"inspected",monkey.inspectCount,"items")



def main():
    monkeys = getMonkeys('input.txt')
    for round in range(10000):
        #print("Round",round)
        #printMonkeyItems(monkeys)
        for monkey in monkeys:
            monkey.inspectItems(monkeys)
        
    inspectCounts = getMonkeyInspectCounts(monkeys)
    print(inspectCounts)
    print("Monkey business:", inspectCounts[-1] * inspectCounts[-2])
    
main()
