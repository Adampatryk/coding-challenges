import pathlib

def openFile(filename):
    currentPath = pathlib.Path(__file__).parent.resolve()
    filepath = pathlib.Path(currentPath, filename)
    return open(filepath)

def getDataStream(filename):
    return openFile(filename).readline()

def checkUnique(marker):
    return len(set(marker)) == len(marker)

def findMarker(datastream, requiredUniqueChars):
    
    startIndex = 0
    marker = datastream[startIndex:startIndex+requiredUniqueChars]

    while not checkUnique(marker):
        startIndex += 1
        marker = datastream[startIndex:startIndex+requiredUniqueChars]
    
    return marker, startIndex + requiredUniqueChars
        

def main():
    datastream = getDataStream("input.txt")
    marker, indexOfLastCharacter = findMarker(datastream, 14)
    print(marker, indexOfLastCharacter)

main()