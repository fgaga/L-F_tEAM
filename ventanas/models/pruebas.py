#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 12:01:47 2021

@author: fatimagarcia
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 20:52:05 2021

@author: bravo
""" 
import os
import pickle
from tkinter import * 
from tkinter import filedialog as fd

"""El modelo ventana es creado para homogenizar los errores , lanzar avisos y sirve de clase padre
a los distintos menues ya que de esta forma usando este objeto de forma correcta
crearemos las dististintas ventanas usando grid"""


#Este objeto inicia el tk y sera heredado por los 
class ventana ():

    def __init__(self): 
        self.crearTk()  
        self.ventana.mainloop()
    """Todos creacion , reinicio , e introduccion de recursos"""
    def crearTk(self):
        self.ventana = Tk()
        self.ventana.title("Adictoventana") 
        self.ventana.config(cursor="arrow")
     
    def reiniciar(self):
        self.ventana.destroy()
        self.crearTk()
     
    def clear_frame(self):
        for widgets in self.ventana.winfo_children():
            widgets.destroy()
    
    """menu se encargara de complementar las funciones con los distintos
    elementos"""
    
    def crearBotones(self,texto,fun,pos): # Crea un boton con una funcion parametro
        n=Button(self.ventana, font=("Arial", 12), fg='red', text=texto, highlightbackground='lightgrey', command=lambda: fun())
        
        if(len(pos)==3): # Podemos darles dimension
             n.grid(row=pos[0], column=pos[1], columnspan=pos[2])
        else:
             n.grid(row=pos[0], column=pos[1])
    
    def mensajeCabezera(self,texto,pos): # Texto informativo
    
        label = Label(self.ventana, font=("Arial", 12), fg='black',bg='blue', text=texto)
        if(len(pos)==3):
             label.grid(row=pos[0], column=pos[1], columnspan=pos[2])
        else:
             label.grid(row=pos[0], column=pos[1])
     
    
             
""" 
    def insertarVentana(self,ventana):
         self.reiniciar()
         self.ventana=ventana
    
    
      
    def controlador (self):pass
        
    """
#
#
# open button
         

# run the application 

