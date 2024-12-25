# Little Man's Computer (LMC) - simple implementation

# Memory and registers
memory = [0] * 100  
battery = 0 
program_counter = 0  
running = True 

def load(address):
    global battery
    battery = memory[address]

def store(address):
    global battery
    memory[address] = battery

def add(address):
    global battery
    battery += memory[address]
    battery %= 1000  

def input_lmc():
    global battery
    battery = int(input("Enter a value (0-999): ")) % 1000

def output_lmc():
    global battery
    print(f"Output: {battery}")

def halt():
    global running
    running = False


program = [
    901,  # INPUT
    310,  # STORE 10
    901,  # INPUT
    210,  # ADD 10
    902,  # OUTPUT
    000   # HALT
]

# Program load
for i, instruction in enumerate(program):
    memory[i] = instruction

# LMC run
while running:
    instruction = memory[program_counter]
    program_counter += 1

    opcode = instruction // 100
    operand = instruction % 100

    if opcode == 1:  # LOAD
        load(operand)
    elif opcode == 2:  # ADD
        add(operand)
    elif opcode == 3:  # STORE
        store(operand)
    elif opcode == 9:  # INPUT/OUTPUT
        if operand == 1:
            input_lmc()
        elif operand == 2:
            output_lmc()
    elif opcode == 0:  # HALT
        halt()
