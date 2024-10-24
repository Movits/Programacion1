import random
import datetime
import funciones_propias

def validar_diccionario_tareas(diccionario: dict):
    """Verifica si un diccionario es un elemento de tipo 'dict' y que sea uno que corresponda a tareas.

    Args:
        diccionario (dict): Diccionario objetivo

    Returns:
        True/False: Valor booleano correspondiente a la validez del elemento parámetro.
    """    
    diccionario_valido = True
    if not isinstance(diccionario, dict):
        print("ATENCIÓN: El elemento ingresado como diccionario no es un diccionario.")
        diccionario_valido = False
    elif diccionario[0] != "tareas":
        print("ATENCIÓN: El diccionario ingresado no es un diccionario de tareas.")
        diccionario_valido = False
    return diccionario_valido

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

acciones = ["escribir","revisar","organizar","preparar","investigar","analizar","completar","documentar","presentar","validar"]
objetos = ["el informe","el proyecto","el plan","la propuesta","el documento","el esquema","la base de datos","el artículo","el gráfico","el diagrama"]
contextos = ["en la oficina","para el cliente","con el equipo","en línea","para el jefe","en la reunión","antes del plazo","en el sistema","durante el viaje","en el servidor"]

generar_tarea = lambda: f"{random.choice(acciones)} {random.choice(objetos)} {random.choice(contextos)}"

def generar_fecha():
    #En base a la fecha de ejecución, genero una fecha entre 15 días antes y 60 días después
    hoy = datetime.date.today()
    fecha_minima = hoy - datetime.timedelta(days = 15)
    fecha_maxima = hoy + datetime.timedelta(days = 60)
    fecha = random.uniform(fecha_minima, fecha_maxima)
    return fecha

def generar_diccionario_tareas(cantidad):
    diccionario_tareas = {0: "tareas"}
    for i in range(1, cantidad + 1):
        estado = random.choice([0,1,2,3])
        diccionario_tareas[i] = {
            "descripcion": generar_tarea(),
            "fecha_límite": generar_fecha(),
            "estado": estado
        }
    return diccionario_tareas

def crear_tarea(diccionario: dict, tarea: str, fecha:  datetime.date,):
    fecha_valida, fecha_corregida = validar_fecha(fecha)
    if validar_diccionario_tareas(diccionario) and fecha_valida:
        estado = 1
        diccionario[len(diccionario)]={
            "descripcion": tarea,
            "fecha_límite": fecha_corregida,
            "estado": estado
        }

def actualizar_tarea(diccionario: dict, id: str, tarea: str, fecha: str, estado: int):
    if id not in diccionario:
        print("ATENCIÓN: El ID otorgado no se encuentra en el diccionario.")
    else:
        fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
        fecha_valida, fecha = validar_fecha(fecha)
        if fecha_valida:
            diccionario[id]["descripcion"] = tarea
            diccionario[id]["fecha_límite"] = fecha
            diccionario[id]["estado"] = estado

def eliminar_tarea(diccionario: dict, id: str):
    id_valido, posicion = funciones_propias.validar_id(diccionario, id)
    if validar_diccionario_tareas(diccionario) and id_valido:
        diccionario.pop(posicion)

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
    for id, tarea in diccionario.items():
        if isinstance(tarea, dict):
            fecha_tarea = tarea["fecha_límite"]
            if fecha_inicio_corregida <= fecha_tarea <= fecha_fin_corregida:
                tareas_rango.append(tarea)
    tareas_rango = sorted(tareas_rango, key=lambda x: x["fecha_límite"])
    return tareas_rango
