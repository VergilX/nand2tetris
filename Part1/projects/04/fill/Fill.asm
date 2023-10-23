// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(START)
    // Initalizing values
    @SCREEN
    D=A
    @address
    M=D
    @KBD
    D=M
    // If pressed or lifted
    @PRESS
    D;JNE
    @LIFT
    D;JEQ

    (PRESS)
        @i
        M=0

        (LOOPA)
            @i
            D=M
            @8192
            D=D-A
            @START
            D;JEQ

            @8192
            D=D+A
            D=D+1
            @i
            M=D

            @address
            A=M
            M=-1
            D=A
            D=D+1
            @address
            M=D
            @LOOPA
            0;JMP


    (LIFT)
        @i
        M=0

        (LOOPB)
            @i
            D=M
            @8192
            D=D-A
            @START
            D;JEQ

            @8192
            D=D+A
            D=D+1
            @i
            M=D

            @address
            A=M
            M=0
            D=A
            D=D+1
            @address
            M=D
            @LOOPB
            0;JMP
