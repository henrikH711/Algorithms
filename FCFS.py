# Processes (arrival time, burst time)
processes = [("P1", 0, 4), ("P2", 2, 3), ("P3", 4, 2)]

# FCFS - First Come First Served algorithm
def fcfs(processes):
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    
    print("Process | Waiting Time | Turnaround Time")
    print("-" * 40)
    
    for process in processes:
        id, arrival, burst = process
        
        # If the process arrives later than the current time, wait
        current_time = max(current_time, arrival)
        
        waiting_time = current_time - arrival
        turnaround_time = waiting_time + burst
        
        # Accumulate totals
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time
        
        # Move to the next time slot
        current_time += burst
        
        print(f"{id:<7} | {waiting_time:<13} | {turnaround_time}")
    
    # Averages
    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)
    
    print("-" * 40)
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

# Execute
fcfs(processes)
