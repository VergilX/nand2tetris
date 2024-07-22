"""
Decoder for VMTranslator

Author: @abhinanddmanoj
Date: 28 Dec 2023
"""

from codebase import *
import sys

ITERATION = 0
CURRENT_FUNCTION = "null"
CURRENT_FUNCTION_INDEX = 0

# Register names
REGISTER = {
        "local"     : "LCL",
        "argument"  : "ARG",
        "this"      : "THIS",
        "that"      : "THAT"
        }
JMP_COMMANDS = {
        "gt"        : "JGT",
        "lt"        : "JLT",
        "eq"        : "JEQ"
        }

def main(parsed_instruction, filename):
    global ITERATION, CURRENT_FUNCTION_INDEX, CURRENT_FUNCTION

    operation = parsed_instruction[0]

    # Arithmetic or Logical commands
    if (operation in AL_COMMANDS) or (operation in JMP_COMMANDS):

        # If eq, lt, gt; dynamic naming is required
        if operation in ["eq", "lt", "gt"]:
            # to be replaced: <val>, <jmp>
            returnvalue = AL_COMMANDS["comp"].replace("<val>", str(ITERATION)).replace("<jmp>", str(JMP_COMMANDS[operation]))
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
        arg = parsed_instruction[2]

        # Checking if arg is valud
        """
        if type(arg) != int:
            print("Invalid type of argument")
            return False
        """

        # constant and temp have similar substitutions
        if (segment=="constant") or (segment=="temp"):
            # In codebase, <val> is used as delimiter for
            # replacing arg in HACK assembly
            return COMMANDS[segment].replace("<val>", arg)

        elif segment in ["local", "argument", "this", "that"]:
            # to be replaced: <val>, <reg>
            return COMMANDS["segment"].replace("<reg>", REGISTER[segment]).replace("<val>", arg)

        elif segment == "pointer":
            # 0 -> THIS
            if arg == '0':
                return COMMANDS[segment].replace("<val>", "THIS")
            # 1 -> THAT
            elif arg == '1':
                return COMMANDS[segment].replace("<val>", "THAT")
            else:
                print("Invalid argument for pointer segment")
                return ""

        elif segment == "static":
            # to be replaced: <val>
            val = filename+"."+arg # Foo.i for input 'Foo.vm'

            return COMMANDS[segment].replace("<file.i>", val)

        else:
            print(f"Undefined segment name: '{segment}'")
            return ""

    # Branching instructions
    elif operation in ["label", "goto", "if-goto"]:

        # CHANGE: use current function name here
        # for now, using null
        labelname = filename + f".{CURRENT_FUNCTION}$" + parsed_instruction[1]

        # label <labelname>
        if operation == "label":
            return BRANCHING_COMMANDS["label"].replace("<label>", labelname)

        # goto <labelname>
        elif operation == "goto":
            return BRANCHING_COMMANDS["goto"].replace("<label>", labelname)

        # if-goto <labelname>
        elif operation == "if-goto":
            return BRANCHING_COMMANDS["if-goto"].replace("<label>", labelname)

    # call <funcname> <nArgs>
    elif operation == "call":
        to_replace = {
            "<fname>": CURRENT_FUNCTION,
            "<index>": CURRENT_FUNCTION_INDEX,
            "<nArgs>": parsed_instruction[2]
        }

        # Updating index if current function
        CURRENT_FUNCTION_INDEX += 1

        decoded_instruction = FUNCTION_COMMANDS["call"]
        for element in to_replace:
            decoded_instruction = decoded_instruction.replace(element, str(to_replace[element]))

        return decoded_instruction

    # function <funcname> <nVars>
    elif operation == "function":
        function = parsed_instruction[1]

        # Reseting index for new function
        CURRENT_FUNCTION_INDEX = 0
        CURRENT_FUNCTION = function

        # have to print the value nVars times
        decoded_instruction = ""
        for iteration in range(int(parsed_instruction[2])):
            decoded_instruction += FUNCTION_COMMANDS["function"]

        return decoded_instruction

    # return
    elif operation == "return":
        return FUNCTION_COMMANDS["return"]

    else:
        print(operation)  # for debugging
        print("yet to implement")

if __name__ == "__main__":
    print("""
    Cannot be used independently.

    Use the VMTranslator or pass parser input
    by importing to another file

    main(parsed_instruction, filename)
    """)
