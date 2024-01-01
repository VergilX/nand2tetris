// Should contain address of SP, but using 0
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D

// Insert required variable letter
@TRUE_
D;JEQ // Replace with JGT for gt and JLT for lt
@FALSE_
0;JMP

(TRUE_)
    @SP
    A=M-1
    M=-1
    @END_
    0;JMP
(FALSE_)
    @SP
    A=M-1
    M=0
    @END_
    0;JMP

(END_)
