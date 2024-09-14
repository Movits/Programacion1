import funciones_propias
import personas
import tareas
import asignaciones
import datetime

matriz_personas = personas.generar_matriz_personas(5)
matriz_tareas = tareas.generar_matriz_tareas(5)

#Matriz de asignaciones
def imprimir_matriz_gestion(matriz_personas: list, matriz_tareas: list, matriz_asignaciones: list):
    tabla=["nombre_completo", "tareas", "descripcion_tarea", "fecha_limite", "pendiente", "en_proceso", "finalizada", "retrasada"]
    print(f"{tabla[0]:^25} | {tabla[1]:^7} | {tabla[2]:^40} | {tabla[3]:^12} | {tabla[4]:^10} | {tabla[5]:^10} | {tabla[6]:^10} | {tabla[7]:^10}".upper().replace("_"," "))
    
    for i in range(1, len(matriz_asignaciones)):
        nombre_completo = f"{matriz_personas[i][1]} {matriz_personas[i][2]}"
        cantidad_tareas = f"{len(matriz_asignaciones[i][2])}"
        print(f"{nombre_completo} {cantidad_tareas}")

def menu():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Ver personas")
        print("2. Crear persona")
        print("3. Actualizar persona")
        print("4. Eliminar persona")
        print("5. Ver tareas")
        print("6. Crear tarea")
        print("7. Buscar tarea por fecha")
        print("8. Actualizar tarea")
        print("9. Eliminar tarea")
        print("0. Salir")

        opcion = input("Elige una opcion: ")

        if opcion == '1':
            ver_personas()
            volver_o_salir()
        elif opcion == '2':
            crear_persona()
            volver_o_salir()
        elif opcion == '3':
            actualizar_persona()
            volver_o_salir()
        elif opcion == '4':
            eliminar_persona()
            volver_o_salir()
        elif opcion == '5':
            ver_tareas()
            volver_o_salir()
        elif opcion == '6':
            crear_tarea()
            volver_o_salir()
        elif opcion == '7':
            buscar_tareas()
            volver_o_salir()
        elif opcion == '8':
            actualizar_tarea()
            volver_o_salir()
        elif opcion == '9':
            eliminar_tarea()
            volver_o_salir()
        elif opcion == '0':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor elige nuevamente.")

# Funciones auxiliares para manejar personas
def ver_personas():
    print("Matriz de las personas:")
    funciones_propias.imprimir_matriz(matriz_personas)

def crear_persona():
    nombre = input("Ingresa el nombre de la persona: ")
    apellido = input("Ingresa el apellido de la persona: ")
    personas.crear_persona(matriz_personas, nombre, apellido)

def actualizar_persona():
    ver_personas()
    id_persona = int(input("Ingresa el ID de la persona a actualizar: "))
    nombre = input("Nuevo nombre: ")
    apellido = input("Nuevo apellido: ")
    personas.actualizar_persona(matriz_personas, id_persona, nombre, apellido)

def eliminar_persona():
    ver_personas()
    id_persona = int(input("Ingresa el ID de la persona a eliminar: "))
    personas.eliminar_persona(matriz_personas, id_persona)

# Funciones auxiliares para manejar tareas
def ver_tareas():
    print("Matriz de las tareas:")
    funciones_propias.imprimir_matriz(matriz_tareas)

def crear_tarea():
    descripcion = input("Descripción de la tarea: ")
    fecha = input("Ingresa la fecha límite (DD/MM/AAAA): ")
    fecha_límite = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
    tareas.crear_tarea(matriz_tareas, descripcion, fecha_límite)

def actualizar_tarea():
    ver_tareas()
    id_tarea = int(input("Ingresa el ID de la tarea a actualizar: "))
    tareas.actualizar_tarea(matriz_tareas, id_tarea)

def eliminar_tarea():
    ver_tareas()
    id_tarea = int(input("Ingresa el ID de la tarea a eliminar: "))
    tareas.eliminar_tarea(matriz_tareas, id_tarea)

def buscar_tareas():
    fecha_inicio = input("Ingresa la fecha de inicio (DD/MM/AAAA): ")
    fecha_fin = input("Ingresa la fecha de fin (DD/MM/AAAA): ")
    tareas_en_rango = tareas.buscar_tareas_por_fecha(matriz_tareas, fecha_inicio, fecha_fin)

    if tareas_en_rango:
        print("Tareas encontradas en el rango de fechas:")
        for tarea in tareas_en_rango:
            print(tarea)
    else:
        print("No se encontraron tareas en el rango de fechas especificado.")


def volver_o_salir():
    while True:
        print("\n--- Opciones ---")
        print("1. Volver al menú principal")
        print("2. Salir del programa")
        
        opcion = input("Elige una opción: ")

        if opcion == '1':
            return
        elif opcion == '2':
            print("Saliendo del programa...")
            exit()
        else:
            print("Opción no válida, por favor elige nuevamente.")


menu()
