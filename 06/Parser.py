# -*- coding: utf-8 -*-
"""
Created on Mon May 22 06:24:04 2017

@author: Ram Limbu

@Purpose: To parse assembly files

To Do:
    
1) When creating target filename, use os rutines to get src filename
    only, i.e. it should work if users type '.\filename.ext' or 'filename.ext'.
    Currently, only the latter case works    

2) Optional: Ensure assembly file uses valid command types, i.e. command types 
    are one of the three valid command types
3) Optional: Check that commands only use expected symbols and literals   
    
"""

#define Parser class to handle assembly file parsing routines
class Parser():
    '''Class to provide Hack assembly file parsing routines'''
    def __init__(self, srcFileName=None):
        self.srcFileName = srcFileName
        self.trgFileName = srcFileName.split('.')[0]+'.hack' 
        self.allCommands = self.readFile()
        self.currCommand = None
      
    # helper methods used within the class
    def readFile(self):
        '''Read file into a list, with each rec a list item'''
        if self.srcFileName is None:
            return None             
        recs = []
        with open(self.srcFileName, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # ignore comments, i.e. lines that start with '//'
                if not line.startswith('//'):
                    # ignore blank lines
                    if line:
                        # ignore comments started after commands
                        rec = line.split('//',2)[0].strip()
                        # remove space from the middle of the commmands, 
                        # i.e. change D + 1 to D+1
                        rec = "".join(rec.split())
                        recs.append(rec)
            return recs 
            
    def hasMoreCommands(self):
        '''Returns True if there are more commands. Else, it returns False'''
        if self.allCommands:
            return self.currCommand is None or self.currCommand < (len(self.allCommands) - 1)
        else:
            return False
    
    def advance(self):
        '''Advances the command pointer to the next command if it exists'''
        if self.hasMoreCommands():
            if self.currCommand is None:
                self.currCommand = 0
            else:
                self.currCommand = self.currCommand + 1      
    
    def resetCurrCommand(self):
        '''Sets command pointer'''            
        self.currCommand = None
        
        
    def commandType(self):
        '''Returns current command type
           To Do: Add regex() to make the following more robust, including
           checking for valid syntax
        '''         
        if self.allCommands[self.currCommand].startswith('@'):
            return 'A_COMMAND'
        elif self.allCommands[self.currCommand].startswith('('):
            return 'L_COMMAND'
        elif self.allCommands[self.currCommand][0] in {'D','A','M','0','-1','!'}:
            return 'C_COMMAND'
        else: 
            return 'U_COMMAND'
            
    
    def symbol(self):
        '''returns the symbol or decimal XXX of current command @Xxx or (Xxx).
        Should be called only when commandType() returns A_COMMAND
        or L_COMMAND'''
        currCommandType = self.commandType()
        if currCommandType == 'L_COMMAND':
            return self.allCommands[self.currCommand][1:-1]
        elif currCommandType == 'A_COMMAND':
            return self.allCommands[self.currCommand][1:]
        else:
            return None
    def dest(self):
        '''Returns the dest mnemonic in the current C-command.'''
        if not self.commandType() == 'C_COMMAND': return None
        if '=' in self.allCommands[self.currCommand]:
            return self.allCommands[self.currCommand].split('=')[0]
        else:
            return None
    
    def comp(self):
        '''Returns comp mnemonic in the current C-instruction'''
        if not self.commandType() == 'C_COMMAND': return None
        currInstruction = self.allCommands[self.currCommand]                            
        if '=' in currInstruction:
            currInstruction = currInstruction.split('=')[1]
        if ';' in currInstruction:
            currInstruction = currInstruction.split(';')[0]
        return currInstruction
    
    def jump(self):
        '''Returns the jump mnemonic when
        commandType() is C_COMMAND'''
        if not self.commandType() == 'C_COMMAND': return None    
        currInstruction = self.allCommands[self.currCommand]    
        if ';' in currInstruction:    
            return currInstruction.split(';')[1]
        else:
            return None
            
            
if __name__ == '__main__':
    pass