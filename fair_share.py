#!/bin/env/python3 

class FairShareScheduler:

    def __init__(self, processes, total_time):
        self.processes = processes  
        self.total_time = total_time  
        self.time_slice = total_time // len(processes)  
   
    def run(self):
        print("Total CPU time available:", self.total_time)
        print("Time slice for each process:", self.time_slice)
        # Run each process one by one
        for process in self.processes:
            print("Running process:", process)
            self.execute_process(process)

    def execute_process(self, process):
        print("Starting process:", process)
        print("Process", process, "is running for", self.time_slice, "seconds.")
        print("Process", process, "finished.")



total_time = 9  # Total CPU time available
processes = ["P1", "P2", "P3"]
# Create a scheduler and run it
scheduler = FairShareScheduler(processes, total_time)
scheduler.run()
