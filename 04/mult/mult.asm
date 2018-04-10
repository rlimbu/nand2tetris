// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
// Completed: 2018-04-10

// initialise R2 to 0
@R2
M = 0

// initialise counter to R0
@R0
D = M
@ctr
M = D

(LOOP)

	// decrement counter, and if it's less than 0, end
	@ctr
	M = M - 1

	@END
	M;JLT
	
	// save the value of R1 in D register
	@R1
	D = M
	
	// perform D + R2, and save the result in R2
	@R2	
	M = M + D	
	
	@LOOP
	0;JMP
	
(END)

	@END
	0;JMP

