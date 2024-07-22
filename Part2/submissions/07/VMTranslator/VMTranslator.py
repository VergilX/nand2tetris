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
            parsed_instruction = parser.main(instruction)

            # If not empty line or comment
            if (parsed_instruction != ""):
                # Writing instruction as comment
                f.write("// " + instruction)

                decoded_instruction = decoder.main(parsed_instruction, filename)
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
