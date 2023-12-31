// pop local i
// addr=LCL+i, SP--, *addr=*SP
@1 // LCL
D=M
@2 // i
D=D+A
@0 // SP
M=M-1
A=M
A=M
// swapping
A=A+D
D=A-D
A=A-D
M=D // assigning to it

// ---------------------------------------------------------------------------------------

// pop argument i
// addr=ARG+i, SP--, *addr=*SP
@1 // ARG
D=M
@2 // i
D=D+A
@0 // SP
M=M-1
A=M
A=M

// swapping
A=A+D
D=A-D
A=A-D
M=D // assigning to it

// ---------------------------------------------------------------------------------------

// pop this i
// addr=THIS+i, SP--, *addr=*SP
@1 // THIS
D=M
@2 // i
D=D+A
@0 // SP
M=M-1
A=M
A=M

// swapping
A=A+D
D=A-D
A=A-D
M=D // assigning to it

// ---------------------------------------------------------------------------------------

// pop that i
// addr=THAT+i, SP--, *addr=*SP
@1 // THAT
D=M
@2 // i
D=D+A
@0 // SP
M=M-1
A=M
A=M

// swapping
A=A+D
D=A-D
A=A-D
M=D // assigning to it

// ---------------------------------------------------------------------------------------

// pop temp i
// addr=5+i, SP--, *addr=*SP
@5 // temp has constant base address 5
D=M
@2 // i
D=D+A
@0 // SP
M=M-1
A=M
A=M

// swapping
A=A+D
D=A-D
A=A-D
M=D // assigning to it

// ---------------------------------------------------------------------------------------

// pop pointer 0
@0 // SP
M=M-1
A=M
D=M
@3 // THIS
M=D

// ---------------------------------------------------------------------------------------

// pop pointer 1
@0 // SP
M=M-1
A=M
D=M
@4 // THAT
M=D

// ---------------------------------------------------------------------------------------

// pop static i
// Starts with address 16
@0 // SP
M=M-1
A=M
D=M
@15 // <file>.i
M=D
