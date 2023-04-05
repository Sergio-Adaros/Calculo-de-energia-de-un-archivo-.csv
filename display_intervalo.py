from tkinter import *
from popup_interv import sinDatos1, sinDatos2
import pyperclip
from display_detalles import detalle



def display_int(result, dateList):

    # * Definición de funciones

    # Función copiar
    def copiar1():
        if result[2] % 96 != 0:
            pyperclip.copy("")
        else:
            r = str(result[0])
            r = r.replace('.',',')
            pyperclip.copy(r)
        
    def copiar2():
        if result[3] % 96 != 0:
            pyperclip.copy("")
        else:
            r = str(result[1])
            r = r.replace('.',',')
            pyperclip.copy(r)


    # Función seteo de datos con el boton calcular
    def seteo_datos():

        DtotalMWdy_i1 = Label(fdy_inferior_left, text=round(result[0], 5), font=(fuente, tamañoLetras), width=wl_dat,bg=colorFondo, borderwidth=1, relief="sunken")
        DtotalMWdy_i1.grid(row=1, columnspan=2, padx=pdx)

        DtotalMWdy_i2 = Label(fdy_inferior_right, text=round(result[1], 5), font=(fuente, tamañoLetras), width=wl_dat,bg=colorFondo, borderwidth=1, relief="sunken")
        DtotalMWdy_i2.grid(row=1, columnspan=2, padx=pdx)

        DdatTomadosdy_i1 = Label(fdy_inferior_left, text=result[2],  font=(fuente, tamañoLetras), width=wl_dat,bg=colorFondo, borderwidth=1, relief="sunken")
        DdatTomadosdy_i1.grid(row=3, columnspan=2, padx=pdx)

        DdatTomadosdy_i2 = Label(fdy_inferior_right, text=result[3], font=(fuente, tamañoLetras), width=wl_dat,bg=colorFondo, borderwidth=1, relief="sunken")
        DdatTomadosdy_i2.grid(row=3, columnspan=2, padx=pdx)

        DdiasTomadosdy_i1 = Label(fdy_inferior_left, text=result[6][0],  font=(fuente, tamañoLetras), width=wl_dat,bg=colorFondo, borderwidth=1, relief="sunken")
        DdiasTomadosdy_i1.grid(row=5, columnspan=2, padx=pdx)

        DdiasTomadosdy_i2 = Label(fdy_inferior_right, text=result[7][0],  font=(fuente, tamañoLetras), width=wl_dat,bg=colorFondo, borderwidth=1, relief="sunken")
        DdiasTomadosdy_i2.grid(row=5, columnspan=2, padx=pdx)

        # Detalles del cálculo botón
        l_fechasDetalles = [result[6], result[7]]
        detalles = Button(root_dy, text='Detalles', font=(fuente, tamañoBotones), command=lambda:detalle(l_fechasDetalles), bg=colorBoton)
        detalles.grid(row=4, columnspan=2) 

        # Comprobación ion1 si hay días con menos de 96 datos
        if result[2] % 96 != 0:

            pyperclip.copy("")

            DtotalMWdy_i1 = Label(fdy_inferior_left, text='Datos incompletos', font=(fuente, tamañoLetras),fg='red', width=wl_dat,bg=colorFondo, borderwidth=1, relief="sunken")
            DtotalMWdy_i1.grid(row=1, columnspan=2, padx=pdx)

            DdatTomadosdy_i1 = Label(fdy_inferior_left, text=result[2],  font=(fuente, tamañoLetras),fg='red', width=wl_dat,bg=colorFondo, borderwidth=1, relief="sunken")
            DdatTomadosdy_i1.grid(row=3, columnspan=2, padx=pdx)

            label1dy =Label(fdy_inferior_left, text='Existen días con datos incompletos', font=(fuente, tamañoLetras), bg='#fff7be', width=w_m_error, height=3, borderwidth=1, relief="groove")
            label1dy.grid(row=6, column=0, columnspan=2, rowspan=3, padx=pdx)
        # Comprobación ion2 si hay días con menos de 96 datos
        if result[3] % 96 != 0:

            pyperclip.copy("")

            DtotalMWdy_i2 = Label(fdy_inferior_right, text='Datos incompletos', font=(fuente, tamañoLetras),fg='red', width=wl_dat,bg=colorFondo, borderwidth=1, relief="sunken")
            DtotalMWdy_i2.grid(row=1, columnspan=2, padx=pdx) 

            DdatTomadosdy_i2 = Label(fdy_inferior_right, text=result[3], font=(fuente, tamañoLetras),fg='red', width=wl_dat,bg=colorFondo, borderwidth=1, relief="sunken")
            DdatTomadosdy_i2.grid(row=3, columnspan=2, padx=pdx)

            label2dy =Label(fdy_inferior_right, text='Existen días con datos incompletos', font=(fuente, tamañoLetras), bg='#fff7be', width=w_m_error, height=3, borderwidth=1, relief="groove")
            label2dy.grid(row=6, column=0, columnspan=2, rowspan=3, padx=pdx)   

        try:
            if len(result[4]) > 0:   
                sinDatos1(result[4])
                root_dy.destroy() 
                    
            if len(result[5]) > 0:
                sinDatos2(result[5]) 
                root_dy.destroy()
        except:
            pass        

    # Extrayendo fecha inicio y fin
    dateIN = 'Fecha inicio:   ' + str(dateList[0])
    dateFIN = '   Fecha fin:   ' + str(dateList[-1])
    
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
    # Labels datos
    wl_dat = 20
    w_m_error = 30
    w_fecha = 20
    # padx de los label
    pdx = 5

    # todo: Definiendo el root y sus caracterízticas
    root_dy = Tk()                                   
    root_dy.title("INTERVALO".center(180))  
    root_dy.iconbitmap("icono.ico")                      
    root_dy.resizable(0,0)                 
    root_dy.config(bd=10, bg=colorRoot, relief='ridge')
    # Extracción de datos del tamaño de la pantalla
    wdy_total = root_dy.winfo_screenwidth()    
    hdy_total = root_dy.winfo_screenheight()   
    # definición tamaño de la ventana
    wdy_Windows = 650   
    hdy_Windows = 550
    # Calculo para la posición de la ventana root
    pdy_width = round(wdy_total/2-wdy_Windows/2)
    pdy_height = round(hdy_total/2-hdy_Windows/2)
    # Configurando el tamaño y posición del root
    root_dy.geometry(str(wdy_Windows)+"x"+str(hdy_Windows)+"+"+str(pdy_width)+"+"+str(pdy_height))
        
    # todo: Parte superior
    # Definición tamaño del frame superior
    wsdy_matriz = (wdy_Windows/1.0317460317)
    hsdy_matriz = (hdy_Windows/5)
    # Creación de columnas superior que contiene la fecha, el boton calcular y la versión del software
    fdy_superior = Frame(root_dy, width=wsdy_matriz, height=hsdy_matriz)
    fdy_superior.grid(row=0, columnspan=2)
    # Columnas y filas dentro de f_superior
    twdy_frame_superior = wsdy_matriz/2
    thdy_frame_superior = hsdy_matriz/3

    for column in range(2):  
        for fila in range(3):
            sfdy_superior = Frame(fdy_superior, width=twdy_frame_superior, height=thdy_frame_superior)
            sfdy_superior.grid(column=column, row=fila)
            sfdy_superior.configure(bg=colorFondo)
            sfdy_superior.grid_propagate(False)

    # Boton calcular, fecha y versión del software - en la parte superior dentro de f_superior
    dateFdy_superior_ini = Label(fdy_superior, text=dateIN, font=(fuente, tamañoLetras), bg=colorFondo, fg='#082a8c', width=23, height=2, borderwidth=1, relief="flat")
    dateFdy_superior_ini.grid(row=0, column=0, padx=10, pady=10, rowspan=2)

    dateFdy_superior_fin = Label(fdy_superior, text=dateFIN, font=(fuente, tamañoLetras), bg=colorFondo, fg='#082a8c', width=w_fecha, height=2, borderwidth=1, relief="flat")
    dateFdy_superior_fin.grid(row=0, column=1, padx=10, pady=10, rowspan=2)

    bdy_calcular = Button(fdy_superior, text="Calcular", height=1, width=10,font=(fuente, tamañoBotones),command=seteo_datos, bg=colorBoton)  
    bdy_calcular.grid(row=0, columnspan=2,rowspan=3)

    versiondy = Label(fdy_superior, text="  Version 2", font=(fuente, 9), bg=colorFondo)
    versiondy.grid(row=0, columnspan=2, sticky='nw')

    ndy_ion1 = Label(fdy_superior, text="Datos ION 1", font=(fuente, tamañoLetras), bg=colorFondo)
    ndy_ion1.grid(row=2, column=0)

    ndy_ion2 = Label(fdy_superior, text="Datos ION 2", font=(fuente, tamañoLetras), bg=colorFondo)
    ndy_ion2.grid(row=2, column=1)

    # todo: Parte central


    # Creación de datos ion izquierdo y derecho
    widy_matriz = (wdy_Windows/2.0967741935)
    hidy_matriz = (hdy_Windows/1.6176470588)
    # Lado izquierdo frame principal
    fdy_inferior_left = Frame(root_dy, width=widy_matriz, height=hidy_matriz)
    fdy_inferior_left.grid(column=0, row=2, rowspan=2, pady=4)
    fdy_inferior_left.configure(bg=colorFondo, relief='ridge', bd=5)
    fdy_inferior_left.grid_propagate(False)
    # Tamaño de las celdas
    twdy_fInf = (widy_matriz/2)-6
    thdy_fInf = (hidy_matriz/9)-1.5
    # Creación de columnas y filas
    for column in range(2):  
        for fila in range(9):
            sfdy_superior = Frame(fdy_inferior_left, width=twdy_fInf, height=thdy_fInf)
            sfdy_superior.grid(column=column, row=fila)
            sfdy_superior.configure(bg=colorFondo)

    # Labels del lado izquierdo
    totalMWdy_i1 = Label(fdy_inferior_left, text="Total MW", font=(fuente, tamañoLetras), bg=colorFondo)
    totalMWdy_i1.grid(row=0, columnspan=2, padx=pdx)

    DtotalMWdy_i1 = Label(fdy_inferior_left, font=(fuente, tamañoLetras), width=wl_dat,bg=colorFondo, borderwidth=1, relief="sunken")
    DtotalMWdy_i1.grid(row=1, columnspan=2, padx=pdx)

    datTomadosdy_i1 = Label(fdy_inferior_left, text="Total datos tomados", font=(fuente, tamañoLetras), bg=colorFondo)
    datTomadosdy_i1.grid(row=2, columnspan=2, padx=pdx)

    DdatTomadosdy_i1 = Label(fdy_inferior_left,  font=(fuente, tamañoLetras), width=wl_dat,bg=colorFondo, borderwidth=1, relief="sunken")
    DdatTomadosdy_i1.grid(row=3, columnspan=2, padx=pdx)

    diasTomadosdy_i1 = Label(fdy_inferior_left, text="Días tomados", font=(fuente, tamañoLetras), bg=colorFondo)
    diasTomadosdy_i1.grid(row=4, columnspan=2, padx=pdx)

    DdiasTomadosdy_i1 = Label(fdy_inferior_left,  font=(fuente, tamañoLetras), width=wl_dat,bg=colorFondo, borderwidth=1, relief="sunken")
    DdiasTomadosdy_i1.grid(row=5, columnspan=2, padx=pdx)

   
    # Lado derecho
    fdy_inferior_right = Frame(root_dy, width=widy_matriz, height=hidy_matriz)
    fdy_inferior_right.grid(column=1,row=1, rowspan=2, pady=4)
    fdy_inferior_right.configure(bg=colorFondo, relief='ridge', bd=5)
    fdy_inferior_right.grid_propagate(False)
    # Creación de filas y columnas
    for column in range(2):  
        for fila in range(9):
            sfdy_superior = Frame(fdy_inferior_right, width=twdy_fInf, height=thdy_fInf)
            sfdy_superior.grid(column=column, row=fila)
            sfdy_superior.configure(bg=colorFondo)

    # Labels del lado izquierdo
    totalMWdy_i2 = Label(fdy_inferior_right, text="Total MW", font=(fuente, tamañoLetras), bg=colorFondo)
    totalMWdy_i2.grid(row=0, columnspan=2, padx=pdx)

    DtotalMWdy_i2 = Label(fdy_inferior_right, font=(fuente, tamañoLetras), width=wl_dat,bg=colorFondo, borderwidth=1, relief="sunken")
    DtotalMWdy_i2.grid(row=1, columnspan=2, padx=pdx)

    datTomadosdy_i2 = Label(fdy_inferior_right, text="Total datos tomados", font=(fuente, tamañoLetras), bg=colorFondo)
    datTomadosdy_i2.grid(row=2, columnspan=2, padx=pdx)

    DdatTomadosdy_i2 = Label(fdy_inferior_right, font=(fuente, tamañoLetras), width=wl_dat,bg=colorFondo, borderwidth=1, relief="sunken")
    DdatTomadosdy_i2.grid(row=3, columnspan=2, padx=pdx)

    diasTomadosdy_i2 = Label(fdy_inferior_right, text="Días tomados", font=(fuente, tamañoLetras), bg=colorFondo)
    diasTomadosdy_i2.grid(row=4, columnspan=2, padx=pdx)

    DdiasTomadosdy_i2 = Label(fdy_inferior_right,  font=(fuente, tamañoLetras), width=wl_dat,bg=colorFondo, borderwidth=1, relief="sunken")
    DdiasTomadosdy_i2.grid(row=5, columnspan=2, padx=pdx)

    # todo: Parte inferior
    bldy_copy = Button(root_dy, text="Copiar MW ION 1",font=(fuente, tamañoBotones), width=20, command=copiar1, bg=colorBoton)  
    bldy_copy.grid(column=0, row=4, pady=7)

    bldy_copy = Button(root_dy, text="Copiar MW ION 2",font=(fuente, tamañoBotones), width=20, command=copiar2, bg=colorBoton)  
    bldy_copy.grid(column=1, row=4, pady=7)

    bydy_S_Adaros = Label(root_dy, text="By S. Adaros", font=(fuente, 9), bg=colorFondo)
    bydy_S_Adaros.grid(row=5, column=1, sticky='e', padx=10)

    # todo: label de decoración parte inferior sobre los botones copiar
    label1dy =Label(fdy_inferior_left, font=(fuente, tamañoLetras), bg=colorFondo, width=w_m_error, height=3, borderwidth=1, relief="groove")
    label1dy.grid(row=6, column=0, columnspan=2, rowspan=3, padx=pdx)

    label2dy =Label(fdy_inferior_right, font=(fuente, tamañoLetras), bg=colorFondo, width=w_m_error, height=3, borderwidth=1, relief="groove")
    label2dy.grid(row=6, column=0, columnspan=2, rowspan=3, padx=pdx)




    root_dy.mainloop()