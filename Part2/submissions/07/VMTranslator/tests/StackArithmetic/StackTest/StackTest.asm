// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// eq
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D

@TRUE0
D;JEQ
@FALSE0
0;JMP

(TRUE0)
@SP
A=M-1
M=-1
@END0
0;JMP

(FALSE0)
@SP
A=M-1
M=0
@END0
0;JMP

(END0)
// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 16 // Hello there!
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
// eq
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D

@TRUE1
D;JEQ
@FALSE1
0;JMP

(TRUE1)
@SP
A=M-1
M=-1
@END1
0;JMP

(FALSE1)
@SP
A=M-1
M=0
@END1
0;JMP

(END1)
// push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// eq
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D

@TRUE2
D;JEQ
@FALSE2
0;JMP

(TRUE2)
@SP
A=M-1
M=-1
@END2
0;JMP

(FALSE2)
@SP
A=M-1
M=0
@END2
0;JMP

(END2)
// push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// lt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D

@TRUE3
D;JLT
@FALSE3
0;JMP

(TRUE3)
@SP
A=M-1
M=-1
@END3
0;JMP

(FALSE3)
@SP
A=M-1
M=0
@END3
0;JMP

(END3)
// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
// lt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D

@TRUE4
D;JLT
@FALSE4
0;JMP

(TRUE4)
@SP
A=M-1
M=-1
@END4
0;JMP

(FALSE4)
@SP
A=M-1
M=0
@END4
0;JMP

(END4)
// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// lt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D

@TRUE5
D;JLT
@FALSE5
0;JMP

(TRUE5)
@SP
A=M-1
M=-1
@END5
0;JMP

(FALSE5)
@SP
A=M-1
M=0
@END5
0;JMP

(END5)
// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// gt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D

@TRUE6
D;JGT
@FALSE6
0;JMP

(TRUE6)
@SP
A=M-1
M=-1
@END6
0;JMP

(FALSE6)
@SP
A=M-1
M=0
@END6
0;JMP

(END6)
// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
// gt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D

@TRUE7
D;JGT
@FALSE7
0;JMP

(TRUE7)
@SP
A=M-1
M=-1
@END7
0;JMP

(FALSE7)
@SP
A=M-1
M=0
@END7
0;JMP

(END7)
// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// gt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D

@TRUE8
D;JGT
@FALSE8
0;JMP

(TRUE8)
@SP
A=M-1
M=-1
@END8
0;JMP

(FALSE8)
@SP
A=M-1
M=0
@END8
0;JMP

(END8)
// push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 53
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M
// push constant 112
@112
D=A
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D
// neg
@SP
M=M-1
A=M
M=-M
@SP
M=M+1
// and
@SP
M=M-1
A=M
D=M
A=A-1
M=M&D
// push constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
// or
@SP
M=M-1
A=M
D=M
A=A-1
M=M|D
// not
@SP
M=M-1
A=M
M=!M
@SP
M=M+1
