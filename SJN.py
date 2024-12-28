# Processes (ID, arrival time, burst time)
processes = [("P1", 0, 6), ("P2", 1, 8), ("P3", 2, 7), ("P4", 3, 3)]

# SJN algorithm
def sjn(processes):
    completed = []  # Completed processes
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0

    print("Process | Waiting Time | Turnaround Time")
    print("-" * 40)

    while processes:
        # Find all processes that have arrived and are not completed
        available = [p for p in processes if p[1] <= current_time]

        if not available:
            # If no process is available, move time to the next arrival
            current_time = min(processes, key=lambda x: x[1])[1]
            continue

        # Select the shortest job (smallest burst time)
        shortest_job = min(available, key=lambda x: x[2])

        # Process details
        id, arrival, burst = shortest_job

        # Calculate waiting and turnaround time
        waiting_time = current_time - arrival
        turnaround_time = waiting_time + burst

        # Update totals
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time

        # Update current time and mark the process as completed
        current_time += burst
        completed.append(shortest_job)
        processes.remove(shortest_job)

        print(f"{id:<7} | {waiting_time:<13} | {turnaround_time}")

    # Averages
    avg_waiting_time = total_waiting_time / len(completed)
    avg_turnaround_time = total_turnaround_time / len(completed)

    print("-" * 40)
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

# Execute
sjn(processes)
