# -*- coding: utf-8 -*-
"""
Created on Sun May 28 20:26:19 2017

@author: Ram Limbu
@Purpose: To hold symbols encountered while parsing assembly files
"""

class SymbolTable():
    '''The class to hold and manipulate symobls in assemly files'''
    
    def __init__(self):
        '''init method to initialize symbol table class'''
        self.symbols = {}
        self.symbols['SP'] = '0'
        self.symbols['LCL'] = '1'
        self.symbols['ARG'] = '2'
        self.symbols['THIS'] = '3'
        self.symbols['THAT'] = '4'
        self.symbols['SCREEN'] = '16384'
        self.symbols['KBD'] = '24576'
        self.symbols['R0'] = '0'
        self.symbols['R1'] = '1'
        self.symbols['R2'] = '2'
        self.symbols['R3'] = '3'
        self.symbols['R4'] = '4'
        self.symbols['R5'] = '5'
        self.symbols['R6'] = '6'
        self.symbols['R7'] = '7'
        self.symbols['R8'] = '8'
        self.symbols['R9'] = '9'
        self.symbols['R10'] = '10'
        self.symbols['R11'] = '11'
        self.symbols['R12'] = '12'
        self.symbols['R13'] = '13'
        self.symbols['R14'] = '14'
        self.symbols['R15'] = '15'

    
    def addEntry(self, symbol, address):
        '''Enter symbol and address if symbol  is not already present.'''
        if not symbol in self.symbols:
            self.symbols[symbol] = address

    def contains(self, symbol):
        '''Checks if the symbol exists in the symbol table'''
        return symbol in self.symbols
        
    def getAddress(self, symbol):
        '''Returns the address associated with the symbol'''
        return self.symbols[symbol]
        

if __name__ == '__main__':
    print("Please, import this file as a module")