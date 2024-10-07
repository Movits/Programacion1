import funciones_propias
import personas
import tareas
import asignaciones
import datetime
import random

matriz_personas = personas.generar_diccionario_personas(5)
matriz_tareas = tareas.generar_matriz_tareas(5)
matriz_asignaciones = asignaciones.generar_matriz_asignaciones(matriz_personas, matriz_tareas)

def imprimir_matriz_gestion(matriz_personas: list, matriz_tareas: list, matriz_asignaciones: list):
    tabla=["nombre_completo", "tareas", "descripcion_tarea", "fecha_limite", "pendiente", "en_proceso", "finalizada", "retrasada"]
    print(f"{tabla[0]:^25} | {tabla[1]:^7} | {tabla[2]:^40} | {tabla[3]:^12} | {tabla[4]:^10} | {tabla[5]:^10} | {tabla[6]:^10} | {tabla[7]:^10}".upper().replace("_"," "))
    
    for persona in matriz_personas[1:]:
        nombre_completo = f"{persona[1]} {persona[2]}"
        
        asignaciones_persona = []
        for asignacion in matriz_asignaciones:
            if asignacion[1] == persona[0]:
                asignaciones_persona.append(asignacion)
        
        estados = {"Pendiente": 0, "En proceso": 0, "Finalizada": 0, "Retrasada": 0}
        total_tareas = 0
        
        detalles_tareas = []
        descripciones_tareas = []
        fechas_limite = []
        
        for asignacion in asignaciones_persona:
            ids_tareas = asignacion[2]     
            estados = {"Pendiente": 0, "En proceso": 0, "Finalizada": 0, "Retrasada": 0}
        
            for id_tarea in ids_tareas:
                tarea = []
                for t in matriz_tareas:
                    if t[0] == id_tarea:
                        tarea = t
                        
                descripcion_tarea = tarea[1]
                fecha_limite = tarea[2].strftime("%d/%m/%Y")
                
                estado = random.choice(["Pendiente", "En proceso", "Finalizada", "Retrasada"])
                estados[estado] += 1
                
                descripciones_tareas.append(descripcion_tarea)
                fechas_limite.append(fecha_limite)
                
                detalles_tareas.append((descripcion_tarea, fecha_limite))
                total_tareas += 1
                
            if total_tareas >0:  
                print(f"{nombre_completo.title():^25} | {total_tareas:^7} | {'':^40} | {'':^12} | {estados['Pendiente']:^10} | {estados['En proceso']:^10} | {estados['Finalizada']:^10} | {estados['Retrasada']:^10}")

                for descripcion_tarea, fecha_limite in detalles_tareas :
                    print(f"{'':^25} | {'':^7} | {descripcion_tarea[:36].capitalize() + '...' if len(descripcion_tarea) > 36 else descripcion_tarea.capitalize():^40} | {fecha_limite:^12} | {'':^10} | {'':^10} | {'':^10} | {'':^10}")

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
        print("10.Ver asignaciones")
        print("11.Crear asignacion")
        print("12.Actualizar asignacion")
        print("13.Eliminar asignacion")
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
        elif opcion == '10':
            imprimir_matriz_gestion(matriz_personas, matriz_tareas, matriz_asignaciones)
            volver_o_salir()
        elif opcion == '11':
            crear_asignacion()
            volver_o_salir()
        elif opcion == '12':
            ver_personas()
            actualizar_asignacion()
            volver_o_salir()
        elif opcion == '13':
            eliminar_asignacion()
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

def crear_asignacion():
    id_persona = int(input("Ingresa el ID de la persona: "))
    num_tareas = int(input("Cuantas tareas quieres asignar? "))
    ids_tareas = random.sample([tarea[0] for tarea in matriz_tareas[1:]], num_tareas)
    asignaciones.crear_asignacion(matriz_asignaciones, id_persona, ids_tareas)

def actualizar_asignacion():
    id_asignacion = int(input("Ingresa el ID de la asignacion a actualizar: "))
    num_tareas = int(input("Cuantas tareas quieres asignar? "))
    ids_tareas = random.sample([tarea[0] for tarea in matriz_tareas[1:]], num_tareas)
    asignaciones.actualizar_asignacion(matriz_asignaciones, id_asignacion, ids_tareas)

def eliminar_asignacion():
    id_asignacion = int(input("Ingresa el ID de la asignacion a eliminar: "))
    asignaciones.eliminar_asignacion(matriz_asignaciones, id_asignacion)

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
