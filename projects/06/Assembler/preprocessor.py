"""
Preprocessor for HACK Assembler
Author: Abhinand D Manoj

- First pass: Creates symbol table
- Returns the symbol table
- Can be used as input for parser
"""

import sys

LABELS = {
        "SP" : 0,
        "LCL" : 1,
        "ARG" : 2,
        "THIS" : 3,
        "THAT" : 4,
        "SCREEN" : 16384,
        "KBD" : 24576
        }

def second_pass():
    """ Generates the final symbol table """

    var_address = 16           # Location for variables

    with open(file, "r") as f:
        for line in f:
            start_char = line[0]

            if start_char == "@":
                arg = line[1:-1]            # Remove @ and '\n'

                if arg.isalpha():
                    # If not present in symbol table
                    if arg not in LABELS:
                        LABELS[arg] = var_address
                        var_address += 1

def first_pass():
    """ Adds pseudo instructions to symbol table"""

    with open(file, "r") as f:
        instruction_count = 0       # Instruction line number

        for line in f:
            # Ignore line comments and whitespace
            if (not line.isspace()) and line!="\n" and line[:2]!="//":
                start_char = line[0]    # Starting symbol of instruction

                # Pseudo symbols: (Xxx)
                if start_char == "(":
                    LABELS[line[1:-2]] = instruction_count      # Removing ( and )\n

                else:
                    instruction_count += 1

def main():
    # Adding General Purpose Registers
    for i in range(16):
        LABELS[f"R{i}"] = i

    first_pass()
    second_pass()

    return LABELS

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 preprocessor.py file.asm")
    else:
        file = sys.argv[1]
        print(main())
