import random

def generar_matriz_asignaciones(diccionario_personas: dict, diccionario_tareas: dict):
    """Genera una matriz de asignaciones de tareas a personas utilizando los diccionarios correspondientes.

    Args:
        diccionario_personas (dict): Diccionario de personas.
        diccionario_tareas (dict): Diccionario de tareas.

    Returns:
        asignaciones (list): Matriz con las asignaciones correspondientes.
    """    
    # En base a los IDs existentes de personas y tareas, se va generando una lista de personas que se asignaran a cada tarea hasta que todas las tareas esten asignadas a 1 o mas personas.
    personas_asignables = list(diccionario_personas.keys())[1:]
    asignaciones = ["asignaciones"]
    id_asignacion = 0
    
    for tarea_asignable in list(diccionario_tareas.keys())[1:]:
        id_asignacion += 1
        # El método sample de la librería random permite seleccionar una cantidad dada de elementos sin repetirlos. Aquí se usa para seleccionar ID's al azar pertenecientes a las personas para asignarlos a tareas.
        personas_seleccionadas = random.sample(personas_asignables, random.randint(1, len(personas_asignables)))
        asignaciones.append([id_asignacion ,tarea_asignable, personas_seleccionadas])
    
    return asignaciones

def crear_asignacion(matriz_asignaciones: list, personas_asignables: list, tareas_asignables: list, id_tarea: int, personas_seleccionadas: list):
    """Asigna una tarea a una lista de personas sólo si ámbos existen en el sistema.

    Args:
        matriz_asignaciones (list): Matriz de asignaciones a la cual se le quiere crear una nueva asignación.
        personas_asignables (list): Lista de todos los IDs de las personas asignables.
        tareas_asignables (list): Lista de todos los IDs de las tareas seleccionables para asignar.
        id_tarea (int): ID de la tarea a la cual se le quiere asignar las personas.
        personas_seleccionadas (list): Lista de las personas que serán asignadas a la tarea.
    """    
    # Se verifica que tanto el ID de la tarea como los IDs de las personas existan dentro de los diccionarios correspondientes.
    if id_tarea in tareas_asignables and all(id_persona in personas_asignables for id_persona in personas_seleccionadas):
        # Generando una lista con todos los IDs de tareas presentes en la matriz, verifica que el ID de tarea otorgado no este dentro de la nueva lista.
        if id_tarea not in [fila[1] for fila in matriz_asignaciones[1:]]:
            print("Info: Tarea asignada")
            matriz_asignaciones.append([len(matriz_asignaciones),id_tarea, personas_seleccionadas])
        else:
            print("¡ATENCIÓN!: la tarea que intentas asignar ya está asignada a otro grupo de personas. Para editarla, debes usar la funcion 'actualizar_asignacion()'")
    else:
        if not(id_tarea in tareas_asignables):
            print("¡ATENCIÓN!: El ID otorgado no está registrado en el sistema.")
        elif not(all(id_persona in personas_asignables for id_persona in personas_seleccionadas)):
            print("¡ATENCIÓN!: Uno o más IDs de las personas no existen en el sistema.")
        print("Info: No se ha concretado la creción de la asignación.")

def actualizar_asignacion(matriz_asignaciones: list, personas_asignables: list, tareas_asignables: list, id_tarea: int, personas_seleccionadas: list):
        """Actualiza una tarea a una lista de personas sólo si los tres existen en el sistema.
    Args:
        matriz_asignaciones (list): Matriz de asignaciones que se quiere actualizar.
        personas_asignables (list): Lista de todos los IDs de las personas asignables.
        tareas_asignables (list): Lista de todos los IDs de las tareas seleccionables para asignar.
        id_tarea (int): ID de la tarea a la cual se le quiere asignar las personas
        personas_seleccionadas (list): Lista de las personas que serán asignadas a la tarea
    """
        # Si la tarea y las personas estan presentes en sus respectivos diccionarios, se verifica que la tarea este tambien presente en la matriz de asignaciones, y se la actualiza con los datos otorgados. De caso contrario se notifica al usuario de cual es el impedimento y no se modifica ningun dato.
        if id_tarea in tareas_asignables and all(id_persona in personas_asignables for id_persona in personas_seleccionadas):
            if id_tarea in [fila[1] for fila in matriz_asignaciones[1:]]:
                for i in range(1, len(matriz_asignaciones)):
                    if matriz_asignaciones[i][1] == id_tarea:
                        matriz_asignaciones[i] = [i, id_tarea, personas_seleccionadas]
                        break
            else:
                print("¡ATENCIÓN!: El ID de tarea otorgado no esta presente en el diccionario de asignaciones. Para crear una asignacion debes usar la funcion 'crear_asignacion()'.")
        else:
            if id_tarea not in tareas_asignables:
                print("¡ATENCIÓN!: El ID de tarea otorgado no existe en el el diccionario de tareas.")
            elif not all(id_persona in personas_asignables for id_persona in personas_seleccionadas):
                print("¡ATENCIÓN!: El ID de persona otorgado no existe en el diccionario de personas.")

def eliminar_asignacion(matriz_asignaciones: list, id_tarea: int):
    # En caso de que el ID de la tarea esté presente dentro de la matriz de asignaciones, la elimina, de ser confirmado por el usuario. De lo contrario, notifica al usuario de la inconveniencia.
    id_taraes_existente = False
    for i in range(1, len(matriz_asignaciones)):
        if matriz_asignaciones[i][1] == id_tarea:
            id_taraes_existente = True
            confirmacion = input(f"Para confirmar la eliminación del la tarea cuyo ID es {id_tarea}, escriba 'Eliminar': ")
            if confirmacion == "Eliminar":
                del matriz_asignaciones[i]
                print(f"Info: Se ha eliminado la asignación de la tarea {id_tarea}.")
                break
            else:
                print("Info: No se ha eliminado ningún dato.")
    if not id_taraes_existente:
        print("¡ATENCIÓN!: El ID de tarea otorgado no existe en la matriz asignaciones.")