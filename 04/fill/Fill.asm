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

// Put your code here.
// Completed: 2018-04-11

// initialize a variable with the total number of memory words on the Hack screen

(INIT)

@8192
D = A

@RAMS_covered
M = D

@SCREEN
D = A

@next_RAM
M = D

@KBD
D = M

// if a key is pressed, start filling the screen
@FILL
D;JNE

// if a key is not pressed, go to CLEAR
@CLEAR
0;JMP

(FILL)

@RAMS_covered
M = M - 1	

//if the screen has been filled, go to INIT 
@INIT
M;JLT

// fill the RAM pointed to by @next_RAM
@next_RAM
A = M
M = -1

// point to next RAM address to fill
@next_RAM
M = M + 1

@KBD
D = M

// if a key is pressed, keep filling the screen
@FILL
D;JNE


// if a key is not pressed, go to INIT routine
@INIT
D;JEQ

(CLEAR)

@RAMS_covered
M = M - 1	

//if the screen has been cleared, go to INIT 
@INIT
M;JLT

// clear the RAM address pointed to by @next_RAM
@next_RAM
A = M
M = 0

// point to next RAM to clear
@next_RAM
M = M + 1

@KBD
D = M

// if a key is not pressed, keep clearing the screen
@CLEAR
D;JEQ


// if a key is pressed, go to INIT routine
@INIT
D;JNE
