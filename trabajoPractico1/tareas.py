import random
import datetime
import funciones_propias

'''
Descripción: Verifica si un diccionario otorgado es un diccionario de tareas válido o no.
Retorno: True o False.
'''
def validar_diccionario_tareas(diccionario):
    diccionario_valido = True
    if not isinstance(diccionario, dict):
        print("ERROR FATAL: El elemento ingresado como diccionario no es un diccionario.")
        diccionario_valido = False
    elif "tareas" not in diccionario or not isinstance(diccionario["tareas"], dict):
        print("ERROR FATAL: El diccionario ingresado no es un diccionario de tareas.")
        diccionario_valido = False
    return diccionario_valido

'''
Descripción: Verifica si una fecha es válida o no.
Retorno: True o False.
'''
def validar_fecha(fecha: datetime.date):
    fecha_valida = True
    if not isinstance(fecha, datetime.date):
        fecha_valida = False
        print("¡Atención!: El elemento ingresado como fecha no es una fecha.")
    while fecha < datetime.date.today():
        print(f"¡Atención!: La fecha ingresada es inválida. No se puede ingresar una fecha anterior al día de hoy, {datetime.date.today()}")
        fecha_corregida = input("Ingrese la fecha nuevamente. Formato DD/MM/AAAA: ")
        fecha = datetime.datetime.strptime(fecha_corregida, "%d/%m/%Y").date()
    return fecha_valida, fecha

'''
Descripción: Genera una tarea aleatoria a petición.
Retorno: String con la descripción de una tarea aleatoria
'''
acciones = ["escribir","revisar","organizar","preparar","investigar","analizar","completar","documentar","presentar","validar"]
objetos = ["el informe","el proyecto","el plan","la propuesta","el documento","el esquema","la base de datos","el artículo","el gráfico","el diagrama"]
contextos = ["en la oficina","para el cliente","con el equipo","en línea","para el jefe","en la reunión","antes del plazo","en el sistema","durante el viaje","en el servidor"]
 
generar_tarea = lambda: f"{random.choice(acciones)} {random.choice(objetos)} {random.choice(contextos)}"
 
'''
Descripción: Generea una fecha aleatoria entre los 15 días anteriores y los 60 días posteriores a la actualidad.
Retorno: Fecha de tipo datetime.
'''
def generar_fecha():
    #En base a la fecha de ejecución, genero una fecha entre 15 días antes y 60 días después
    hoy = datetime.date.today()
    fecha_minima = hoy - datetime.timedelta(days = 15)
    fecha_maxima = hoy + datetime.timedelta(days = 60)
    fecha = random.uniform(fecha_minima, fecha_maxima)
    return fecha

'''
Descripción: Genera un diccionario con una cantidad solicitada de tareas, sus fechas límite y un estado aleatorio.
Retorno: Diccionario con las tareas, sus fechas límite y el estado en que se encuentra.
'''
def generar_diccionario_tareas(cantidad):
    diccionario_tareas = {"tareas": {}}
    for i in range(1, cantidad + 1):
        estado = random.choice(["pendiente", "en proceso", "finalizada"])
        diccionario_tareas["tareas"][i] = {
            "descripción": generar_tarea(),
            "fecha_límite": generar_fecha(),
            "estado": estado
        }
    return diccionario_tareas

'''
Descripción: Crea una nueva tarea en base a un diccionario, descripción y fecha que se le otorguen, en caso de ser válidos los datos.
Retorno: Nulo.
'''

def crear_tarea(diccionario: dict, tarea: str, fecha:  datetime.date):
    fecha_valida, fecha_corregida = validar_fecha(fecha)
    if validar_diccionario_tareas(diccionario) and fecha_valida:
        estado = "pendiente"
        nuevo_id = max(diccionario["tareas"].keys(), default=0) + 1
        diccionario["tareas"][nuevo_id] = {
            "descripción": tarea,
            "fecha_límite": fecha_corregida,
            "estado": estado
        }

'''
Descripción: Edita la descripción y fecha de una tarea en base al ID dado
Retorno: Nulo
'''
def actualizar_tarea(diccionario: dict, id: str):
    id_valido, posicion = funciones_propias.validar_id(diccionario["tareas"], id)
    if validar_diccionario_tareas(diccionario) and id_valido:
        tarea = input("Ingrese la descripción de la tarea: ")
        fecha = datetime.datetime.strptime(input(" Formato DD/MM/AAAA: "), "%d/%m/%Y").date()
        fecha_valida, fecha_ = validar_fecha(fecha)
        if fecha_valida:
            diccionario["tareas"][id]["descripción"] = tarea
            diccionario["tareas"][id]["fecha_límite"] = fecha_

'''
Descripción: Elimina una tarea en base a el ID otorgado de la misma
Retorno: Nulo
'''
def eliminar_tarea(diccionario: dict, id: str):
    id_valido, posicion = funciones_propias.validar_id(diccionario["tareas"], id)
    if validar_diccionario_tareas(diccionario) and id_valido:
        diccionario["tareas"].pop(posicion)

'''
Descripción: La función bsca tareas en la matriz según el rango de fechas que el usuario indica
Retorno:
'''
def buscar_tareas_por_fecha(diccionario, fecha_inicio, fecha_fin):
    if not validar_diccionario_tareas(diccionario):
        print("El diccionario de tareas no es válido")
        return []
    
    fecha_inicio = datetime.datetime.strptime(fecha_inicio, "%d/%m/%Y").date()
    fecha_fin = datetime.datetime.strptime(fecha_fin, "%d/%m/%Y").date()

    fecha_inicio_valida, fecha_inicio_corregida = validar_fecha(fecha_inicio)
    fecha_fin_valida, fecha_fin_corregida = validar_fecha(fecha_fin)

    if not (fecha_inicio_valida and fecha_fin_valida):
        print("Una o ambas fechas ingresadas son inválidas.")
        return []
    tareas_rango = []
    for id, tarea in diccionario["tareas"].items():
        fecha_tarea = tarea["fecha_límite"]
        if fecha_inicio_corregida <= fecha_tarea <= fecha_fin_corregida:
            tareas_rango.append(tarea)
    tareas_rango = sorted(tareas_rango, key=lambda x: x["fecha_límite"])
    return tareas_rango
