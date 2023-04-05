from tkinter import *
from tkcalendar import *
import datetime
from dateutil.rrule import rrule, DAILY
from calculo_intervalo import *
from display_intervalo import display_int
from popup_interv import sinArchivo

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

def intervalo():

    # * Función intervalo pedido por usuario
    def intervalo_pedido():
        try:
            dateList = []
            # Extrayendo datos de la fecha inicio y fin
            date_star = datei_entry_ini.get()
            date_end = datei_entry_fin.get()
            # Formateando las fechas de d/m/a - d-m-a
            date_star = date_star.replace('/','-')
            date_end = date_end.replace('/','-')
    
            start_date_obj = datetime.datetime.strptime(date_star, ("%d-%m-%Y"))
            end_date_obj = datetime.datetime.strptime(date_end, ("%d-%m-%Y"))
            date_list = list(rrule(DAILY, dtstart=start_date_obj, until=end_date_obj))
            # Iterando el rango de fechas, forateando el objeto y agregandolo como str a una lista
            for date in date_list:
                data = str(date.strftime("%d-%m-%Y"))
                dateList.append(data)
            # Llamada a la función de cálculo
            resultados_i = calcular_i(dateList)
            rooti.destroy()
            # Llamada al display para mostrar los resultados del intervalo
            display_int(resultados_i, dateList)  
        except:
            rooti.destroy()

        
    # Root principal para la ventana donde elegimos el rango de fechas
    rooti = Tk()                                   
    rooti.title("Intervalo".center(90))  
    rooti.iconbitmap("icono.ico")                      
    rooti.resizable(0,0)                 
    rooti.config(bd=10, bg=colorRoot, relief='ridge')
    # Extracción de datos del tamaño de la pantalla
    wi_total = rooti.winfo_screenwidth()    
    hi_total = rooti.winfo_screenheight()   
    # definición tamaño de la ventana
    wi_Windows = 400   
    hi_Windows = 200
    # Calculo para la posición de la ventana root
    pi_width = round(wi_total/2-wi_Windows/2)
    pi_height = round(hi_total/2-hi_Windows/2)
    # Configurando el tamaño y posición del root
    rooti.geometry(str(wi_Windows)+"x"+str(hi_Windows)+"+"+str(pi_width)+"+"+str(pi_height))

    # Definición de tamaño de celdas
    twi = (wi_Windows/2)-50
    thi = (hi_Windows/3)-7
    # Creación de columnas y filas
    for column in range(2):
        for fila in range(3):
            sfi = Frame(rooti, width=twi, height=thi)
            sfi.grid(column=column, row=fila)
            sfi.configure(bg=colorFondo)
    # Creación de labels
    datei = Label(rooti, text='Fecha inicio (dd/mm/aaaa)',font=(fuente, 13), bg=colorFondo)
    datei.grid(row=0, column=0, sticky='w', padx=10)

    datei_entry_ini = DateEntry(rooti, font=(fuente, tamañoLetras), width=11, justify='center', locale='es', date_pattern='dd/mm/y')
    datei_entry_ini.grid(row= 0, column=1, sticky='w')

    datei = Label(rooti, text='Fecha fin     (dd/mm/aaaa)',font=(fuente, 13), bg=colorFondo)
    datei.grid(row=1, column=0, sticky='w', padx=10)

    datei_entry_fin = DateEntry(rooti, font=(fuente, tamañoLetras), width=11, justify='center', locale='es', date_pattern='dd/mm/y')
    datei_entry_fin.grid(row= 1, column=1, sticky='w')
    
    # Boton ok y llamada a la función intervalo_pedido
    datei_ok = Button(rooti, text='OK', font=(fuente, 11), width=10, command=intervalo_pedido)
    datei_ok.grid(row=2, columnspan=2)


     
    rooti.mainloop()