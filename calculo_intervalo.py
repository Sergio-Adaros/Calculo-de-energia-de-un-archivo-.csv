from io import open  
import csv       
from popup_interv import sinArchivo   

# Calculo ion
def calculo_i(set_csv, dateList):
    
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
    
        list_end = []
        cont = 0
        l_fechas_csv = []
        l_diasCompletos = []
        l_diasIncompletos = []
        # Iterando sobre el rango de fechas definidas por el usuario
        for fechas in dateList:
            # Extracción de datos útiles
            list_kwh = []
            
            # Iterando sobre los datos del documento ion fecha y MW de la lista original y guardandolo en listas separadas siempre que existan datos en la fecha
            c_mw = 0
            for i in list_ion:
                if i[0] == fechas:
                    list_kwh.append(float(i[2]))
                    cont += 1  # Contador de datos por día  
                    if i[0] not in l_fechas_csv:
                        l_fechas_csv.append(i[0])     # Guardando todas las fechas en las que existen datos
                    c_mw += 1
                    if c_mw == 96:
                        l_diasCompletos.append(i[0])  # Guardando todas las fechas en la que existen datos completos

            # Almacenamiento y órden de datos
            t_kwh = sum(list_kwh)/1000
            list_end.append(t_kwh)

        # * Extrayendo la cantidad de días con datos y las fechas que se tomaron los datos completos como también las fechas en donde se tomaron los datos incompletos
        for i in l_fechas_csv:
            if i not in l_diasCompletos:
                l_diasIncompletos.append(i)

        C_diasTomados = len(l_fechas_csv) # Total de días con datos (cantidad)
        fechasConDAtos = l_fechas_csv     
        dias96datos = l_diasCompletos     
        diasMenos96datos = l_diasIncompletos    

        lista_fechas_datos = [C_diasTomados, fechasConDAtos, dias96datos, diasMenos96datos]

        # * Extrayendo las fechas en las que no se encuentra ningún dato
        # Extrayendo las fechas que se encuentran en las 2 listas
        l_fechas_sinDatos = list(set(dateList).symmetric_difference(l_fechas_csv))

        # Ordenando fechas de dd-mm-aaaa => aaaa-mm-dd para poder ordenar de menor a mayor con el método sort() 
        ordenFechas = []
        ordenFechas2 = []

        for f in l_fechas_sinDatos:
            orden = f.split('-')
            orden.reverse()
            c = 0
            for i in orden:
                if len(ordenFechas) == 1 or len(ordenFechas) == 3:
                    ordenFechas.append('-')
                ordenFechas.append(orden[c])
                c += 1
            orden2 = ''.join(ordenFechas)
            ordenFechas = []
            ordenFechas2.append(orden2)
           
        ordenFechas2.sort() # Ordenando la lista de menor a mayor

        # Ordenando fechas de aaaa-mm-dd => dd-mm-aaaa
        ordenFecha2 = []

        for f in ordenFechas2:
            orden = f.split('-')
            orden.reverse()                         
            orden2 = '-'.join(orden)
            ordenFecha2.append(orden2)    
        
        # * Fin extrayendo las fechas en las que no se encuentra ningún dato

        resultado_final = sum(list_end)

        return resultado_final, cont, ordenFecha2, lista_fechas_datos


    # Gestion de error llamada al popup
    except FileNotFoundError:
        sinArchivo()
        

def calcular_i(dateList):  

    ion_1 = 'Revenue Log for PJ-1108A337-02.csv'   
    ion_2 = 'Revenue Log for PJ-1503A882-05.csv'  

    l_ion_1, cont1, f_sinDatos1, lista_fechas_datos1  = calculo_i(ion_1, dateList)                     
    l_ion_2, cont2, f_sinDatos2, lista_fechas_datos2 = calculo_i(ion_2, dateList)                     

    lista = [l_ion_1, l_ion_2, cont1, cont2, f_sinDatos1, f_sinDatos2, lista_fechas_datos1, lista_fechas_datos2]  
                    
    return lista       
