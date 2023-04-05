from tkinter import *
from tkinter import messagebox as MessageBox  

def m_fecha ():
    MessageBox.showinfo("  Atención!","""No se encuentran datos para 
la fecha seleccionada en ION 1 y 2""") 

def m_fecha1 ():
    MessageBox.showinfo("  Atención!","""No se encuentran datos para 
la fecha seleccionada en ION 1""") 

def m_fecha2 ():
    MessageBox.showinfo("  Atención!","""No se encuentran datos para 
la fecha seleccionada en ION 2""") 

def mensaje_muestras ():
    MessageBox.showinfo("  Atención!","Hay menos de 96 datos en el ION 1")

def mensaje_muestras_2 ():
    MessageBox.showinfo("  Atención!","Hay menos de 96 datos en el ION 2")

def mensaje_muestras_3 ():
    MessageBox.showinfo("  Atención!","Hay más de 96 datos en el ION 1")
    
def mensaje_muestras_4 ():
    MessageBox.showinfo("  Atención!","Hay más de 96 datos en el ION 2")

def not_file (n_file):

    MessageBox.showinfo("  Atención!","No se encuentra el archivo {} en la carpeta".format(n_file))

