# List of processes (ID, arrival time, burst time)
processes = [("P1", 0, 6), ("P2", 1, 8), ("P3", 2, 7), ("P4", 3, 3)]

def sjn(processes):
    completed = []              # List of completed processes
    current_time = 0            # Tracks the current time
    total_waiting_time = 0      # Total waiting time
    total_turnaround_time = 0   # Total turnaround time

    print("Process | Waiting Time | Turnaround Time")
    print("-" * 40)

    while processes:            # Loop until all processes are completed
        # Get processes that have arrived by current time
        available = [p for p in processes if p[1] <= current_time]

        if not available:       # If no process is available, jump to next arrival time
            current_time = min(processes, key=lambda x: x[1])[1]
            continue

        # Select the process with the shortest burst time
        shortest_job = min(available, key=lambda x: x[2])
        id, arrival, burst = shortest_job

        # Calculate times
        waiting_time = current_time - arrival
        turnaround_time = waiting_time + burst

        # Update totals
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time

        # Update time and remove the completed process
        current_time += burst
        completed.append(shortest_job)
        processes.remove(shortest_job)

        print(f"{id:<7} | {waiting_time:<13} | {turnaround_time}")

    # Calculate and display averages
    avg_waiting_time = total_waiting_time / len(completed)
    avg_turnaround_time = total_turnaround_time / len(completed)

    print("-" * 40)
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

# Run the SJN algorithm
sjn(processes)

