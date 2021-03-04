// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

(BEGIN)

@8192
D=A
@i
M=D

@KBD
D = M

@BLACK
D;JGT

(WHITE)
    @i
    M=M-1
    D = M

    @SCREEN
    A = A + D
    M = 0

    @WHITE
    D;JGT

@BEGIN
0;JMP

(BLACK)
    @i
    M=M-1
    D = M

    @SCREEN
    A = A + D
    M = -1

    @BLACK
    D;JGT

    @BLACK
    D;JGT

@BEGIN
0;JMP