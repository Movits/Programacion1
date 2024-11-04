import personas
import tareas
import asignaciones
import datetime
import json
import os

def leer_archivo_personas():
    """
    Lee el archivo personas.json y devuelve un diccionario con los datos registrados. En caso de no ser encontrado, se lo genera con datos aleatorios.

    Returns:
        Dict: Diccionario de personas
    """    
    # Se intenta la lectura del archivo personas.json. 
    # De no existir el archivo, se generan los datos automáticamente. 
    # Se aplica manejo de excepciones en todos los casos posibles de fallo de lectura/escritura del archivo json.
    try:
        with open("personas.json", "r", encoding="UTF-8") as arch_personas:
            # Se leen los datos de personas.json y se los guarda en un diccionario
            diccionario_personas = json.load(arch_personas)
            print("Info: Se ha leído correctamente los datos del archivo personas.json")
    except FileNotFoundError:
        # Se generan los datos de forma alteatoria para el archivo personas.json y se los escribe en el mismo. 
        print("Info: No se ha encontrado el archivo personas.json")
        diccionario_personas = personas.generar_diccionario_personas(8)
        try:
            with open("personas.json", "w", encoding="UTF-8") as arch_personas:
                #NOTA SOBRE ARGUMENTOS:
                # El argumento indent sirve para establecer los espacios de tabulación en el archivo json
                # El argumento ensure_ascii permite que existan dentro de este archivo carácteres pertenecientes a la lengua española, en este caso, por ejemplo, letras con tildación como la "á". 
                json.dump(diccionario_personas, arch_personas, indent=4, ensure_ascii=False)
                print("Info: Se ha generado el archivo personas.json con datos aleatorios.")
        except OSError as error:
            print(f"ERROR: No se ha podido generar el archivo personas.json por un error del sistema operativo: {error}")
        except PermissionError as error:
            print(f"ERROR: No se ha podido generar el archivo personas.json por falta de permisos del programa: {error}")
        except:
            print("ERROR: No se ha podido generar el archivo personas.json")
    except OSError as error:
        print(f"No se ha podido abrir el archivo personas.json por un error del sistema operativo: {error}")
    except PermissionError as error:
        print(f"ERROR: No se ha podido abrir el archivo personas.json por falta de permisos del programa: {error}")
    except Exception as error:
        print(f"ERROR: No se ha podido abrir el archivo personas.json: {error}")
    else:
        #Convierto nuevamente el nombre completo a tupla si este fue leido como list en un archivo json.
        for id, persona in diccionario_personas.items():
            if isinstance(persona, dict): # Evita la lectura del elmento con ID 0 que representa el tipo del archivo.
                if isinstance(persona.get("nombre_completo"), list):
                    persona["nombre_completo"] = tuple(persona["nombre_completo"])
    return diccionario_personas
def leer_archivo_tareas():
    """
    Lee el archivo tareas.json y devuelve un diccionario con los datos registrados. En caso de no ser encontrado, se lo genera con datos aleatorios.

    Returns:
        Dict: Diccionario de tareas
    """    
    # Se intenta la lectura del archivo tareas.json. 
    # De no existir el archivo, se generan los datos automáticamente. 
    # Se aplica manejo de excepciones en todos los casos posibles de fallo de lectura/escritura del archivo json.
    try:
        with open("tareas.json", "r", encoding="UTF-8") as arch_tareas:
            # Se leen los datos de tareas.json y se los guarda en un diccionario
            diccionario_tareas = json.load(arch_tareas)
            # NOTA: Se convierten las fechas en un formato legible por el módulo date.
            for id, elemento in diccionario_tareas.items():
                if isinstance(elemento, dict) and "fecha_límite" in elemento:
                    elemento["fecha_límite"] = datetime.datetime.strptime(elemento['fecha_límite'], "%d-%m-%Y").date()
            print("Info: Se ha leído correctamente los datos del archivo tareas.json")
    except FileNotFoundError:
        # Se generan los datos de forma alteatoria para el archivo tareas.json, se convierten las fechas a un formato legible para archivos json, y se los guarda. 
        print("Info: No se ha encontrado el archivo tareas.json")
        diccionario_tareas = tareas.generar_diccionario_tareas(4)
        for id, elemento in diccionario_tareas.items():
            if isinstance(elemento, dict) and "fecha_límite" in elemento:
                elemento["fecha_límite"] = elemento["fecha_límite"].strftime("%d-%m-%Y")
        try:
            with open("tareas.json", "w", encoding="UTF-8") as arch_tareas:
                # NOTA SOBRE ARGUMENTOS:
                # El argumento indent sirve para establecer los espacios de tabulación en el archivo json
                # El argumento ensure_ascii permite que existan dentro de este archivo carácteres pertenecientes a la lengua española, en este caso, por ejemplo, letras con tildación como la "á". 
                json.dump(diccionario_tareas, arch_tareas, indent=4, ensure_ascii=False)
                # NOTA: Convierto nuevamente los datos a un formato legible por el módulo date.
                for id, elemento in diccionario_tareas.items():
                    if isinstance(elemento, dict) and "fecha_límite" in elemento:
                        elemento["fecha_límite"] = datetime.datetime.strptime(elemento['fecha_límite'], "%d-%m-%Y").date()
                print("Info: Se ha generado el archivo tareas.json con datos aleatorios.")
        except OSError as error:
            print(f"ERROR: No se ha podido generar el archivo tareas.json por un error del sistema operativo: {error}")
        except PermissionError as error:
            print(f"ERROR: No se ha podido generar el archivo tareas.json por falta de permisos del programa: {error}")
        except:
            print("ERROR: No se ha podido generar el archivo tareas.json")
    except OSError as error:
        print(f"No se ha podido abrir el archivo tareas.json por un error del sistema operativo: {error}")
    except PermissionError as error:
        print(f"ERROR: No se ha podido abrir el archivo tareas.json por falta de permisos del programa: {error}")
    except Exception as error:
        print(f"ERROR: No se ha podido abrir el archivo tareas.json: {error}")
    return diccionario_tareas

def leer_archivo_asignaciones():
    matriz_asignaciones = []
    # Se intenta la lectura del archivo asignaciones.txt. 
    # De no existir el archivo, se generan los datos automáticamente. 
    # Se aplica manejo de excepciones en todos los casos posibles de fallo de lectura/escritura del archivo txt.
    try:
        with open("asignaciones.txt", "r", encoding="UTF-8") as arch_asignaciones:
            # Se leen los datos del archivo asignaciones.txt y se los convierte a cada formato correspondiente para que sean entendibles por las funciones de los otros modulos.
            for linea in arch_asignaciones:
                linea = linea.strip()
                # Salta el primer ciclo ya que es el nombre de la matriz
                if linea == "asignaciones":
                    matriz_asignaciones.append(linea)
                    continue
                id_asignacion, id_tarea, string_personas = linea.split(",")
                id_asignacion = int(id_asignacion)
                id_tarea = int(id_tarea)
                personas = list(map(int, string_personas.split("|")))
                matriz_asignaciones.append([id_asignacion, id_tarea, personas])
            print("Info: Se ha leído correctamente los datos del archivo asignaciones.txt")
            return matriz_asignaciones
    except FileNotFoundError:
        # Se generan los datos de forma alteatoria para el archivo asignaciones.txt y se los guarda en un archivo nuevo. Para ello debe utilizar las 2 funciones anteriores para obtener los datos.
        diccionario_personas = leer_archivo_personas()
        diccionario_tareas = leer_archivo_tareas()
        matriz_asignaciones = asignaciones.generar_matriz_asignaciones(diccionario_personas, diccionario_tareas)
        try:
            with open("asignaciones.txt", "w", encoding="UTF-8") as arch_asignaciones:
                for linea in matriz_asignaciones:
                    # Leyendo dato por dato generado, los va guardando en forma ordenada en el archivo asignaciones.txt
                    # Se desglosa la lista de personas asignadas para poder guardarlo de una forma mas comoda dentro del archivo de texto, y luego poder ser leido y procesado correctamente.
                    if linea == "asignaciones":
                        arch_asignaciones.write(f"{linea}\n")
                        continue
                    id_asignacion = linea[0]
                    id_tarea = linea[1]
                    personas_asignadas = "|".join(map(str, linea[2]))
                    arch_asignaciones.write(f"{id_asignacion},{id_tarea},{personas_asignadas}\n")
                print("Info: Se han generado los datos del archivo asignaciones.txt")
                return matriz_asignaciones
        except OSError as error:
            print(f"ERROR: No se ha podido generar el archivo asignaciones.txt por un error del sistema operativo: {error}")
        except PermissionError as error:
            print(f"ERROR: No se ha podido generar el archivo asignaciones.txt por falta de permisos del programa: {error}")
        except Exception as error:
            print(f"ERROR: No se ha podido generar el archivo asignaciones.txt: {error}")
    except OSError as error:
        print(f"ERROR: No se ha podido abrir el archivo asignaciones.txt por un error del sistema operativo: {error}")
    except PermissionError as error:
        print(f"ERROR: No se ha podido abrir el archivo asignaciones.txt por falta de permisos del programa: {error}")
    except Exception as error:
        print(f"ERROR: No se ha podido abrir el archivo asignaciones.txt: {error}")

os.system("cls") # NOTA: Esta función permite limpiar la consola al momento de iniciarse el programa.
print("Iniciando programa...")
print("----------------------------------------------------------------------")
print("Lectura/generación de datos:")
diccionario_personas = leer_archivo_personas()
diccionario_tareas = leer_archivo_tareas()
matriz_asignaciones = leer_archivo_asignaciones()
print("----------------------------------------------------------------------")