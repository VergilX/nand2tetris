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
                    "M=M-1\n"   \
                    "A=M\n"     \
                    "D=M\n"     \
                    "A=A-1\n"   \
                    "M=D+M\n",

        "sub"   :   "@SP\n"     \
                    "M=M-1\n"   \
                    "A=M\n"     \
                    "D=M\n"     \
                    "A=A-1\n"   \
                    "M=M-D\n",

        "neg"   :   "@SP\n"     \
                    "M=M-1\n"   \
                    "A=M\n"     \
                    "M=-M\n"    \
                    "@SP\n"     \
                    "M=M+1\n",

        "comp"    : "@SP\n"         \
                    "M=M-1\n"       \
                    "A=M\n"         \
                    "D=M\n"         \
                    "A=A-1\n"       \
                    "D=M-D\n\n"     \
                                    \
                    "@TRUE<val>\n"  \
                    "D;<jmp>\n"       \
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
                    "(END<val>)\n",

        "and"   :   "@SP\n"     \
                    "M=M-1\n"   \
                    "A=M\n"     \
                    "D=M\n"     \
                    "A=A-1\n" \
                    "M=M&D\n",

        "or"    :   "@SP\n"     \
                    "M=M-1\n"   \
                    "A=M\n"     \
                    "D=M\n"     \
                    "A=A-1\n"   \
                    "M=M|D\n",

        "not"   :   "@SP\n"     \
                    "M=M-1\n"   \
                    "A=M\n"     \
                    "M=!M\n"    \
                    "@SP\n"     \
                    "M=M+1\n",

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
                        "D=A\n"         \
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
                        "D=A\n"         \
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

# Branching commands
BRANCHING_COMMANDS = {
        "label"     :   "(<label>)\n",

        "goto"      :   "@<label>\n"    \
                        "0;JMP\n",

        "if-goto"   :   "@SP\n"         \
                        "M=M-1\n"       \
                        "A=M\n"         \
                        "D=!M\n"        \
                        "@<label>\n"    \
                        "D;JNE\n"
                        }

# Function commands
FUNCTION_COMMANDS = {
        "call"      :   # push retAddr
                        # Foo.ret$1
                        "@<fname>$ret.<index>\n"        \
                        "D=A\n"                         \
                        "@SP\n"                         \
                        "A=M\n"                         \
                        "M=D\n"                         \
                        "@SP\n"                         \
                        "M=M+1\n"                       \

                        # push LCL
                        "@LCL\n"        \
                        "D=M\n"         \
                        "@SP\n"         \
                        "A=M\n"         \
                        "M=D\n"         \
                        "@SP\n"         \
                        "M=M+1\n"       \

                        # push ARG
                        "@ARG\n"        \
                        "D=M\n"         \
                        "@SP\n"         \
                        "A=M\n"         \
                        "M=D\n"         \
                        "@SP\n"         \
                        "M=M+1\n"       \

                        # push THIS
                        "@THIS\n"       \
                        "D=M\n"         \
                        "@SP\n"         \
                        "A=M\n"         \
                        "M=D\n"         \
                        "@SP\n"         \
                        "M=M+1\n"       \

                        # push THAT
                        "@THAT\n"       \
                        "D=M\n"         \
                        "@SP\n"         \
                        "A=M\n"         \
                        "M=D\n"         \
                        "@SP\n"         \
                        "M=M+1\n"       \

                        # ARG = SP-5-nArgs
                        "@5\n"          \
                        "D=A\n"         \
                        "@SP\n"         \
                        "D=M-D\n"       \
                        "@<nArgs>\n"    \
                        "D=D-A\n"       \
                        "@ARG\n"        \
                        "M=D\n"         \

                        # LCL = SP
                        "@SP\n"         \
                        "D=M\n"         \
                        "@LCL\n"        \
                        "M=D\n"         \

                        # goto <fname>
                        "@<fname>\n"    \
                        "0;JMP\n",

                        # add (returnAddress) in decoder

        "function"  :   # push 0 (multiply with nVars in decoder)
                        "@SP\n"         \
                        "A=M\n"         \
                        "M=0\n"         \
                        "@SP\n"         \
                        "M=M+1\n",

        "return"    :   # endframe = LCL
                        "@LCL\n"        \
                        "D=M\n"         \
                        "@R13\n"        \
                        "M=D\n"         \

                        # retaddr = *(endframe-5)
                        "@5\n"          \
                        "D=A\n"         \
                        "@R13\n"        \
                        "A=M-D\n"       \
                        "D=M\n"         \
                        "@R14\n"        \
                        "M=D\n"         \

                        # *ARG = pop()
                        "@SP\n"         \
                        "M=M-1\n"       \
                        "A=M\n"         \
                        "D=M\n"         \
                        "@ARG\n"        \
                        "A=M\n"         \
                        "M=D\n"         \

                        # SP = ARG+1
                        "@ARG\n"        \
                        "D=M+1\n"       \
                        "@SP\n"         \
                        "M=D\n"         \

                        # THAT = *(endframe-1)
                        "@1\n"          \
                        "D=A\n"         \
                        "@R13\n"        \
                        "A=M-D\n"       \
                        "D=M\n"         \
                        "@THAT\n"       \
                        "M=D\n"         \

                        # THIS = *(endframe-2)
                        "@2\n"          \
                        "D=A\n"         \
                        "@R13\n"        \
                        "A=M-D\n"       \
                        "D=M\n"         \
                        "@THIS\n"       \
                        "M=D\n"         \

                        # ARG = *(endframe-3)
                        "@3\n"          \
                        "D=A\n"         \
                        "@R13\n"        \
                        "A=M-D\n"       \
                        "D=M\n"         \
                        "@ARG\n"        \
                        "M=D\n"         \

                        # LCL = *(endframe-4)
                        "@4\n"          \
                        "D=A\n"         \
                        "@R13\n"        \
                        "A=M-D\n"       \
                        "D=M\n"         \
                        "@LCL\n"        \
                        "M=D\n"         \

                        # goto returnaddress
                        "@R14\n"        \
                        "A=M\n"         \
                        "0;JMP\n"
                        }
