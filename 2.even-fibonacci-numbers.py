#!/bin/python3

import sys

myFib = [1,2]
myEvenFib = [2]
result = 3
while (result <= 4E+16):
    if(result % 2 == 0):
        myEvenFib.append(result)
    myFib.append(result)
    result = myFib[len(myFib)-1] + myFib[len(myFib)-2]
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    output = 0
    for fibNum in myEvenFib:
        if (fibNum > n): 
            break
        output += fibNum
    print(output)
        
    
    