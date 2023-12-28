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
            # iteration replacement
            returnvalue = AL_COMMANDS[operation].replace("<val>", str(ITERATION))
            ITERATION += 1
            return returnvalue

        else:
            return AL_COMMANDS[operation]


if __name__ == "__main__":
    print("""
    Cannot be used independently.

    Use the VMTranslator or pass parser input
    by importing to another file
    """)
