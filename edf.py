#!/bin/env/python3

def sort_by_deadline(process):
    return process[1]  

def earliest_deadline_first(processes):

    processes.sort(key=sort_by_deadline)
    
    for process in processes:
        print("Running process:", process[0])
        print("Process", process[0], "has deadline:", process[1])
        print("Process", process[0], "finished.")


processes = [("P1", 5), ("P2", 3), ("P3", 1)]  

earliest_deadline_first(processes)
