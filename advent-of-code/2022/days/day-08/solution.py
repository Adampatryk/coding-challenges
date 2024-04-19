import pathlib
from enum import Enum

class Tree:
    def __init__(self, x, y, height, visible):
        self.x = x
        self.y = y
        self.height = height
        self.visible = visible
        self.scenicScore = 0

def openFile(filename):
    currentPath = pathlib.Path(__file__).parent.resolve()
    filepath = pathlib.Path(currentPath, filename)
    return open(filepath)

def getTreeGrid(filename):
    treeGrid = []
    file=openFile(filename)
    lineIndex = 0
    for line in file:
        treeLine = line.strip()
        trees = []
        for characterIndex in range(len(treeLine)):
            height = int(treeLine[characterIndex])
            trees.append(Tree(characterIndex, lineIndex, height, False))
        treeGrid.append(trees)
        lineIndex += 1
    
    return treeGrid

def printTreeGrid(treeGrid, onlyVisible = False):
    for treeLine in treeGrid:
        for tree in treeLine:
            if onlyVisible and not tree.visible:
                print("x", end="")
            else:
                print(tree.height,end="")
        print()
    print()

def getDimensions(treeGrid):
    width = len(treeGrid[0])
    height = len(treeGrid)
    return width, height

def setOuterTreesVisible(treeGrid):
    width, height = getDimensions(treeGrid)
    for y in range(0, height):
        for x in range(0, width):
            if x == 0 or y == 0 or x == width-1 or y == height-1:
                treeGrid[y][x].visible = True
    return treeGrid 

def getTreeAt(x, y, treeGrid):
    return treeGrid[y][x]

def treeCanSeeLeftEdge(tree, treeGrid):
    for x in range(tree.x-1, -1, -1):
        if getTreeAt(x, tree.y,treeGrid).height >= tree.height:
            return False
    return True

def treeCanSeeTopEdge(tree, treeGrid):
    for y in range(tree.y-1, -1, -1):
        if getTreeAt(tree.x, y,treeGrid).height >= tree.height:
            return False
    return True

def treeCanSeeRightEdge(tree, treeGrid):
    width, _ = getDimensions(treeGrid)
    for x in range(tree.x+1, width):
        if getTreeAt(x, tree.y, treeGrid).height >= tree.height:
            return False
    return True

def treeCanSeeBottomEdge(tree, treeGrid):
    _, height = getDimensions(treeGrid)

    for y in range(tree.y+1, height):
        if treeGrid[y][tree.x].height >= tree.height:
            return False
    return True

def treeCanSeeEdge(tree, treeGrid):
    print(tree.x, tree.y, tree.height)

    return  treeCanSeeLeftEdge(tree,treeGrid) or \
            treeCanSeeTopEdge(tree,treeGrid) or \
            treeCanSeeRightEdge(tree,treeGrid) or \
            treeCanSeeBottomEdge(tree,treeGrid) 
        
def countVisibleTrees(treeGrid):
    count = 0
    for treeLine in treeGrid:
        for tree in treeLine:
            if tree.visible:
                count += 1
    return count

def setTreeVisibilities(treeGrid):
    for treeLine in treeGrid:
        for tree in treeLine:
            if treeCanSeeEdge(tree, treeGrid):
                tree.visible = True

def countVisibleTreesUp(tree, treeGrid):
    visibleTrees = 0
    for y in range(tree.y-1, -1, -1):
        lookingAtTree = getTreeAt(tree.x, y,treeGrid)
        if lookingAtTree.height >= tree.height:
            visibleTrees += 1
            return visibleTrees
        elif lookingAtTree.height < tree.height:
            visibleTrees += 1
    return visibleTrees

def countVisibleTreesRight(tree, treeGrid):
    visibleTrees = 0
    width, _ = getDimensions(treeGrid)
    for x in range(tree.x+1, width):
        lookingAtTree = getTreeAt(x, tree.y,treeGrid)
        if lookingAtTree.height >= tree.height:
            visibleTrees += 1
            return visibleTrees
        elif lookingAtTree.height < tree.height:
            visibleTrees += 1
    return visibleTrees

def countVisibleTreesDown(tree,treeGrid):
    visibleTrees = 0
    _, height = getDimensions(treeGrid)
    for y in range(tree.y+1, height):
        print("down", y)
        lookingAtTree = getTreeAt(tree.x, y,treeGrid)
        #if the tree im looking at is bigger than the current tree
            # it is visible and stop
        if lookingAtTree.height >= tree.height:
            visibleTrees += 1
            print("down last visible tree")
            return visibleTrees
        elif lookingAtTree.height < tree.height:
            print("down visible tree")
            visibleTrees += 1
        
    return visibleTrees

def countVisibleTreesLeft(tree,treeGrid):
    visibleTrees = 0
    for x in range(tree.x-1, -1, -1):
        print("left", x)

        lookingAtTree = getTreeAt(x, tree.y,treeGrid)
        if lookingAtTree.height >= tree.height: #blocked
            visibleTrees += 1
            print("left last visible tree")

            return visibleTrees
        elif lookingAtTree.height < tree.height:
            print("left visible tree")

            visibleTrees += 1
    return visibleTrees


def calculateScenicScore(tree, treeGrid):
    visibleTrees = [countVisibleTreesUp(tree, treeGrid), countVisibleTreesRight(tree, treeGrid), countVisibleTreesDown(tree, treeGrid), countVisibleTreesLeft(tree, treeGrid)]
    print(tree.x, tree.y, tree.height, visibleTrees)

    # Multiply elements one by one
    result = 1
    for x in visibleTrees:
        result = result * x
    print(result)
    return result

def calculateScenicScores(treeGrid):
    for treeLine in treeGrid:
        for tree in treeLine:
            tree.scenicScore = calculateScenicScore(tree, treeGrid)

def getTreeWithMaxScenicScore(treeGrid):
    maxScoreTree = treeGrid[0][0]
    for trees in treeGrid:
        for tree in trees:
            if tree.scenicScore > maxScoreTree.scenicScore:
                maxScoreTree = tree
    return maxScoreTree

def main():
    treeGrid = getTreeGrid('input.txt')
    printTreeGrid(treeGrid, True)
    printTreeGrid(treeGrid, False)

    setOuterTreesVisible(treeGrid)
    printTreeGrid(treeGrid, True)

    setTreeVisibilities(treeGrid)

    printTreeGrid(treeGrid, True)
    printTreeGrid(treeGrid, False)

    visibleTrees = countVisibleTrees(treeGrid)
    print("Visible trees: ",visibleTrees)
    
    #calculate scenic score for each tree
    calculateScenicScores(treeGrid)

    #get biggest scenic score
    maxScenicScoringTree = getTreeWithMaxScenicScore(treeGrid)
    print("Max scenic score", maxScenicScoringTree.scenicScore, "x:", maxScenicScoringTree.x, "y:", maxScenicScoringTree.y)
    
main()
