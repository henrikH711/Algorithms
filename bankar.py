#!/bin/env/python3
#number of resources (m)
#processes that are working (n)

import random
import math
max_req = []
n = int(input("Number of resources (1-10): "))
m = int(input("Working processes: "))
for row in range(n):
    s = random.randint(0,9)
    for coloumn in range(m):
         max_req.append(s)
print(max_req)
#avaible  
available = [random.randint(1, 10) for _ in range(n)]

    #allocation 
allocation = [[random.randint(0, max_req[i][j]) for j in range(n)] for i in range(m)]
need = [[max_req[i][j] - allocation[i][j] for j in range(n)] for i in range(m)]
def is_safe():
    work = available[:]
    finish = [False] * m
    safe_sequence = []

    for _ in range(m):
        found = False
        for i in range(m):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(n)):
        
                work = [work[j] + allocation[i][j] for j in range(n)]
                safe_sequence.append(i)
                finish[i] = True
                found = True
                break
        if not found:
            return False, []

    return True, safe_sequence

    print("Max Request Matrix:")
for row in max_req:
    print(row)

print("\nAllocation Matrix:")
for row in allocation:
    print(row)

print("\nNeed Matrix:")
for row in need:
    print(row)

print("\nAvailable Resources:")
print(available)

safe, sequence = is_safe()
if safe:
    print("\nSafe state. Safe sequence:", sequence)
else:
    print("\nNot a safe state.")