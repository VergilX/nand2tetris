"""
Parser for HACK machine Assembly
Author: Abhinand D Manoj

- Removes white space
- Removes comments
- Separates components
"""

import sys

def remove_whitespace(ins):
    # ins = ins.trim()
    cleaned_ins = ""
    
    for i in ins:
        if i != " ":
            cleaned_ins += i

    return cleaned_ins

def remove_comments(ins):
    cleaned_ins = ""

    n = len(ins)
    for i in range(n-1):
        if not (ins[i:i+2] == "//"):
            cleaned_ins += ins[i]
    # Leftover character
    cleaned_ins += ins[n-1]

    return cleaned_ins

def main(ins):
    # Instruction type codes
    A_INSTRUCTION = 0
    C_INSTRUCTION = 1

    cleaned_ins = remove_comments(remove_whitespace(ins))
    print(cleaned_ins)

    # A instruction
    if cleaned_ins[0] == "@":
        return (A_INSTRUCTION, cleaned_ins[1:])

    else: # C instruction
        if_des = ins.find("=")
        if_jmp = ins.find(";")
        dest = comp = jmp = None
        
        if if_des != -1:
            if if_jmp != -1:
                dest = ins[:if_des]
                comp = ins[if_des+1:if_jmp]
                jmp = ins[if_jmp+1:]

            else:
                dest = ins[:if_des]
                comp = ins[if_des+1:]
        else:
            if if_jmp != -1:
                dest = ins[:if_jmp]
                jmp = ins[if_jmp+1:]
        
        return (C_INSTRUCTION, comp, dest, jmp)

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: python3 parser.py \"<instruction>\"")
    else:
        main(sys.argv[1])
