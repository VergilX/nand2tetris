"""
VMTranslator of JACK language

Source: JACK language (high level)
Sink: HACK Assembly

Author: @abhinanddmanoj
Date: 28 Dec 2023
"""

import decoder
import parser
import sys

FILE = "output.asm"

def main():
    try:
        # Output file
        f = open(FILE, "w")

        # Input file
        g = open(file, "r")
    except FileNotFoundError:
        print("File not found")
    else:
        instruction = g.readline()

        # Reading whole input file
        while (instruction != ""):
            # instruction = g.readline().strip()
            instruction = instruction.strip()
            # print(instruction)

            # If not empty line or comment
            if (instruction not in ["", "\n"]) and (instruction[:2]!="//"):
                # Writing instruction as comment
                f.write("// " + instruction + "\n")

                parsed_instruction = parser.main(instruction)
                decoded_instruction = decoder.main(parsed_instruction, filename)
                # print(decoded_instruction)
                f.write(decoded_instruction)

            # Reading next line
            instruction = g.readline()
        f.close()
        g.close()

if __name__ == "__main__":
    syslen = len(sys.argv)
    if syslen not in [2, 3]:
        print("Usage: python3 VMTranslator.py <inputfile> [<outputfile>]")
    else:
        # input file details
        file = sys.argv[1]
        filename = file[:file.index('.')]

        if syslen == 3:
            # output filename provided in cli
            FILE = sys.argv[2]
        else:
            # default
            FILE = filename+".asm"
        main()
