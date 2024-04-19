import pathlib

def openFile(filename):
    currentPath = pathlib.Path(__file__).parent.resolve()
    filepath = pathlib.Path(currentPath, filename)
    return open(filepath)

def getTreeGrid(filename):
    file=openFile(filename)
    for line in file:
        pass
        

def main():
    treeGrid = getTreeGrid('input.txt')
    
    
main()
