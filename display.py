from tkinter import *
from tkcalendar import *
from date import date
from ion_cal import calcular
import pyperclip                        
from popup import *
from intervalo import *

# todo: Definicion de funciones   
# * Función calendario
def calendario():

    def cambiar_fecha(): 

        global new_fecha

        new_fecha = cal.selection_get()
        new_fecha = new_fecha.strftime("%d-%m-%Y") 
        newDate.set(new_fecha)
        dateDinamic.set("Fecha: " + new_fecha)
        top.destroy()
        i_1.set('')
        i_2.set('')
        d_err.set('')
        d_err2.set('')
        h_star1.set('')
        h_fin1.set('')
        m_ion1.set('')
        h_star2.set('')
        h_fin2.set('')
        m_ion2.set('')

    top = Toplevel(root, bg=colorFondo)
    top.title("Calendario".center(110))
    top.iconbitmap('icono.ico')
    top.resizable(0,0)
    listaFecha = d_y.split('-')
    top.geometry(str(w_Windows-200)+"x"+str(h_Windows-260)+"+"+str(p_width+100)+"+"+str(p_height+100))

    cal = Calendar(top, font=(fuente, tamañoLetras), selectmode='day', locale='es',
                   cursor="arrow", year=int(listaFecha[2]), month=int(listaFecha[1]), day=int(listaFecha[0]),)

    cal.pack(fill="both", expand=0)
    Button(top, text="OK", font=(fuente, tamañoBotones), bg=colorBoton, width=14, command=cambiar_fecha).pack(pady=5)

# * Funcion para llamar al calculo de datos del ion
def obtencionDatos(f): 

    try:
            
        global copiarIon1
        global copiarIon2

        nueva_fecha = f.get()

        l_dat_ion = calcular(nueva_fecha)                      

        i1 = l_dat_ion[0][0]                        
        i2 = l_dat_ion[1][0] 

        i_1.set(round(i1, 3))                      
        i_2.set(round(i2, 3))                        

        h_star1.set(l_dat_ion[0][3])
        h_fin1.set(l_dat_ion[0][4])

        m_ion1.set(str(l_dat_ion[0][2]) + " de 96")

        h_star2.set(l_dat_ion[1][3])
        h_fin2.set(l_dat_ion[1][4])

        m_ion2.set(str(l_dat_ion[1][2]) + " de 96")

        copiarIon1 = str(l_dat_ion[0][0])
        copiarIon1 = copiarIon1.replace('.', ',')
        copiarIon2 = str(l_dat_ion[1][0])
        copiarIon2 = copiarIon2.replace('.', ',')
        
        if l_dat_ion[0][2] != 0 or l_dat_ion[1][2] != 0:

            if l_dat_ion[0][2] < 96 and l_dat_ion[0][2] != 0:
                mensaje_muestras()
                i_1.set("Datos incompletos")
                i_2.set("Datos incompletos")
                pyperclip.copy("")
                error_label()
            elif l_dat_ion[0][2] > 96:
                mensaje_muestras_3()
                i_1.set("Datos incorrectos")
                pyperclip.copy("")
                error_label()

            if l_dat_ion[1][2] < 96 and l_dat_ion != 0:
                mensaje_muestras_2()
                i_1.set("Datos incompletos")
                i_2.set("Datos incompletos")
                pyperclip.copy("")  
                error_label2()
            elif l_dat_ion[1][2] > 96:
                mensaje_muestras_4()
                i_2.set("Datos incorrectos")
                pyperclip.copy("")
                error_label2()

            if l_dat_ion[0][2] == 0:
                m_fecha1()
                i_1.set("Sin datos")
                pyperclip.copy("")
                error_label()

            if l_dat_ion[1][2] == 0:
                m_fecha2()
                i_2.set("Sin datos")
                pyperclip.copy("")
                error_label2()

        else:
            m_fecha()
            i_1.set("Sin datos")
            i_2.set("Sin datos")
            pyperclip.copy("")
            error_label()
            error_label2()
    
    except:
        pass

# * Funcion copiar
def copiar1():
    a = i_1.get()
    b = i_2.get()
    c = m_ion1.get()
    c = int(c[:2])
    if a != b and c == 96:
        pyperclip.copy(copiarIon1)
    else:
        pyperclip.copy("")
   
def copiar2():
    a = i_1.get()
    b = i_2.get()
    c = m_ion2.get()
    c = int(c[:2])
    if a != b and c == 96:
        pyperclip.copy(copiarIon2)
    else:
        pyperclip.copy("")

# * Función error label

def error_label():
    d_err.set("""Revisa si se encuentra el archivo en
la carpeta o intenta con otra fecha.""")
    error = Label(f_inferior_left, textvariable=d_err, font=(fuente, tamañoLetras), bg='#fff7be', width=30, height=3, borderwidth=1, relief="groove")
    error.grid(row=6, column=0, columnspan=2, rowspan=3, padx=pdx)
def error_label2():
    d_err2.set("""Revisa si se encuentra el archivo en
la carpeta o intenta con otra fecha.""")
    error = Label(f_inferior_right, textvariable=d_err2, font=(fuente, tamañoLetras), bg='#fff7be', width=30, height=3, borderwidth=1, relief="groove")
    error.grid(row=6, column=0, columnspan=2, rowspan=3, padx=pdx)

# todo: Formato
# Colores
colorFondo = '#D3DCF0'
colorLabel = '#D3E0ED'
colorBoton = '#D3E0ED'
colorRoot = '#D3DCF0'
# Fuentes
fuente = "Calibri"
tamañoLetras = 13
tamañoBotones = 13
# Diseño botones
colorActive = '#818181'

# todo: Definiendo el root y sus caracterízticas
root = Tk()                                   
root.title("Datos ION".center(170))  
root.iconbitmap("icono.ico")                      
root.resizable(0,0)                 
root.config(bd=10, bg=colorRoot, relief='ridge')
# Extracción de datos del tamaño de la pantalla
w_total = root.winfo_screenwidth()    
h_total = root.winfo_screenheight()   
# definición tamaño de la ventana
w_Windows = 650   
h_Windows = 550
# Calculo para la posición de la ventana root
p_width = round(w_total/2-w_Windows/2)
p_height = round(h_total/2-h_Windows/2)
# Configurando el tamaño y posición del root
root.geometry(str(w_Windows)+"x"+str(h_Windows)+"+"+str(p_width)+"+"+str(p_height)) 

# todo: llamada a funcion fecha
d_y, d_t = date()

# todo: Definicion de variables
newDate = StringVar()
newDate.set(d_y)
dateDinamic = StringVar()
dateDinamic.set("fecha:  " + d_y)  

i_1 = StringVar()                                 
i_2 = StringVar()

h_star1 = StringVar()
h_fin1 = StringVar()
m_ion1 = StringVar ()

h_star2 = StringVar()
h_fin2 = StringVar()
m_ion2 = StringVar ()

d_err = StringVar()
d_err2 = StringVar() 

# todo: Parte superior
# Definición tamaño del frame superior
ws_matriz = (w_Windows/1.0317460317)
hs_matriz = (h_Windows/5)
# Creación de columnas superior que contiene la fecha, el boton calcular y la versión del software
f_superior = Frame(root, width=ws_matriz, height=hs_matriz)
f_superior.grid(row=0, columnspan=2)
# Columnas y filas dentro de f_superior
tw_frame_superior = ws_matriz/2
th_frame_superior = hs_matriz/3

for column in range(2):  
    for fila in range(3):
        sf_superior = Frame(f_superior, width=tw_frame_superior, height=th_frame_superior)
        sf_superior.grid(column=column, row=fila)
        sf_superior.configure(bg=colorFondo)
# Boton calcular, fecha y versión del software - en la parte superior dentro de f_superior
dateF_superior = Button(f_superior, textvariable=dateDinamic, command=calendario ,font=(fuente, tamañoLetras), fg='#082a8c', bg=colorFondo, width=17, borderwidth=1, relief="raised")
dateF_superior.grid(row=0, column=1, sticky='ne', padx=10, pady=10, rowspan=2)

b_calcular = Button(f_superior, text="Calcular", height=1, width=10,font=(fuente, tamañoBotones),command=lambda: obtencionDatos(newDate), bg=colorBoton)  
b_calcular.grid(row=0, columnspan=2,rowspan=3)

version = Label(f_superior, text="  Version 2", font=(fuente, 9), bg=colorFondo)
version.grid(row=0, columnspan=2, sticky='nw')

n_ion1 = Label(f_superior, text="Datos ION 1", font=(fuente, tamañoLetras), bg=colorFondo)
n_ion1.grid(row=2, column=0)

n_ion2 = Label(f_superior, text="Datos ION 2", font=(fuente, tamañoLetras), bg=colorFondo)
n_ion2.grid(row=2, column=1)

# todo: Parte central
# Creación de datos ion izquierdo y derecho
wi_matriz = (w_Windows/2.0967741935)
hi_matriz = (h_Windows/1.6176470588)
# Lado izquierdo frame principal
f_inferior_left = Frame(root, width=wi_matriz, height=hi_matriz)
f_inferior_left.grid(column=0, row=2, rowspan=2, pady=4)
f_inferior_left.configure(bg=colorFondo, relief='ridge', bd=5)
f_inferior_left.grid_propagate(False)
# Tamaño de las celdas
tw_fInf = (wi_matriz/2)-6
th_fInf = (hi_matriz/9)-1.5
# Creación de columnas y filas
for column in range(2):  
    for fila in range(9):
        sf_superior = Frame(f_inferior_left, width=tw_fInf, height=th_fInf)
        sf_superior.grid(column=column, row=fila)
        sf_superior.configure(bg=colorFondo)

# padx de los label
pdx = 10
# label del lado izquierdo
fecha_i1 = Label(f_inferior_left, text="Fecha", font=(fuente, tamañoLetras), bg=colorFondo)
fecha_i1.grid(row=1, column=0, sticky='w', padx=pdx)

Dfecha_i1 = Label(f_inferior_left, textvariable=newDate, font=(fuente, tamañoLetras), width=14, bg=colorFondo, fg='#082a8c', borderwidth=1, relief="sunken")
Dfecha_i1.grid(row=1, column=1, sticky='w', padx=pdx)

totalMW_i1 = Label(f_inferior_left, text="Total MW", font=(fuente, tamañoLetras), bg=colorFondo)
totalMW_i1.grid(row=2, column=0, sticky='w', padx=pdx)

DtotalMW_i1 = Label(f_inferior_left, textvariable=i_1, font=(fuente, tamañoLetras), width=14,bg=colorFondo, borderwidth=1, relief="sunken")
DtotalMW_i1.grid(row=2, column=1, sticky='w', padx=pdx)

primerDat_i1 = Label(f_inferior_left, text="Hora primer dato", font=(fuente, tamañoLetras), bg=colorFondo)
primerDat_i1.grid(row=3, column=0, sticky='w', padx=pdx)

DprimerDat_i1 = Label(f_inferior_left, textvariable=h_star1, font=(fuente, tamañoLetras), width=14,bg=colorFondo, borderwidth=1, relief="sunken")
DprimerDat_i1.grid(row=3, column=1, sticky='w', padx=pdx)

ultimoDat_i1 = Label(f_inferior_left, text="Hora último dato", font=(fuente, tamañoLetras), bg=colorFondo)
ultimoDat_i1.grid(row=4, column=0, sticky='w', padx=pdx)

DultimoDat_i1 = Label(f_inferior_left, textvariable=h_fin1, font=(fuente, tamañoLetras), width=14,bg=colorFondo, borderwidth=1, relief="sunken")
DultimoDat_i1.grid(row=4, column=1, sticky='w', padx=pdx)

datTomados_i1 = Label(f_inferior_left, text="Datos tomados", font=(fuente, tamañoLetras), bg=colorFondo)
datTomados_i1.grid(row=5, column=0, sticky='w', padx=pdx)

DdatTomados_i1 = Label(f_inferior_left, textvariable=m_ion1, font=(fuente, tamañoLetras), width=14,bg=colorFondo, borderwidth=1, relief="sunken")
DdatTomados_i1.grid(row=5, column=1, sticky='w', padx=pdx)

# Lado derecho
f_inferior_right = Frame(root, width=wi_matriz, height=hi_matriz)
f_inferior_right.grid(column=1,row=1, rowspan=2, pady=4)
f_inferior_right.configure(bg=colorFondo, relief='ridge', bd=5)
f_inferior_right.grid_propagate(False)
# Creación de filas y columnas
for column in range(2):  
    for fila in range(9):
        sf_superior = Frame(f_inferior_right, width=tw_fInf, height=th_fInf)
        sf_superior.grid(column=column, row=fila)
        sf_superior.configure(bg=colorFondo)
# Labels del lado derecho
fecha_i2 = Label(f_inferior_right, text="Fecha", font=(fuente, tamañoLetras), bg=colorFondo)
fecha_i2.grid(row=1, column=0, sticky='w', padx=pdx)

Dfecha_i2 = Label(f_inferior_right, textvariable=newDate, font=(fuente, tamañoLetras), width=14, bg=colorFondo, fg='#082a8c', borderwidth=1, relief="sunken")
Dfecha_i2.grid(row=1, column=1, sticky='w', padx=pdx)

totalMW_i2 = Label(f_inferior_right, text="Total MW", font=(fuente, tamañoLetras), bg=colorFondo)
totalMW_i2.grid(row=2, column=0, sticky='w', padx=pdx)

DtotalMW_i2 = Label(f_inferior_right, textvariable=i_2, font=(fuente, tamañoLetras), width=14,bg=colorFondo, borderwidth=1, relief="sunken")
DtotalMW_i2.grid(row=2, column=1, sticky='w', padx=pdx)

primerDat_i2 = Label(f_inferior_right, text="Hora primer dato", font=(fuente, tamañoLetras), bg=colorFondo)
primerDat_i2.grid(row=3, column=0, sticky='w', padx=pdx)

DprimerDat_i2 = Label(f_inferior_right, textvariable=h_star2, font=(fuente, tamañoLetras), width=14,bg=colorFondo, borderwidth=1, relief="sunken")
DprimerDat_i2.grid(row=3, column=1, sticky='w', padx=pdx)

ultimoDat_i2 = Label(f_inferior_right, text="Hora último dato", font=(fuente, tamañoLetras), bg=colorFondo)
ultimoDat_i2.grid(row=4, column=0, sticky='w', padx=pdx)

DultimoDat_i2 = Label(f_inferior_right, textvariable=h_fin2, font=(fuente, tamañoLetras), width=14,bg=colorFondo, borderwidth=1, relief="sunken")
DultimoDat_i2.grid(row=4, column=1, sticky='w', padx=pdx)

datTomados_i2 = Label(f_inferior_right, text="Datos tomados", font=(fuente, tamañoLetras), bg=colorFondo)
datTomados_i2.grid(row=5, column=0, sticky='w', padx=pdx)

DdatTomados_i2 = Label(f_inferior_right, textvariable=m_ion2, font=(fuente, tamañoLetras), width=14,bg=colorFondo, borderwidth=1, relief="sunken")
DdatTomados_i2.grid(row=5, column=1, sticky='w', padx=pdx)

# todo: Parte inferior
bl_copy = Button(root, text="Copiar MW ION 1",font=(fuente, tamañoBotones), width=20, command=copiar1, bg=colorBoton)  
bl_copy.grid(column=0, row=4, pady=7)

bl_copy = Button(root, text="Copiar MW ION 2",font=(fuente, tamañoBotones), width=20, command=copiar2, bg=colorBoton)  
bl_copy.grid(column=1, row=4, pady=7)

by_S_Adaros = Label(root, text="By S. Adaros", font=(fuente, 9), bg=colorFondo)
by_S_Adaros.grid(row=5, column=1, sticky='e', padx=10)

# todo: Intervalo
date_intervalo = Button(f_superior, text='Intervalo', command=intervalo ,font=(fuente, 12), bg=colorFondo, width=9, borderwidth=1, relief="raised")
date_intervalo.grid(row=1, column=1, padx=10, pady=10, rowspan=2, sticky='e')

# todo: label de decoración parte inferior sobre los botones copiar
label1 =Label(f_inferior_left, font=(fuente, tamañoLetras), bg=colorFondo, width=30, height=3, borderwidth=1, relief="groove")
label1.grid(row=6, column=0, columnspan=2, rowspan=3, padx=pdx)

label2 =Label(f_inferior_right, font=(fuente, tamañoLetras), bg=colorFondo, width=30, height=3, borderwidth=1, relief="groove")
label2.grid(row=6, column=0, columnspan=2, rowspan=3, padx=pdx)

root.mainloop()