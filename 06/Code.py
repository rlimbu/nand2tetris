# -*- coding: utf-8 -*-
"""
Created on Wed May 24 07:07:41 2017

@author: Ram Limbu

@purpose: To translate assembly language mnemonics into binary codes

"""

class Code():
    '''Class to provide methods to translate assembly language
    mnemonics into binary codes'''
    def __init__(self):
        '''init dictionaries to hold destination, jump and compute binary codes'''
        self.destCode = {'NotStored':'000' 
                ,'M':'001'
                ,'D':'010'
                ,'MD':'011'
                ,'A':'100'
                ,'AM':'101'
                ,'AD':'110'
                ,'AMD':'111'
                }
        self.jumpCode = {'NoJump':'000'
                ,'JGT':'001'
                ,'JEQ':'010'
                ,'JGE':'011'
                ,'JLT':'100'
                ,'JNE':'101'
                ,'JLE':'110'
                ,'JMP':'111' 
                }
                
        self.compCode = {'0':'0101010'
                ,'1':'0111111'
                ,'-1':'0111010'
                ,'D':'0001100'
                ,'A':'0110000'
                ,'!D':'0001101'
                ,'!A':'0110001'
                ,'-D':'0001111'
                ,'-A':'0110011'
                ,'D+1':'011111'
                ,'A+1':'0110111'
                ,'D-1':'0001110'
                ,'A-1':'0110010'
                ,'D+A':'0000010'
                ,'D-A':'0010011'
                ,'A-D':'0000111'
                ,'D&A':'0000000'
                ,'D|A':'0010101'
                ,'M':'1110000'
                ,'!M':'1110001'
                ,'-M':'1110011'
                ,'M+1':'1110111'
                ,'M-1':'1110010'
                ,'D+M':'1000010'
                ,'D-M':'1010011'
                ,'M-D':'1000111'
                ,'D&M':'1000000'
                ,'D|M':'1010101'
                }
    
    def dest(self, strDest=None):
        '''Returns 3-bit binary code for destination'''
        if strDest is None:
            return self.destCode['NotStored']
        else:
            return self.destCode[strDest]

    def jump(self, strJump=None):
        '''Returns the 3-bit binary code of the jump mnemonic.'''
        if strJump is None:
            return self.jumpCode['NoJump']
        else:
            return self.jumpCode[strJump]
    
    def comp(self, strComp=None):
        '''Returns the 7-bit binary code for comp mnemonic'''
        if strComp is None: return None
        return self.compCode[strComp]
      