# Processes (arrival time, burst time)
processes = [("P1", 0, 4), ("P2", 2, 3), ("P3", 4, 2)]

# FCFS Algorithm
def fcfs(processes):
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    
    print("Process | Waiting Time | Turnaround Time")
    print("-" * 30)
    
    for id, arrival, burst in processes:
        current_time = max(current_time, arrival)
        waiting_time = current_time - arrival
        turnaround_time = waiting_time + burst
        
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time
        current_time += burst
        
        print(f"{id:<7} | {waiting_time:<13} | {turnaround_time}")
    
    print("-" * 30)
    print(f"Avg Waiting Time: {total_waiting_time / len(processes):.2f}")
    print(f"Avg Turnaround Time: {total_turnaround_time / len(processes):.2f}")

# Run
fcfs(processes)
