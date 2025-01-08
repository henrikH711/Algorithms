#!/bin/env/python3

 # Sort by the second element 
def sort_by_period(process):
    return process[1] 


def rate_monotonic_scheduling(processes):
    # Sort processes 
    processes.sort(key=sort_by_period)
    
    for process in processes:
        print("Running process:", process[0])
        print("Process", process[0], "has period:", process[1])
        print("Process", process[0], "finished.")

processes = [("P1", 3), ("P2", 5), ("P3", 1)]  


rate_monotonic_scheduling(processes)
