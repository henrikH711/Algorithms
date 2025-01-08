#!/bin/env/python3

def fair_share_scheduler(processes, total_time):
    time_slice = total_time // len(processes)  # Each process gets equal time slice
    
    print("Total CPU time available:", total_time)
    print("Time slice for each process:", time_slice)
    
    for process in processes:
        print("Running process:", process)
        print("Process", process, "is running for", time_slice, "seconds.")
        print("Process", process, "finished.")


# Example processes and total time
total_time = 9  # Total CPU time available
processes = ["P1", "P2", "P3"]

# Run the fair share scheduler
fair_share_scheduler(processes, total_time)
