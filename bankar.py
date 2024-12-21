#!/bin/env/python3
#number of resources (m)
#processes that are working (n)
import random
import math
mtrx = []

n = int(input("Number of resources (1-10): "))
m = int(input("Working processes: "))
#user input 
for row in range(n):
    s = []
    for coloumn in range(m):
        s.append(m)
    mtrx.append(s)
#printing matrices
def matrix():
    for row in range(n):
        for column in range(m):
            print(mtrx[row][column], end=" ")
            return matrix