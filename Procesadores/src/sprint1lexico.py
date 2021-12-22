#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 12:55:39 2021

@author: fatimagarcia
"""

class analisislexico():
    def __init__(self,texto):
        self.texto=texto
        self.T={     '+':('+','MAS') ,
                '-':('-','MENOS') ,
                '*':('*','POR') ,  
                '/':('/','DIVISION ') ,
                '(':('(',' ') ,
                ')':(')',' ') ,
                '{':('{',' ') ,
                '}':('}',' ') , 
                '=':('=',' ') ,
                '.':('.',' ') ,
                ';':(';',' ') ,
                '_':('_',' '), 
                '^':('',' ') ,
                }
        self.PalRes=(['raiz','cos','sen','tan','log','exp'])
        self.cad='' 
        self.listatokens=[]
    def initanal (self):
        contd=0
        while contd<len(self.texto): 
                aux=self.analizar(self.texto[contd])
                if (aux=='simbolo'):# Error
                    solucion=self.T.get(self.texto[contd],"Error")
                    if  solucion != "Error":
                        self.listatokens.append(solucion)
                    else: print ("eroro")
                    contd+=1
                    
                elif (aux=='numero'):
                     while contd<len(self.texto) and (self.analizar(self.texto[contd]))=='numero' :
                        self.cad+=self.texto[contd]
                        contd+=1 
                     self.meterToken('int')
                elif (self.analizar(self.texto[contd]))=='letra':
                     while contd<len(self.texto) and (self.analizar(self.texto[contd]))=='letra' :
                        self.cad+=self.texto[contd]
                        contd+=1
                    
                     self.meterToken('id')
                else :
                    contd+=1
                    print('error')
                
            
            
    def meterToken(self,a): 
        if(a=='int'):
            self.listatokens.append(((self.cad),'Num'))
        else:
            solucion= self.cad in self.PalRes
            if solucion:
                self.listatokens.append(('palres',self.cad))
            else :
                self.listatokens.append(('Id',self.cad))
        
        self.cad=''
        
    def gettoken(self):
        for (a,b) in self.listatokens:
            print ('<',a,',',b,'>')


    def analizar(self,caracter):
        resultado=''#creo una variable que almacenara el resultado
        if( caracter.isnumeric()):
            resultado='numero'
        elif(caracter.isalpha()):
            resultado='letra'
        else:
            resultado='simbolo'

        return resultado
    

prueba='(cosx≠)'
p1=analisislexico(prueba)
p1.initanal()
p1.gettoken()







