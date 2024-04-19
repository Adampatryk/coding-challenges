import pathlib

currentPath = pathlib.Path(__file__).parent.resolve()
filepath = pathlib.Path(currentPath, "input.txt")

def convertItemToPriority(item):
    asc = ord(item)
    #upper case letters A(27)-Z(52)
    if asc > 64 and asc < 91:
        return asc-64+26
    #lower case letters a(1)-z(26)
    elif asc > 96 and asc < 123:
        return asc-96
    else:
        raise Exception("Not a letter")

def commonItems(a, b):
    items = list(set(a).intersection(set(b)))
    #print(items)
    return items

def commonItem(a, b, c):
    print(a, b, c)
    items = list(set(a) & set(b) & set(c))
    print(items)
    return items[0]

def sumBackpackCommonItemPriorities(rucksacks):
    total = 0
    for rucksack in rucksacks:
        common = rucksack["common"]
        if (len(common)>0):
            total += convertItemToPriority(common[0])

    return total

def part1(f):
    rucksacks = []

    #for each line
    for line in f:
        size = len(line)
        one = line[0:size//2]
        two = line[size//2:size]
        rucksack = {
            'one': one,
            'two': two,
            'common': commonItems(one,two)
        }
        rucksacks.append(rucksack)
    
    print(sumBackpackCommonItemPriorities(rucksacks))

def part2(f):

    rucksacks = []
    groups = []

    i = 0
    #for each line
    for rucksack in f:
        if i < 3:
            rucksacks.append(rucksack.strip())
            i += 1
        else:
            groups.append(rucksacks)
            rucksacks = []
            rucksacks.append(rucksack)
            i = 1
    groups.append(rucksacks)

    
    total = 0
    for group in groups:
        common = commonItem(group[0], group[1], group[2])
        total += convertItemToPriority(common)
    print(total)

def main():
    f = open(filepath)
    part2(f)

main()