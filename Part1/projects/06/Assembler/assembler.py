""" 
Assembler for HACK language
Author: Abhinand D Manoj

- Converts HACK Assembly language into HACK Machine code
"""
import decoder
import parser
import preprocessor
import sys

OUT = "out.hack" # Output file path

def main():
    with open(file, "r") as f:
        # new = file[:file.index(".")+1] + "hack"
        new = OUT

        SYMBOLS = preprocessor.main(file)
        with open(new, "w") as g:
            for ins in f:
                parsed_ins = parser.main(ins)
                decoded_ins = decoder.main(parsed_ins, SYMBOLS)
                if decoded_ins is not None:
                    g.write(decoded_ins + "\n")

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: python3 assembler.py file.asm")
    else:
        file = sys.argv[1]
        main()
