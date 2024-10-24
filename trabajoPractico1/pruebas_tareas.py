import funciones_propias
import tareas
import datetime

tarea = tareas.generar_tarea()
print("GENERACIÓN DE UNA TAREA")
print(tarea)
print()

fecha = tareas.generar_fecha()
print("GENERACIÓN DE UNA FECHA")
print(fecha)
print()

diccionario_tareas = tareas.generar_diccionario_tareas(5)
print("DICCIONARIO DE TAREAS GENERADO")
print("NOTA: Se genera una matriz de tareas de longitud 5.")
for key, valor in diccionario_tareas.items():
    if isinstance(valor, dict):
        print(f"ID: {key}, Descripción: {valor['descripcion']}, Fecha límite: {valor['fecha_límite']}, Estado: {valor['estado']}")
    else:
        print(f"ID: {key}, Tipo: {valor}")
print()

print("CREACIÓN DE UNA TAREA")
print("NOTA: Se genear una tarea cuya descripción es 'Ver la tele en el cuarto de Tiago' y su fecha límite es el 1/12/2024. Por defecto, al crearse una tarea, siempre se le asignará el estado pendiente (1).")
tareas.crear_tarea(diccionario_tareas, "Ver la tele en el cuarto de Tiago", datetime.date(2024, 11, 12))
for key, valor in diccionario_tareas.items():
    if isinstance(valor, dict):
        print(f"ID: {key}, Descripción: {valor['descripcion']}, Fecha límite: {valor['fecha_límite']}, Estado: {valor['estado']}")
    else:
        print(f"ID: {key}, Tipo: {valor}")
print()

print("ACTUALIZACIÓN DE UNA TAREA")
print("NOTA: Se actualiza la tarea con ID 3 con una descripcion 'Ordenar la matriz de estudiantes', fecha límite '19/11/2024', y estado finalizada (3)")
tareas.actualizar_tarea(diccionario_tareas, 3, "Ordenar la matriz de estudiantes", "19/11/2024", 3)
for key, valor in diccionario_tareas.items():
    if isinstance(valor, dict):
        print(f"ID: {key}, Descripción: {valor['descripcion']}, Fecha límite: {valor['fecha_límite']}, Estado: {valor['estado']}")
    else:
        print(f"ID: {key}, Tipo: {valor}")
print()

print("ELIMINACIÓN DE UNA TAREA")
print("NOTA: Se elimina la tarea con el ID 3")
tareas.eliminar_tarea(diccionario_tareas, 3)
for key, valor in diccionario_tareas.items():
    if isinstance(valor, dict):
        print(f"ID: {key}, Descripción: {valor['descripcion']}, Fecha límite: {valor['fecha_límite']}, Estado: {valor['estado']}")
    else:
        print(f"ID: {key}, Tipo: {valor}")
print()


fecha_inicio = datetime.datetime.today().strftime("%d/%m/%Y")
fecha_fin = "30/12/2024"
tareas_en_rango = tareas.buscar_tareas_por_fecha(diccionario_tareas, fecha_inicio, fecha_fin)
print(f"TAREAS ENTRE {fecha_inicio} Y {fecha_fin}")
for key, valor in diccionario_tareas.items():
    if isinstance(valor, dict):
        print(f"ID: {key}, Descripción: {valor['descripcion']}, Fecha límite: {valor['fecha_límite']}, Estado: {valor['estado']}")
    else:
        print(f"ID: {key}, Tipo: {valor}")
print()