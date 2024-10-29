import personas
import tareas
import asignaciones
import datetime
import json

def leer_archivo_personas():
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
    except:
        print("ERROR: No se ha podido abrir el archivo personas.json")
    else:
        #Convierto nuevamente el nombre completo a tupla si este fue leido como list en un archivo json.
        for id, persona in diccionario_personas.items():
            if isinstance(persona, dict): # Evita la lectura del elmento con ID 0 que representa el tipo del archivo.
                if isinstance(persona.get("nombre_completo"), list):
                    persona["nombre_completo"] = tuple(persona["nombre_completo"])
    return diccionario_personas

def leer_archivo_tareas():
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
                    elemento["fecha_límite"] = datetime.strptime(elemento['fecha_límite'], "%d-%m-%Y").date()
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
                        elemento["fecha_límite"] = datetime.strptime(elemento['fecha_límite'], "%d-%m-%Y").date()
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
    except:
        print("ERROR: No se ha podido abrir el archivo tareas.json")
    return diccionario_tareas

dict_personas = leer_archivo_personas()
dict_tareas = leer_archivo_tareas()

print(dict_personas)
print()
print(dict_tareas)
