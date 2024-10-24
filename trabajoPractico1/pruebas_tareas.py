import funciones_propias
import tareas
import datetime

tarea = tareas.generar_tarea()
print("TAREA GENERADA")
print(tarea)
print()

fecha = tareas.generar_fecha()
print("FECHA GENERADA")
print(fecha)
print()

diccionario_tareas = tareas.generar_diccionario_tareas(5)
print("DICCIONARIO DE TAREAS GENERADO")
for key, valor in diccionario_tareas["tareas"].items():
    print(f"ID: {key}, Descripción: {valor['descripción']}, Fecha Límite: {valor['fecha_límite']}, Estado: {valor['estado']}")
print()

tareas.crear_tarea(diccionario_tareas, "Ver la tele en el cuarto de Tiago", datetime.date(2024, 11, 12))
print("TAREA CREADA")

for key, valor in diccionario_tareas["tareas"].items():
    print(f"ID: {key}, Descripción: {valor['descripción']}, Fecha Límite: {valor['fecha_límite']}, Estado: {valor['estado']}")
print()

tareas.actualizar_tarea(diccionario_tareas, 3)
print("ACTUALIZACIÓN DE TAREA")
print()

for key, valor in diccionario_tareas["tareas"].items():
    print(f"ID: {key}, Descripción: {valor['descripción']}, Fecha Límite: {valor['fecha_límite']}, Estado: {valor['estado']}")
print()

tareas.eliminar_tarea(diccionario_tareas, 1)
print("TAREA ELIMINADA")
for key, valor in diccionario_tareas["tareas"].items():
    print(f"ID: {key}, Descripción: {valor['descripción']}, Fecha Límite: {valor['fecha_límite']}, Estado: {valor['estado']}")
print()


fecha_inicio = datetime.datetime.today().strftime("%d/%m/%Y")
fecha_fin = "30/12/2024"
tareas_en_rango = tareas.buscar_tareas_por_fecha(diccionario_tareas, fecha_inicio, fecha_fin)
print(f"TAREAS ENTRE {fecha_inicio} Y {fecha_fin}")
for tarea in tareas_en_rango:
    print(f"Descripción: {tarea['descripción']}, Fecha Límite: {tarea['fecha_límite']}, Estado: {tarea['estado']}")
print()