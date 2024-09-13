import funciones_propias
import personas
import tareas
import asignaciones
import datetime

matriz_personas = personas.generar_matriz_personas(5)
matriz_tareas = tareas.generar_matriz_tareas(5)

def menu():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Ver personas")
        print("2. Crear persona")
        print("3. Actualizar persona")
        print("4. Eliminar persona")
        print("5. Ver tareas")
        print("6. Crear tarea")
        print("7. Actualizar tarea")
        print("8. Eliminar tarea")
        print("9. Salir")

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
            actualizar_tarea()
            volver_o_salir()
        elif opcion == '8':
            eliminar_tarea()
            volver_o_salir()
        elif opcion == '9':
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