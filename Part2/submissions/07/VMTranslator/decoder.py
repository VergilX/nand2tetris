"""
Decoder for VMTranslator

Author: @abhinanddmanoj
Date: 28 Dec 2023
"""

from codebase import *
import sys

ITERATION = 0

# Register names
REGISTER = {
        "local"     : "LCL",
        "argument"  : "ARG",
        "this"      : "THIS",
        "that"      : "THAT"
        }

def main(parsed_instruction, filename):
    global ITERATION
    global STATIC

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

    # push/pop <segmentPointer> <arg>
    elif (operation=="push") or (operation=="pop"):
        COMMANDS = PUSH_COMMANDS

        # Setting if push/pop
        if operation == "pop":
            COMMANDS = POP_COMMANDS

        segment = parsed_instruction[1]

        # will only have single argument
        arg = parsed_instruction[2][0]

        # constant and base have similar substitutions
        if (segment=="constant") or (segment=="temp"):
            # In codebase, <val> is used as delimiter for
            # replacing arg in HACK assembly
            return COMMANDS[segment].replace("<val>", str(arg))

        elif segment in ["local", "argument", "this", "that"]:
            # to be replaced: <val>, <reg>
            return COMMANDS["segment"].replace("<reg>", REGISTER[segment]).replace("<val>", str(arg))

        elif segment == "pointer":
            # 0 -> THIS
            if arg == 0:
                return COMMANDS[segment].replace("<val>", "THIS")
            # 1 -> THAT
            elif arg == 1:
                return COMMANDS[segment].replace("<val>", "THAT")
            else:
                print("Invalid argument for pointer segment")
                return ""

        elif segment == "static":
            # to be replaced: <val>
            val = filename+"."+str(arg) # Foo.i for input 'Foo.vm'

            return COMMANDS[segment].replace("<file.i>", val)

        else:
            print(f"Undefined segment name: '{segment}'")
            return ""

    else:
        print("yet to implement")

if __name__ == "__main__":
    print("""
    Cannot be used independently.

    Use the VMTranslator or pass parser input
    by importing to another file

    main(parsed_instruction, filename)
    """)
