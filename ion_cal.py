from io import open  
import csv    
from date import date     
from popup import not_file         

# Calculo ion
def calculo(set_csv, set_date=None):
    #Gestión de errores
    try:
        #Open file
        with open(set_csv, newline='') as set_csv:  
            list_ion = []

            n_ion = csv.reader(set_csv, delimiter=',') 
            # Orden y formato de datos
            for e, filas in enumerate(n_ion):  
                if e != 0:  
                    filas = filas[:2]
                    fila_1 = filas[0]
                    fila_1 = fila_1.replace(' ', ',')
                    fila_2 = filas[1]
                    filas = fila_1 + ',' + fila_2
                    filas = filas.split(',')
                    list_ion.append(filas)
            # Actualización de fecha
            if set_date == None:
                f_set = date()
            else:
                f_set = set_date
            # Extracción de datos útiles
            list_kwh = []
            list_hrs = []

        for e, i in enumerate(list_ion):
            if i[0] == f_set:
                list_kwh.append(float(i[2]))
                list_hrs.append(i[1])
        # Almacenamiento y órden de datos
        t_hrs = 0
        h_ini = 0
        h_end = 0

        t_kwh = sum(list_kwh)/1000  
        if len(list_hrs) >= 1: 
            t_hrs = len(list_hrs)
            h_ini = list_hrs[0]
            h_end = list_hrs[-1]
            h_ini = h_ini.replace(':00000', '')
            h_end = h_end.replace(':00000', '')

        list_end = [t_kwh, f_set, t_hrs, h_ini, h_end]

        return list_end       
    # Gestion de error llamada al popup
    except FileNotFoundError:
        not_file(set_csv)

def calcular(fecha_nueva):  

    ion_1 = 'Revenue Log for PJ-1108A337-02.csv'
    ion_2 = 'Revenue Log for PJ-1503A882-05.csv'

    l_ion_1 = calculo(ion_1, fecha_nueva)                     
    l_ion_2 = calculo(ion_2, fecha_nueva)                     

    lista = [l_ion_1, l_ion_2]                       
 
    return lista                 