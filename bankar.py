#simplified Bankar's 

def is_safe_state(available, allocation, max_resources, num_processes, num_resources):
    work = available[:]
    finish = [False] * num_processes
    safe_sequence = []

    while len(safe_sequence) < num_processes:
        progress_made = False
        print("Current available resources:", work)
        print("Processes' allocation:", allocation)
        print("Processes' maximum demands:", max_resources)
        
        for i in range(num_processes):
            if not finish[i]:
                # Check if process i can be allocated resources
                can_allocate = True
                for j in range(num_resources):
                    if max_resources[i][j] - allocation[i][j] > work[j]:
                        can_allocate = False
                        break

                if can_allocate:
                    print(f"Allocating resources to Process {i}")
                    for j in range(num_resources):
                        work[j] += allocation[i][j]  # Release resources
                    safe_sequence.append(i)
                    finish[i] = True
                    progress_made = True
                    print(f"Process {i} finished. Updated available resources:", work)
                    print("Safe sequence so far:", safe_sequence)
                    break

        if not progress_made:
            print("No progress can be made, the system is not in a safe state.")
            return False, []

    print("System is in a safe state.")
    return True, safe_sequence


# Example data
available = [3, 3, 2]  # Available resources
max_resources = [  # Maximum demand for each process
    [7, 5, 3],  # P0
    [3, 2, 2],  # P1
    [9, 0, 2],  # P2
    [2, 2, 2],  # P3
    [4, 3, 3]   # P4
]

allocation = [  
    [0, 1, 0],  # P0
    [2, 0, 0],  # P1
    [3, 0, 2],  # P2
    [2, 1, 1],  # P3
    [0, 0, 2]   # P4
]

num_processes = 5  # Number of processes
num_resources = 3  # Number of resources

# Run the Banker's algorithm
safe, sequence = is_safe_state(available, allocation, max_resources, num_processes, num_resources)

if safe:
    print("The system is in a safe state, safe execution sequence:", sequence)
else:
    print("The system is not in a safe state, deadlock may occur.")
