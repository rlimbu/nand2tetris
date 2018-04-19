# -*- coding: utf-8 -*-
"""
Created on Wed May 24 20:48:07 2017

@author: Ram Limbu
@Purpose: To convert assembly files into machine instructions

"""

import sys, Code, Parser, SymbolTable

if len(sys.argv) < 2:
	print("No assemly filename supplied. Exiting ...")
	sys.exit(0)
	
filename = sys.argv[1]
cd = Code.Code()
p = Parser.Parser(filename)
st = SymbolTable.SymbolTable()
outFile = p.trgFileName

# first pass to enter label variables and their ROM addresses into the symbol table
locROM = 0
for n, v in enumerate(p.allCommands):
    p.advance()
    if p.commandType() == 'L_COMMAND':
        sym = p.symbol()
        st.addEntry(sym, locROM)
    else:
        locROM = locROM + 1

# second pass to enter variables and their RAM addresses into the symbol table       
p.resetCurrCommand()
locRAM = 16
for c in p.allCommands:
    p.advance()
    if p.commandType() == 'A_COMMAND':
        sym = p.symbol()
        try:
            sym = int(sym)
        except ValueError:
            if not st.contains(sym): # check required so that locRAM increment works
                st.addEntry(sym, locRAM)
                locRAM = locRAM + 1        

# generate the binary codes.
# please, note: L_COMMANDs are ignored as they are not real commands, just place-holders
      
p.resetCurrCommand()        
with open(outFile, 'w') as f:
    while p.hasMoreCommands():     
        p.advance()
        if p.commandType() == 'A_COMMAND':
            a_symbol = p.symbol()            
            try:
                a_symbol = int(a_symbol)
            except ValueError:
                a_symbol = st.getAddress(a_symbol)
            line = "{0:016b}".format(int(a_symbol))
            f.write(line+'\n')
        elif p.commandType() == 'C_COMMAND':
            comp_symbol = p.comp()
            dest_symbol = p.dest()
            jmp_symbol = p.jump()
            line = '111'+cd.comp(comp_symbol)+cd.dest(dest_symbol)+cd.jump(jmp_symbol)
            f.write(line+'\n')
        


