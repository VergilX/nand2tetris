// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Put your code here.

@ans
M=0

@i
M=0

(LOOP)
    @R1
    D=M
    @i
    D=D-M
    @END
    D;JLE

    @ans
    D=M
    @R0
    D=D+M

    @ans
    M=D

    @i
    M=M+1

    @LOOP
    0;JMP

(END)
    @ans
    D=M
    @R2
    M=D
    @FIN
    0;JMP

(FIN)
    0;JMP
