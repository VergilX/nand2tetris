// 	push constant 0    
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	pop local 0         // sum = 0
@LCL
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
(inputLOOP)
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
// 	push local 0
@LCL
D=M
@0
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
// 	pop local 0	        // sum = sum + n
@LCL
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
// 	pop argument 0      // n--
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
// 	if-goto LOOP        // if n > 0, goto LOOP
@SP
M=M-1
A=M
D=!M
@inputLOOP
D;JNE
// 	push local 0        // else, pushes sum to the stack's top
@LCL
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
