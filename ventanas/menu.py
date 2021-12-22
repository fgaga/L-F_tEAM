#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 20:52:05 2021

@author: bravo
""" 
from tkinter import * 
from models.ventana import ventana
class menu ():
    def __init__(self): 
        self.avisos()
        self.crearTk()
        self.crearBotones() 
        self.Calculator.mainloop()
        
        
    def crearTk(self):
        self.Calculator = Tk()
        self.Calculator.title("AdictoCalculator") 
        self.Calculator.config(cursor="arrow")
    
    def aviso (self,m):
        self.mensaje()
        self.crearBotones()
    def crearBotones(self,fun):
        n=Button(self.Calculator, font=("Arial", 12), fg='red', text="Calculadora", highlightbackground='lightgrey', command=lambda: fun())
        n.grid(row=5, column=0, columnspan=20)
    
    def mensaje(self):
        label = Label(self.Calculator, font=("Arial", 12), fg='black',bg='blue', text='    This is a label      ')
        label.grid(row=0, column=7, columnspan=20)
        
    
    def opcion(self,n):
        self.Calculator.destroy()
        self.crearTk()
        Pycalc(self.Calculator) 
        
    def clear_frame(self):
        for widgets in self.Calculator.winfo_children():
            widgets.destroy()

a=ventana()