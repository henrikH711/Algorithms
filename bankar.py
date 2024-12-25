#!/usr/bin/env/python3
import random

n = int(input("Number of resources (1-10): "))
m = int(input("Number of processes: "))

max_req = [[random.randint(1, 10) for _ in range(n)] for _ in range(m)]
allocation = [[random.randint(0, max_req[i][j]) for j in range(n)] for i in range(m)]
available = [random.randint(1, 10) for _ in range(n)]
need = [[max_req[i][j] - allocation[i][j] for j in range(n)] for i in range(m)]

def is_safe():
    work = available[:]
    finish = [False] * m
    sequence = []

    for _ in range(m):
        for i in range(m):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(n)):
                work = [work[j] + allocation[i][j] for j in range(n)]
                sequence.append(i)
                finish[i] = True
                break
        else:
            return False, []

    return True, sequence

#  matrices
print("Max Request:", max_req)
print("Allocation:", allocation)
print("Need:", need)
print("Available:", available)

#  safety
safe, sequence = is_safe()
if safe:
    print("System is safe. Safe sequence:", sequence)
else:
    print("System is not safe.")
