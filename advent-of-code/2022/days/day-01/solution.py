import pathlib

currentPath = pathlib.Path(__file__).parent.resolve()
filepath = pathlib.Path(currentPath, "input.txt")

#open file
f = open(filepath)

#initialise a max variable
elfCalories = []

#initialise a calorie count variable
currentElfCalorieCount = 0

#for each line
for line in f:
    
    if line != "\n":    #current elf
        #if line has calories, add calories to current elf calorie count
        currentElfCalorieCount += int(line)
    else:               #new elf
        #if line is empty, 
        elfCalories.append(currentElfCalorieCount)
        currentElfCalorieCount = 0

elfCalories.append(currentElfCalorieCount)
sortedCalories = sorted(elfCalories, reverse=True)

print("Top 3 Calorie Carrying Elves:")
for i in range(0,3):
    print(sortedCalories[i])
print()

print("In total:", sum(sortedCalories[0:3]))



    

    