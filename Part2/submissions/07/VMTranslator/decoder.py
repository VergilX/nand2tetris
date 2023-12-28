"""
Decoder for VMTranslator

Author: @abhinanddmanoj
Date: 28 Dec 2023
"""
from codebase import *

ITERATION = 0

def main(parsed_instruction):
    global ITERATION

    operation = parsed_instruction[0]

    # Arithmetic or Logical commands
    if operation in AL_COMMANDS:

        # If eq, lt, gt; dynamic naming is required
        if operation in ["eq", "lt", "gt"]:
            # In codebase, <val> is used as delimiter for
            # iteration replacement in arithmetic and logical
            # operations
            returnvalue = AL_COMMANDS[operation].replace("<val>", str(ITERATION))
            ITERATION += 1
            return returnvalue

        else:
            return AL_COMMANDS[operation]

    # push <segmentPointer> <arg>
    elif operation == "push":
        segment = parsed_instruction[1]

        # will only have single argument
        arg = parsed_instruction[2][0]

        # In codebase, <val> is used as delimiter for
        # replacing arg in HACK assembly
        return POP_COMMANDS[segment].replace("<val>", str(arg))

    else:
        print("yet to implement")

if __name__ == "__main__":
    print("""
    Cannot be used independently.

    Use the VMTranslator or pass parser input
    by importing to another file
    """)
