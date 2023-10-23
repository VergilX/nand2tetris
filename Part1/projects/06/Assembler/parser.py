"""
Parser for HACK machine Assembly
Author: Abhinand D Manoj

- Removes white space
- Removes comments
- Separates components
"""

import sys

def remove_whitespace(ins):
    ins = ins.strip()
    cleaned_ins = ""
    
    for i in ins:
        if i != " ":
            cleaned_ins += i
    return cleaned_ins

def remove_comments(ins):
    cleaned_ins = ""

    n = len(ins)
    if n != 0:
        for i in range(n-1):
            if (ins[i:i+2] == "//"):
                break
            else:
                cleaned_ins += ins[i]
        else:
            # Leftover character
            cleaned_ins += ins[n-1]

        return cleaned_ins
    else:
        return None

def main(ins):
    # Instruction type codes
    A_INSTRUCTION = 0
    C_INSTRUCTION = 1
    PSEUDO_INSTRUCTION = 2

    cleaned_ins = remove_comments(remove_whitespace(ins))
    
    # Removing empty lines
    if cleaned_ins in [None, ""]:
        return None

    # A instruction
    if cleaned_ins[0] == "@":
        return f"{A_INSTRUCTION},{cleaned_ins[1:]}"

    # Pseudo instruction
    elif cleaned_ins[0] == "(":
        return f"{PSEUDO_INSTRUCTION},{cleaned_ins[1:-1]}"

    else: # C instruction
        if_des = cleaned_ins.find("=")
        if_jmp = cleaned_ins.find(";")
        dest = comp = jmp = None
        
        if if_des != -1:
            if if_jmp != -1:
                # eg: A=D+M;JGT
                dest = cleaned_ins[:if_des]
                comp = cleaned_ins[if_des+1:if_jmp]
                jmp = cleaned_ins[if_jmp+1:]

            else:
                # eg: D=D+M
                dest = cleaned_ins[:if_des]
                comp = cleaned_ins[if_des+1:]
        else:
            if if_jmp != -1:
                # eg: D;JGT
                comp = cleaned_ins[:if_jmp]
                jmp = cleaned_ins[if_jmp+1:]
        
        return f"{C_INSTRUCTION},{comp},{dest},{jmp}"

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: python3 parser.py \"<instruction>\"")
    else:
        print( main(sys.argv[1]) )
