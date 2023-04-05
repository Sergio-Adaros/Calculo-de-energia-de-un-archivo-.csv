from tkinter import *

def detalle(fechas):   

    # todo: Formato
    # Colores
    colorFondo = '#D3DCF0'
    colorLabel = '#D3E0ED'
    colorBoton = '#D3E0ED'
    colorRoot = '#D3DCF0'
    colorFondo2 = '#f9f9f9'
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
    pdy = 10

    # todo: Definiendo el root y sus caracterízticas
    root_ds = Tk()                                   
    root_ds.title("Detalles".center(180))  
    root_ds.iconbitmap("icono.ico")                      
    root_ds.resizable(0,0)                 
    root_ds.config(bd=10, bg=colorRoot, relief='ridge')
    # Extracción de datos del tamaño de la pantalla
    wds_total = root_ds.winfo_screenwidth()    
    hds_total = root_ds.winfo_screenheight()   
    # definición tamaño de la ventana
    wds_Windows = 650   
    hds_Windows = 550
    # Calculo para la posición de la ventana root
    pds_width = round(wds_total/2-wds_Windows/2)
    pds_height = round(hds_total/2-hds_Windows/2)
    # Configurando el tamaño y posición del root
    root_ds.geometry(str(wds_Windows)+"x"+str(hds_Windows)+"+"+str(pds_width)+"+"+str(pds_height))


    # todo: Mostrando información por pantalla

    # Días tomados
    diasTomados = Label(root_ds, text='Días tomados  =>', font=(fuente, tamañoLetras), width=wl_dat,bg=colorFondo)
    diasTomados.grid(row=3, column=0, padx=pdx, pady=pdy)

    DdiasTomados = Label(root_ds, text=fechas[0][0],  font=(fuente, tamañoLetras), width=wl_dat,bg=colorFondo2, borderwidth=1, relief="sunken")
    DdiasTomados.grid(row=3, column=1, padx=pdx, pady=pdy)

    # Días con 96 datos (días completos)
    diasCompletos = Label(root_ds, text='Fechas días completos =>', font=(fuente, tamañoLetras), width=wl_dat,bg=colorFondo)
    diasCompletos.grid(row=4, column=0, padx=pdx, pady=pdy)

    Lcompletos = fechas[0][1]

    LdiasCompletos = Listbox(root_ds,width=15, height=5, font=(fuente, tamañoLetras))
    LdiasCompletos.grid(row=4, column=1, pady=pdy)
    
    for i in Lcompletos:
        LdiasCompletos.insert(END, i)

    print(fechas)

    root_ds.mainloop()

