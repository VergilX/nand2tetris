"""
Parser for VMTranslator

Author: @abhinanddmanoj
Date: 26 Dec 2023

GUIDELINES:
-> Divide lines into lexical expressions
-> No whitespace or comments so easy
-> Returns codes based on codebase.py

RETURN VALUE:
    list( <operation_code>, [<segment_code>, <value>] )

"""
import sys

def main(instruction):
    """ Driving code """

    """
    components[0] : operation
    components[1] : segmentPointer
    components[2:]: arguments
    """
    components = instruction.split()

    # Arranging to format above mentioned format
    if len(components) > 2:
        # will cause issue in multiple args, deal with it later
        args = [int(elem) for elem in components[2:]]
        components = [components[0], components[1], args]

    return components

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 parser.py \"instruction\"")
    else:
        print( main(sys.argv[1]) )
