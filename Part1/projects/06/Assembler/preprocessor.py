"""
Preprocessor for HACK Assembler
Author: Abhinand D Manoj

- First pass: Creates symbol table
- Returns the symbol table
- Can be used as input for parser
"""

import sys
import parser

LABELS = {
        "SP" : 0,
        "LCL" : 1, "ARG" : 2,
        "THIS" : 3,
        "THAT" : 4,
        "SCREEN" : 16384,
        "KBD" : 24576
        }

def second_pass(file_handler):
    """ Generates the final symbol table """

    var_address = 16           # Location for variables

    for line in file_handler:
        parsed_instruction = parser.main(line)

        if parsed_instruction is not None:
            cleaned_instruction = parsed_instruction.split(',')
            instruction_type = cleaned_instruction[0]

            if instruction_type == "0":
                arg = cleaned_instruction[1]

                if not arg.isdigit():
                    # If not present in symbol table
                    if arg not in LABELS:
                        LABELS[arg] = var_address
                        var_address += 1

def first_pass(file_handler):
    """ Adds pseudo instructions to symbol table"""

    instruction_count = 0       # Instruction line number

    for line in file_handler:
        # Parse line
        parsed_instruction = parser.main(line)

        if parsed_instruction is not None:
            cleaned_instruction = parsed_instruction.split(',')
            instruction_type = cleaned_instruction[0]

            if instruction_type == "2":           # If it's a pseudo instruction
                LABELS[cleaned_instruction[1]] = instruction_count
            else:
                instruction_count += 1

def main(file):
    # Adding General Purpose Registers
    for i in range(16):
        LABELS[f"R{i}"] = i

    with open(file, "r") as file_handler:
        first_pass(file_handler)
        file_handler.seek(0)       # Start of file
        second_pass(file_handler)

    return LABELS

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 preprocessor.py file.asm")
    else:
        file = sys.argv[1]
        print(main(file))
