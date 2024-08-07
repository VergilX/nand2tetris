// 	push argument 1         // sets THAT, the base address of the
@ARG
D=M
@1
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// 	pop pointer 1           // that segment, to argument[1]
@SP
M=M-1
A=M
D=M
@THAT
M=D
// 	push constant 0         // sets the series' first and second
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	pop that 0              // elements to 0 and 1, respectively       
@THAT
D=M
@0
D=D+A
@SP
M=M-1
A=M
A=M
A=A+D
D=A-D
A=A-D
M=D
// 	push constant 1   
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	pop that 1              
@THAT
D=M
@1
D=D+A
@SP
M=M-1
A=M
A=M
A=A+D
D=A-D
A=A-D
M=D
// 	push argument 0         // sets n, the number of remaining elements
@ARG
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// 	push constant 2         // to be computed to argument[0] minus 2,
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	sub                     // since 2 elements were already computed.
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D
// 	pop argument 0          
@ARG
D=M
@0
D=D+A
@SP
M=M-1
A=M
A=M
A=A+D
D=A-D
A=A-D
M=D
// label LOOP
(input.null$LOOP)
// 	push argument 0
@ARG
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// 	if-goto COMPUTE_ELEMENT // if n > 0, goto COMPUTE_ELEMENT
@SP
M=M-1
A=M
D=!M
@input.null$COMPUTE_ELEMENT
D;JNE
// 	goto END                // otherwise, goto END
@input.null$END
0;JMP
// label COMPUTE_ELEMENT
(input.null$COMPUTE_ELEMENT)
// 	push that 0
@THAT
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// 	push that 1
@THAT
D=M
@1
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// 	add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M
// 	pop that 2
@THAT
D=M
@2
D=D+A
@SP
M=M-1
A=M
A=M
A=A+D
D=A-D
A=A-D
M=D
// 	push pointer 1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// 	push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M
// 	pop pointer 1 
@SP
M=M-1
A=M
D=M
@THAT
M=D
// 	push argument 0
@ARG
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// 	push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	sub
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D
// 	pop argument 0          
@ARG
D=M
@0
D=D+A
@SP
M=M-1
A=M
A=M
A=A+D
D=A-D
A=A-D
M=D
// 	goto LOOP
@input.null$LOOP
0;JMP
// label END
(input.null$END)
