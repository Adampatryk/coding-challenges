import pathlib
from enum import Enum
 
currentDir = []
treeMap = {}

TOTAL_SYSTEM_SPACE = 70000000
REQUIRED_FREE_SYSTEM_SPACE = 30000000

class Command(Enum):
    CD = 1
    LS = 2

class Filetype(Enum):
    FILE = 1
    DIR = 2

class Item():
    name = "",
    size = 0
    filetype = Filetype.FILE
    def __init__(self, name, size, filetype):
        self.name = name
        self.size = size
        self.filetype = filetype

def openFile(filename):
    currentPath = pathlib.Path(__file__).parent.resolve()
    filepath = pathlib.Path(currentPath, filename)
    return open(filepath)

def getLines(filename):
    lines = []
    for line in openFile(filename):
        lines.append(line.strip())
    return lines
        
def isCommand(line):
    return line[0] == "$"

def isDir(line):
    return line.split(" ")[0] == "dir"

def isFile(line):
    return line.split(" ")[0].isnumeric()

def getCommandString(line):
    return line.split(" ")[1].strip().lower()

def currentDirStr():
    return '/'.join(currentDir)

def getCommand(line):
    commandString = getCommandString(line)
    if commandString == "cd":
        return Command.CD
    elif commandString == "ls":
        return Command.LS
    else:
        raise Exception(commandString + " is not a command")

def getCdParam(line):
    return line.split(" ")[2].strip().lower()

def cd(dirParam):
    if dirParam == "..":
        print("* Going up a directory *")
        currentDir.pop()
    else:
        print("* Changing to", dirParam, "*")
        currentDir.append(dirParam)
        if currentDirStr() not in treeMap:
            treeMap[currentDirStr()] = []

def executeCommand(line):
    if getCommand(line) == Command.CD:
        dirParam = getCdParam(line)
        cd(dirParam)

def printFile(file):
    print(f'- {file.name} (file, size={file.size})')

def printDir(file):
    print( f'- {file.name} (dir)')

def printTree():
    for dir in treeMap:
        print(dir, "(dir)")
        for item in treeMap[dir]:
            if item.filetype == Filetype.DIR:
                printDir(item)
            else:
                printFile(item)

def getDirSize(dir):
    totalSize = 0
    for item in treeMap[dir]:
        if item.filetype == Filetype.FILE:
            totalSize += item.size
        elif item.filetype == Filetype.DIR:
            pathname = dir + "/" + item.name
            totalSize += getDirSize(pathname)
    return totalSize

def addFileToTree(line):
    size, name = line.split(" ")
    size = int(size)
    treeMap[currentDirStr()].append(Item(name, size, Filetype.FILE))

def addDirToTree(line):
    size = 0
    name = line.split(" ")[1]
    treeMap[currentDirStr()].append(Item(name, size, Filetype.DIR))

def getTotalDirSizesWithUpperLimit(upperLimit):
    total = 0
    dirSizes = [getDirSize(dir) for dir in treeMap.keys()]
    
    for dirSize in dirSizes:
        if dirSize < upperLimit:
            total += dirSize
    
    return total

def getUnusedSpace():
    return TOTAL_SYSTEM_SPACE - getDirSize("/")

def findSmallestDirSizeAboveSize(minimum):
    dirSizes = []
    for dir in treeMap.keys():
        dirSizes.append(getDirSize(dir))
    dirSizes = sorted(dirSizes)
    for size in dirSizes:
        if size > minimum:
            return size

def main():
    lines = getLines('input.txt')
    for line in lines:
        if isDir(line):
            print("Dir", line)
            addDirToTree(line)
        elif isFile(line):
            print("File", line)
            addFileToTree(line)
        elif isCommand(line):
            print("Command", line)
            executeCommand(line)
        print(" -", currentDir)
    print()
    printTree()
    print()
    print(treeMap.keys())
    print()
    print("Getting total dir sizes under 100,000")
    print(getTotalDirSizesWithUpperLimit(100000))
    print()
    print("Total space:", TOTAL_SYSTEM_SPACE)
    print("Used space:", getDirSize("/"))
    print("Unused space:", getUnusedSpace())
    print("Required unused space:", REQUIRED_FREE_SYSTEM_SPACE)
    needToFreeUp = REQUIRED_FREE_SYSTEM_SPACE-getUnusedSpace()
    print("Need to free up at least:", needToFreeUp)
    smallestDirSizeAboveSize = findSmallestDirSizeAboveSize(needToFreeUp)
    print("Found dir with size:",smallestDirSizeAboveSize)
    


main()
