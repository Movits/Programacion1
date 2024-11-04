import personas
import tareas
import asignaciones
import datetime

diccionario_personas = personas.generar_diccionario_personas(8)
diccionario_tareas = tareas.generar_diccionario_tareas(4)
matriz_asignaciones = asignaciones.generar_matriz_asignaciones(diccionario_personas, diccionario_tareas)

print("GENERACIÓN DE ASIGNACIONES")
print("Nota: Se genera una tabla de asignaciones en base a dos diccionarios ya creados con 8 personas y 4 tareas a asignar")
for linea in matriz_asignaciones:
    print(linea)
print()

print("CREACIÓN DE UNA ASIGNACIÓN SATISFACTORIA")
print("Nota: Se crea una tarea nueva, cuya ID deberá ser 5, y se le asignan las personas con ID 1 y 6.")
tareas.crear_tarea(diccionario_tareas, "Ver la tele en casa de Tiago", datetime.date.today())
asignaciones.crear_asignacion(matriz_asignaciones, list(diccionario_personas.keys()), list(diccionario_tareas.keys()), 5, [1,6])
for linea in matriz_asignaciones:
    print(linea)
print()

print("CREACIÓN DE UNA ASIGNACIÓN INCORRECTA")
print("Nota: Se intenta crear una asignación a una tarea que ya está asignada.")
asignaciones.crear_asignacion(matriz_asignaciones, list(diccionario_personas.keys()), list(diccionario_tareas.keys()), 3, [3,4])
for linea in matriz_asignaciones:
    print(linea)
print()

print("CREACIÓN DE UNA ASIGNACIÓN CON UNA TAREA INEXISTENTE")
print("Nota: Se intenta crear una asignacion con un ID inexistente en el diccionario de tareas.")
asignaciones.crear_asignacion(matriz_asignaciones, list(diccionario_personas.keys()), list(diccionario_tareas.keys()), 12, [3,4])
for linea in matriz_asignaciones:
    print(linea)
print()

print("CREACIÓN DE UNA ASIGNACIÓN CON UNA PERSONA INEXISTENTE")
print("Nota: Se intenta crear una asignacion con un ID inexistente en el diccionario de personas.")
asignaciones.crear_asignacion(matriz_asignaciones, list(diccionario_personas.keys()), list(diccionario_tareas.keys()), 3, [3,34])
for linea in matriz_asignaciones:
    print(linea)
print()

print("ACTUALIZACIÓN DE UNA ASIGNACIÓN SATISFACTORIA")
print("Nota: Se actualiza la asignacion")
asignaciones.actualizar_asignacion(matriz_asignaciones, list(diccionario_personas.keys()), list(diccionario_tareas.keys()), 2, [3,4])
for linea in matriz_asignaciones:
    print(linea)
print()

print("ACTUALIZACION DE UNA ASIGNACION CON TAREA INCORRECTA")
print("Nota: Se intenta actualizar una tarea que no está presente dentro de la matriz de asignaciones, pero que si existe.")
tareas.crear_tarea(diccionario_tareas, "Jugar a Counter Strike 2", datetime.date.today())
asignaciones.actualizar_asignacion(matriz_asignaciones, diccionario_personas, diccionario_tareas, 6, [2,5])
for linea in matriz_asignaciones:
    print(linea)
print()

print("ACTUALIZACIÓN DE UNA ASIGNACIÓN CON TAREA INEXISTENTE")
print("Nota: Se intenta actualizar una asignación con un ID de tarea inexistente.")
asignaciones.actualizar_asignacion(matriz_asignaciones, diccionario_personas, diccionario_tareas, 8, [2,5])
for linea in matriz_asignaciones:
    print(linea)
print()

print("ACTUALIZACIÓN DE UNA TAREA CON UNA PERSONA INEXISTENTE")
print("Nota: Se intenta actualizar una asignación con un ID de persona que no exsite.")
asignaciones.actualizar_asignacion(matriz_asignaciones, diccionario_personas, diccionario_tareas, 5, [14,27])
for linea in matriz_asignaciones:
    print(linea)
print()

print("ELIMINACION DE UNA ASIGNACION SATISFACTORIA")
print("Nota: Se elimina la asignacion de la tarea con ID 3.")
asignaciones.eliminar_asignacion(matriz_asignaciones, 3)
for linea in matriz_asignaciones:
    print(linea)
print()

print("ELIMINACION DE UNA ASIGNACION INCORRECTA")
print("Nota: Se elimina la asignacion de la tarea con un ID inexistente en la matriz de asignaciones.")
asignaciones.eliminar_asignacion(matriz_asignaciones, 73)
for linea in matriz_asignaciones:
    print(linea)
print()