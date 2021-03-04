// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
@i
M=0

@R2
M=0

(LOOP)

// handle negative multiplication for R0
@R0
D=M
@END
D;JEQ

// handle negative multiplication for R1
@R1
D=M
@END
D;JEQ

@R0
D=M


// add to R2
@R2
M= M+D

// handle looping
@R1
D = M

@i
M = M+1
D = D-M

@LOOP
D;JGT

(END)
@END
0;JMP
