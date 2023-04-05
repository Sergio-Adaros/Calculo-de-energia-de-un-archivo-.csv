from tkinter import *
from tkinter import messagebox as MessageBox  

def sinDatos1(sd1):
    MessageBox.showinfo("Atención!", "No se encuentran datos del ION 1 para éstos días: \n\n{}".format(sd1))

def sinDatos2(sd2):
    MessageBox.showinfo("Atención!", "No se encuentran datos del ION 2 para éstos días: \n\n{}".format(sd2))

def sinArchivo():
    MessageBox.showinfo("Atención!", "No se encuentra el archivo del ION 1 o 2 en la carpeta")


