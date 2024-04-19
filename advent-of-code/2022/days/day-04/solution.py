import pathlib

currentPath = pathlib.Path(__file__).parent.resolve()
filepath = pathlib.Path(currentPath, "input.txt")

def assignmentRangeToList(assignment):
    start, end = assignment.strip().split("-")
    return list(range(int(start),int(end)+1))

def isFullyContained(a, b):
    for item in a:
        if item not in b:
            return False
    return True


def oneOfPairIsFullyContained(pair):
    a, b = pair
    return isFullyContained(a, b) or isFullyContained(b, a)

def pairHasOverlap(pair):
    a, b = pair
    return len(set(a).intersection(set(b))) > 0


#line to []
def lineToRangePair(line):
    pair = line.strip().split(",")
    rangePair = [assignmentRangeToList(assignment) for assignment in pair]
    return rangePair

def part1(f):
    countFullyContianedPairs = 0
    #for each line
    for line in f:
        rangePair = lineToRangePair(line)
        if oneOfPairIsFullyContained(rangePair):
            countFullyContianedPairs += 1
    
    return countFullyContianedPairs

def part2(f):
    countOverlappedPairs = 0
    #for each line
    for line in f:
        rangePair = lineToRangePair(line)
        if pairHasOverlap(rangePair):
            countOverlappedPairs += 1
    
    return countOverlappedPairs 
        
def main():
    f = open(filepath)
    print(part2(f))

main()