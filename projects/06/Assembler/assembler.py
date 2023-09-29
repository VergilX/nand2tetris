""" 
Assembler for HACK language
Author: Abhinand D Manoj

- Converts HACK Assembly language into HACK Machine code
"""
import sys
import parser
import decoder

OUT = "out.hack" # Output file path

def main():
    with open(file, "r") as f:
        # new = file[:file.index(".")+1] + "hack"
        new = OUT

        with open(new, "w") as g:
            for ins in f:
                parsed_ins = parser.main(ins)
                if parsed_ins is not None:
                    decoded_ins = decoder.main(parsed_ins)
                    g.write(decoded_ins + "\n")

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: python3 assembler.py file.asm")
    else:
        file = sys.argv[1]
        main()
