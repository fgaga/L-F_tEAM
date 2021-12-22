#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""NOTA :
    
    """
from /home/bravo/Escritorio/Fatima/Final
from models import *
class menuVentanas(ventana):
    def __init__(self,ventana):
        self.posicion=0
        self.array=[[()]]
        self.ventana=ventana
    
    def abrirArchivo(self):
        mensaje=""
        self.select_file()
          
        
        
        
    def seleccionarArchivo(self):
            filetypes = (
            ('Archivos de texto', '*.txt'),
           # ('All files', '*.*')
            )
    
            filename = fd.askopenfilename(
            title='Abrir archivo',
            initialdir=self.calcularRutaentrada(),
            filetypes=filetypes)  
            return filename 
    
    def calcularRutaentrada(self):
          return '/home/'+str(os.listdir("/home")[0])
 