import personas
import tareas
import asignaciones
import datetime

cantidad_personas_esperadas = 8
cantidad_tareas_esperadas = 4

diccionario_personas = personas.generar_diccionario_personas(cantidad_personas_esperadas)
diccionario_tareas = tareas.generar_diccionario_tareas(cantidad_tareas_esperadas)
matriz_asignaciones = asignaciones.generar_matriz_asignaciones(diccionario_personas, diccionario_tareas)

def test_generacion():
    """Se evalúa que se genere una matriz de asignaciones y que la misma posea la cantidad de tareas otorgada.
    """    
    assert matriz_asignaciones[0] == "asignaciones", "La matriz generada no posee el encabezado 'asignaciones'"
    assert len(matriz_asignaciones) == cantidad_tareas_esperadas + 1, f"No se generó la cantidad de {cantidad_tareas_esperadas} personas esperadas"

def test_creacion():
    """Se evalúan un caso de creación de asignación satisfactorio, uno en donde una tarea no exsite, y otro donde una persona no existe.
    """    
    # Se evalúa una creación satisfactoria.
    tareas.crear_tarea(diccionario_tareas, "Ver la tele en casa de Tiago", datetime.date.today())
    asignaciones.crear_asignacion(matriz_asignaciones, list(diccionario_personas.keys()), list(diccionario_tareas.keys()), 5, [1,6])
    assert matriz_asignaciones[5] == [5, 5, [1, 6]], "No se han asignado las personas 1 y 6 a la tarea 5."
    
    # Se evalúa intentar asignar una tarea ya asignada.
    mensaje_de_situacion = asignaciones.crear_asignacion(matriz_asignaciones, list(diccionario_personas.keys()), list(diccionario_tareas.keys()), 5, [1,6])
    assert mensaje_de_situacion == "¡ATENCIÓN!: la tarea que intentas asignar ya está asignada a otro grupo de personas. Para editarla, debes usar la funcion 'actualizar_asignacion()'", "No se ha advertido de que la tarea que se busca asignar ya esté asignada a otro grupo de personas."
    
    # Se evalúa asignar una tarea que no existe
    mensaje_de_situacion = asignaciones.crear_asignacion(matriz_asignaciones, list(diccionario_personas.keys()), list(diccionario_tareas.keys()), 12, [3,4])
    assert mensaje_de_situacion == "¡ATENCIÓN!: El ID otorgado no está registrado en el sistema.", "No se ha advertido que se intentó asignar una tarea que no existe."

    # Se evalúa asginar una tarea a una persona inexistente
    mensaje_de_situacion = asignaciones.crear_asignacion(matriz_asignaciones, list(diccionario_personas.keys()), list(diccionario_tareas.keys()), 3, [3,34])
    assert mensaje_de_situacion == "¡ATENCIÓN!: Uno o más IDs de las personas no existen en el sistema.", "No se ha advertido de que se intentó asignar una tarea a una o más personas inexistentes."

def test_actualizacion():
    """Se evalúa la actualización de una asignación satisfactoria, el intento de actualizar una tarea inexistente, el intento de actualizar una tarea no asignada, y el intento de actualizar una asignación a una persona inexistente.
    """    
    # Se evalúa la actualización de una tarea satisfactoria
    mensaje_de_situacion = asignaciones.actualizar_asignacion(matriz_asignaciones, list(diccionario_personas.keys()), list(diccionario_tareas.keys()), 2, [3,4])
    assert matriz_asignaciones[2] == [2, 2,[3,4]], "No se ha actualizado la asignacion 2 a las personas 3 y 4"
    assert mensaje_de_situacion == "Info: Se ha actualizado la asignación correctamente.", "No se ha informado de la actualización de una asignación."
    
    # Se evalua intentar actualizar una asignacion a una tarea existente pero todavia no asignada
    tareas.crear_tarea(diccionario_tareas, "Jugar a Counter Strike 2", datetime.date.today())
    mensaje_de_situacion = asignaciones.actualizar_asignacion(matriz_asignaciones, diccionario_personas, diccionario_tareas, 6, [2,5])
    assert mensaje_de_situacion == "¡ATENCIÓN!: El ID de tarea otorgado no esta presente en el diccionario de asignaciones. Para crear una asignacion debes usar la opcion 'Crear asignacion'.", "No se ha informado que se intento actualizar la asignacion de una tarea que no está asignada todavía."
    
    # Se evalúa intentar actualizar una asginación con una tarea inexistente
    mensaje_de_situacion = asignaciones.actualizar_asignacion(matriz_asignaciones, diccionario_personas, diccionario_tareas, 8, [2,5])
    assert mensaje_de_situacion == "¡ATENCIÓN!: El ID de tarea otorgado no existe en el el diccionario de tareas.", "No se ha informado que se ha intentado asignar una tarea inexistente."
    
    # Se evalúa la actualización de una asignación a una persona inexistente.
    mensaje_de_situacion = asignaciones.actualizar_asignacion(matriz_asignaciones, diccionario_personas, diccionario_tareas, 5, [14,27])
    assert mensaje_de_situacion == "¡ATENCIÓN!: El ID de persona otorgado no existe en el diccionario de personas.", "No se ha informado que se ha intentado actualizar una asignación a una persona inexistente."

def test_eliminacion():
    """Se evalúa la eliminación de una asignación satisfactoria y el intento de eliminar una asignación inexistente.
    """    
    # Se evalúa la eliminación satisfactoria de una asignación
    id_tarea = 3
    mensaje_de_situacion = asignaciones.eliminar_asignacion(matriz_asignaciones, id_tarea, "Eliminar")
    assert len(matriz_asignaciones) == 5, "No se ha eliminado correctamente una asignación"
    assert mensaje_de_situacion == f"Info: Se ha eliminado la asignación de la tarea {id_tarea}.", "No se ha informado de la eliminación de una tarea."
    
    # Se evalúa intentar eliminar una asignación inexistente
    mensaje_de_situacion = asignaciones.eliminar_asignacion(matriz_asignaciones, 73)
    assert mensaje_de_situacion == "¡ATENCIÓN!: El ID de tarea otorgado no existe en la matriz asignaciones.", "No se ha informado que se ha intentado eliminar una asignación inexistente."