#!/bin/python3

import sys

sumOfSquares = []
squareOfSums = []
sums = 0
squareSums = 0

for N in range(1, int(1E+4) +1):
    sums += N
    squareSums += N**2
    sumOfSquares.append(squareSums)
    squareOfSums.append(sums**2)

t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    print(abs(sumOfSquares[n-1] - squareOfSums[n-1]))
    
    