#!/bin/env/python3
#roundrobin_algorithm
#tg stands for time quantum
#p stands for process
import random
tq = random.randint(1,9)
processes = []
for i in range(20):
    tq += 1
    p = input(f"{i + 1}")
    p = str(input(""))
    processes.append(p)
    while processes:
         current_process = processes.pop(0)  
    tq += 1 
    print(f"Under_processing: {current_process} | Time quantum: {tq}")
