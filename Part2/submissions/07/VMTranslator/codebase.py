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
PUSH_COMMANDS =  {
        "constant"   :   "@<val>\n"     \
                         "D=A\n"        \
                         "@SP\n"        \
                         "A=M\n"        \
                         "M=D\n"        \
                         "@SP\n"        \
                         "M=M+1\n",

        # includes local, argument, this, that
        "segment"    :  "@<reg>\n"      \
                        "D=M\n"         \
                        "@<val>\n"      \
                        "A=A+D\n"       \
                        "D=M\n"         \
                        "@SP\n"         \
                        "A=M\n"         \
                        "M=D\n"         \
                        "@SP\n"         \
                        "M=M+1\n",

        # has a fixed base address 5
        "temp"      :   "@5\n"          \
                        "D=M\n"         \
                        "@<val>\n"      \
                        "A=A+D\n"       \
                        "D=M\n"         \
                        "@SP\n"         \
                        "A=M\n"         \
                        "M=D\n"         \
                        "@SP\n"         \
                        "M=M+1\n",

        # replace i(<val>) with register of THIS/THAT
        # corresponding to 0/1 in decoder
        "pointer"   :   "@<val>\n"      \
                        "A=M\n"         \
                        "D=M\n"         \
                        "@SP\n"         \
                        "A=M\n"         \
                        "M=D\n"         \
                        "@SP\n"         \
                        "M=M+1\n",

        "static"    :   "@<file.i>\n"   \
                        "D=M\n"         \
                        "@SP\n"         \
                        "A=M\n"         \
                        "M=D\n"         \
                        "@SP\n"         \
                        "M=M+1\n"
        }

POP_COMMANDS = {
        # includes local, argument, this and that
        "segment"   :   "@<reg>\n"       \
                        "D=M\n"          \
                        "@<val>\n"       \
                        "D=D+A\n"        \
                        "@SP\n"          \
                        "M=M-1\n"        \
                        "A=M\n"          \
                        "A=M\n"          \
                        "A=A+D\n"        \
                        "D=A-D\n"        \
                        "A=A-D\n"        \
                        "M=D\n",

        # has fixed base address of 5
        "temp"      :   "@5\n"          \
                        "D=M\n"         \
                        "@<val>\n"      \
                        "D=D+A\n"       \
                        "@SP\n"         \
                        "M=M-1\n"       \
                        "A=M\n"         \
                        "A=M\n"         \
                        "A=A+D\n"       \
                        "D=A-D\n"       \
                        "A=A-D\n"       \
                        "M=D\n",

        # replace i(<val>) with register of THIS/THAT
        # corresponding to 0/1 in decoder
        "pointer"   :   "@SP\n"         \
                        "M=M-1\n"       \
                        "A=M\n"         \
                        "D=M\n"         \
                        "@<val>\n"      \
                        "M=D\n",

        "static"    :   "@SP\n"         \
                        "M=M-1\n"       \
                        "A=M\n"         \
                        "D=M\n"         \
                        "@<file.i>\n"   \
                        "M=D\n"
        }
