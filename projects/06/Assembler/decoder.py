""" 
Decoder for HACK Assembler
Author: Abhinand D Manoj

- Takes input in form of tuple string eg: (1, 1234)
- Contains codes for C instruction
- Translates into machine code
"""
import sys

JMP_CODES = {
        "NONE" : "000",
        "JGT" : "001",
        "JEQ" : "010",
        "JGE" : "011",
        "JLT" : "100",
        "JNE" : "101",
        "JLE" : "110",
        "JMP" : "111"
        }

COMP_CODES = {
        "0" : "0101010",
        "1" : "0111111",
        "-1" : "0111010",
        "D" : "0001100",
        "A" : "0110000",
        "M" : "1110000",
        "!D" : "0001101",
        "!A" : "0110001",
        "!M" : "1110001",
        "-D" : "0001111",
        "-A" : "0110011",
        "-M" : "1110011",
        "D+1" : "0011111",
        "A+1" : "0110111",
        "M+1" : "1110111",
        "D-1" : "0001110",
        "A-1" : "0110010",
        "M-1" : "1110010",
        "D+A" : "0000010",
        "D+M" : "1000010",
        "D-A" : "0010011",
        "D-M" : "1010011",
        "A-D" : "0000111",
        "M-D" : "1000111",
        "D&A" : "0000000",
        "D&M" : "1000000",
        "D|A" : "0010101",
        "D|M" : "1010101"
        }

DEST_CODES = {
        "None" : "000",
        "M" : "001",
        "D" : "010",
        "MD" : "011",
        "A" : "100",
        "AM" : "101",
        "AD" : "110",
        "AMD" : "111"
        }

def extend(binary):
    """ Returns in 16-bit format; Works only with binary <= 16-bit """

    if 0 < len(binary) < 17:
        while len(binary) != 16:
            binary = "0" + binary
        return binary
    
    else:
        raise ValueError("Invalid input: Binary string too long")

def main(parsed_ins, SYMBOLS=None):
    # If None, return None
    if parsed_ins is None:
        return None

    # Cleaning input
    parsed_ins = tuple(i for i in parsed_ins.split(','))

    # A instruction
    if parsed_ins[0] == '0':
        arg = parsed_ins[1]
        
        if not arg.isdigit():
            bin_data = bin(int(SYMBOLS[arg]))[2:]
            return extend(bin_data)
        else:
            bin_data = bin(int(arg))[2:]
            return extend(bin_data)

    # C instruction
    elif parsed_ins[0] == '1':
        comp = parsed_ins[1]
        dest = parsed_ins[2]
        jmp = parsed_ins[3].upper()

        if (comp not in COMP_CODES) or (dest not in DEST_CODES) or (jmp not in JMP_CODES):
            print(parsed_ins)
            raise ValueError("Invalid instruction")
        else:
            return "111" + COMP_CODES[comp] + DEST_CODES[dest] + JMP_CODES[jmp]

    # if pseudo-instruction, ignore
    else:
        return None

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: python3 decoder.py <parsed_instruction>")
    else:
        print( main(sys.argv[1]) )
