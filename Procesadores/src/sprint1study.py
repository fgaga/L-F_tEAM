#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:34:55 2021

@author: fatimagarcia

S -> delS	|      eol   |   +   |   ;   |   .   |   _   |   {   |   }   |   *    |   )   |   (   |   l T   |   d U   |   ^   |   =   |   / 
T -> l T    	| Lambda
U -> d U	| Lambda
"""

def leer(texto):
    for letra in texto:
        print (letra,analizar(letra))
    #creo una funcion que me dice si un caracter es una letra 
    

        
        #creamos un objeto
class analisislexico():
    def __init__(self):
        self.palabrasreservadas=(['raiz','cos','sen','tan','log','exp','(',')','{','}',':',';','.'])
        self.pal=''
        self.paltipo=''
        self.listatokens=[]
        self.terminales=['+','-','*','/','(',')']
    def initanal (self,texto):
        posicion=0
        while posicion <(len (texto)):
            while analizar(texto[posicion])=='letra':
                self.pal+=texto[posicion]
                posicion+=1
            
            posicion+=
            
          if (self.pal)=='':
             self.pal +=letra #concatenamos un texto.
             self.paltipo= self.analizar(caracter)
          else: 
              if self.analizar(letra)== self.paltipo:
                  self.pal +=letra
              elif self.
                  
              
              
    def analizar(self,caracter):
        resultado=''#creo una variable que almacenara el resultado
        if( caracter.isnumeric()):
            resultado='numero'
        elif(caracter.isalpha()):
            resultado='letra'
        else:
            resultado='simbolo'
            
        return resultado
        
        
        
        