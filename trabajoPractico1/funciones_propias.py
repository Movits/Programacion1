import datetime
# Este es un conjunto de funciones que fui creando, que pienso serán útiles para múltiples proyectos.

def imprimir_matriz(matriz):
    #Calculo los anchos que debe tener cada columna, y se le añade un margen de 4 caracteres para mejor resultado visual
    ancho_columnas = [0] * int(len(matriz[0]))
    for i in matriz:
        for j in range(int(len(matriz[0]))):
            ancho_columnas[j] = max(ancho_columnas[j], len(str(i[j])) + 4)
                
    #Imprimo línea por, con el ancho correspondiente a cada columna
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == 0:
                print(f"{matriz[i][j]:^{ancho_columnas[j]}}".upper(), end = "|") #Encabezado, por eso en Uppercase
            #En caso de que el dato sea una fecha, imprime la misma de manera clara y correcta.
            elif isinstance(matriz[i][j], datetime.date):
                fecha = matriz[i][j].strftime("%d/%m/%Y")     
                print(f"{fecha:^{ancho_columnas[j]}}", end = "|")           
            else:
                print(f"{str(matriz[i][j]).capitalize():^{ancho_columnas[j]}}", end = "|")
        print()
        
'''
Descripción: Verifica si un ID está presente en una lista o no.
Retorno: Booleano que determina si se lo encontró o no, y la posición de donde se encuentra (si no se encuentra, la posición es -1).
'''
def validar_id(diccionario, id):
    if id in diccionario:
        return True, id
    else:
        return False, -1