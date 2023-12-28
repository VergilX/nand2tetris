"""
CodeBase for VMTranslator

Author: @abhinanddmanoj
Date: 26 Dec 2023

GUIDELINES:
- Contains codes for other files of VMTranslator to access
- Use keyword <val> for replacing with arbitrary value if required

RETURN VALUE:
    None
"""

# Arithmetic and Logical commands
AL_COMMANDS = {
        "add"   :   "@SP\n"     \
                    "A=M\n"     \
                    "D=M\n"     \
                    "A=A-1\n"   \
                    "M=D+M\n"   \
                    "@SP\n"     \
                    "M=M-1\n",

        "sub"   :   "@SP\n"     \
                    "A=M\n"     \
                    "D=M\n"     \
                    "A=A-1\n"   \
                    "M=M-D\n"   \
                    "@SP\n"     \
                    "M=M-1\n",

        "neg"   :   "@SP\n"     \
                    "A=M\n"     \
                    "M=-M\n",

        "eq"    :   "@SP\n"         \
                    "A=M\n"         \
                    "D=M\n"         \
                    "A=A-1\n"       \
                    "D=D-M\n\n"     \
                                    \
                    "@TRUE<val>\n"  \
                    "D;JEQ\n"       \
                    "@FALSE<val>\n" \
                    "0;JMP\n\n"     \
                                    \
                    "(TRUE<val>)\n"  \
                    "@SP\n"         \
                    "A=M-1\n"       \
                    "M=-1\n"        \
                    "@END<val>\n"   \
                    "0;JMP\n\n"     \
                                    \
                    "(FALSE<val>)\n" \
                    "@SP\n"         \
                    "A=M-1\n"       \
                    "M=0\n"         \
                    "@END<val>\n"   \
                    "0;JMP\n\n"         \
                                    \
                    "(END<val>)\n"  \
                    "@SP\n"         \
                    "M=M-1\n",

        "lt"    :   "@SP\n"         \
                    "A=M\n"         \
                    "D=M\n"         \
                    "A=A-1\n"       \
                    "D=D-M\n\n"     \
                                    \
                    "@TRUE<val>\n"  \
                    "D;JLT\n"       \
                    "@FALSE<val>\n" \
                    "0;JMP\n\n"     \
                                    \
                    "(TRUE<val>)\n"  \
                    "@SP\n"         \
                    "A=M-1\n"       \
                    "M=-1\n"        \
                    "@END<val>\n"   \
                    "0;JMP\n\n"     \
                                    \
                    "(FALSE<val>)\n" \
                    "@SP\n"         \
                    "A=M-1\n"       \
                    "M=0\n"         \
                    "@END<val>\n"   \
                    "0;JMP\n\n"         \
                                    \
                    "(END<val>)\n"  \
                    "@SP\n"         \
                    "M=M-1\n",

        "gt"    :   "@SP\n"         \
                    "A=M\n"         \
                    "D=M\n"         \
                    "A=A-1\n"       \
                    "D=D-M\n\n"     \
                                    \
                    "@TRUE<val>\n"  \
                    "D;JGT\n"       \
                    "@FALSE<val>\n" \
                    "0;JMP\n\n"     \
                                    \
                    "(TRUE<val>)\n"  \
                    "@SP\n"         \
                    "A=M-1\n"       \
                    "M=-1\n"        \
                    "@END<val>\n"   \
                    "0;JMP\n\n"     \
                                    \
                    "(FALSE<val>)\n" \
                    "@SP\n"         \
                    "A=M-1\n"       \
                    "M=0\n"         \
                    "@END<val>\n"   \
                    "0;JMP\n\n"         \
                                    \
                    "(END<val>)\n"  \
                    "@SP\n"         \
                    "M=M-1\n",

        "and"   :   "@SP\n"     \
                    "A=M\n"     \
                    "D=M\n"     \
                    "A=A-1\n" \
                    "M=M&D\n"   \
                    "@SP\n"     \
                    "M=M-1\n",

        "or"    :   "@SP\n"     \
                    "A=M\n"     \
                    "D=M\n"     \
                    "A=A-1\n"   \
                    "M=M|D\n"   \
                    "@SP\n"     \
                    "M=M-1\n",

        "not"   :   "@SP\n"     \
                    "A=M\n"     \
                    "M=!M\n"
        }

# Memory access commands
MEM_ACCESS_COMMANDS =  {
        "pop"   :   10,
        "push"  :   11
        }
