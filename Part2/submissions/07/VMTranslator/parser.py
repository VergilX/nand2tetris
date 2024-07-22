"""
Parser for VMTranslator

Author: @abhinanddmanoj
Date: 26 Dec 2023

GUIDELINES:
-> Divide lines into lexical expressions
-> Returns codes based on codebase.py

RETURN VALUE:
    list( <operation_code>, [<segment_code>, <value>] )

"""

import sys

def remove_whitespace(instruction):
    """
        Input: instruction without comments
        Output: list
    """

    instruction = instruction.strip()
    return [element.strip() for element in instruction.split()]


def remove_comments(instruction):
    length  = len(instruction)

    for index in range(length-2):
        if instruction[index:index+2] == "//":
            return instruction[:index].strip()

    # If there is not content
    return instruction

def main(instruction):
    """ Driving code """

    """
    components[0] : operation
    components[1] : segmentPointer/label/funcname
    components[2:]: arguments
    """
    components = remove_whitespace(remove_comments(instruction))

    # If no content
    if components == []:
        return ""

    return components

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 parser.py \"instruction\"")
    else:
        print( main(sys.argv[1]) )
