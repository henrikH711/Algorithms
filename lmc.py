# Little Man's Computer (LMC) - Simplified Implementation

# Memory and registers
memory = [0] * 100
battery = 0
program_counter = 0
running = True

def execute(instruction):
    global battery, program_counter, running
    opcode = instruction // 100
    operand = instruction % 100

    if opcode == 1:  # LOAD
        battery = memory[operand]
    elif opcode == 2:  # ADD
        battery = (battery + memory[operand]) % 1000
    elif opcode == 3:  # STORE
        memory[operand] = battery
    elif opcode == 9:  # INPUT/OUTPUT
        if operand == 1:  # INPUT
            battery = int(input("Enter a value (0-999): ")) % 1000
        elif operand == 2:  # OUTPUT
            print(f"Output: {battery}")
    elif opcode == 0:  # HALT
        running = False

# Sample program
program = [
    901,  # INPUT
    310,  # STORE 10
    901,  # INPUT
    210,  # ADD 10
    902,  # OUTPUT
    000   # HALT
]

# Load program into memory
memory[:len(program)] = program

# Run the program
while running:
    execute(memory[program_counter])
    program_counter += 1
