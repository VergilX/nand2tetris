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
        file = sys.argv[1]
        filename = file[:file.index('.')]
        g = open(file, "r")
    except FileNotFoundError:
        print("File not found")
    else:
        instruction = g.readline().strip()

        # Reading whole input file
        while (len(instruction) != 0):
            # instruction = g.readline().strip()
            print(instruction)

            # Writing instruction as comment
            f.write("// " + instruction + "\n")

            parsed_instruction = parser.main(instruction)
            decoded_instruction = decoder.main(parsed_instruction, filename)
            # print(decoded_instruction)
            f.write(decoded_instruction)

            # Reading next line
            instruction = g.readline().strip()
        f.close()
        g.close()

if __name__ == "__main__":
    syslen = len(sys.argv)
    if syslen not in [2, 3]:
        print("Usage: python3 VMTranslator.py <inputfile> [<outputfile>]")
    else:
        if syslen == 3:
            FILE = sys.argv[2]
        main()
