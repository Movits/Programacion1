import personas
import tareas
import asignaciones
import datetime
import json
import os

def obtener_matriz_personas_recursivamente(archivo, matriz_asignaciones=[]):
    """Le una matriz de personas de manera recursiva

    Args:
        archivo (TextIOWrapper): Archivo con los datos de las asignaciones
        matriz_asignaciones (list, opcional): La matriz de asignaciones hasta el momento leída.

    Returns:
        asignaciones (list): Matriz de asignaciones obtenida.
    """    
    linea = archivo.readline().strip()
    if not linea:
        return matriz_asignaciones  # Caso final: Si no hay mas líneas, devuelve la matriz terminada
    
    # Añade el encabezado a la matriz generada y lee los elementos de las siguientes líneas
    if linea != "asignaciones":
        id_asignacion, id_tarea, string_personas = linea.split(",")
        id_asignacion = int(id_asignacion)
        id_tarea = int(id_tarea)
        personas = list(map(int, string_personas.split("|")))
        matriz_asignaciones.append([id_asignacion, id_tarea, personas])
    else:
        matriz_asignaciones.append(linea)
    
    return obtener_matriz_personas_recursivamente(archivo, matriz_asignaciones)

# Lectura de datos
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
            diccionario_personas = {int(key): value for key, value in diccionario_personas.items()} # Convierto las keys (IDs) en enteros nuevamente para evitar conflictos.
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
            diccionario_tareas = {int(key): value for key, value in diccionario_tareas.items()}
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
    """
    Lee el archivo asignaciones.txt y devuelve una matriz con los datos registrados. En caso de no ser encontrado, lo genera con datos aleatorios utilizando los diccionarios de personas y tareas.

    Returns:
        list: Matriz de asignaciones
    """
    matriz_asignaciones = []
    # Se intenta la lectura del archivo asignaciones.txt. 
    # De no existir el archivo, se generan los datos automáticamente. 
    # Se aplica manejo de excepciones en todos los casos posibles de fallo de lectura/escritura del archivo txt.
    try:
        with open("asignaciones.txt", "r", encoding="UTF-8") as arch_asignaciones:
            matriz_asignaciones = obtener_matriz_personas_recursivamente(arch_asignaciones)
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

# Muestreo de datos
def imprimir_asignaciones(matriz_asignaciones: list, diccionario_tareas: dict, diccionario_personas: dict):
    """Imprime la tabla con las asignaciones que hay en memoria

    Args:
        matriz_asignaciones (list): Matriz de las asignaciones
        diccionario_tareas (dict): Diccionario de las tareas
        diccionario_personas (dict): Diccionario de las personas
    """    
    if diccionario_personas[0] != "personas":
        print("¡ATENCIÓN!: El elemento pasado como diccionario_personas no es un diccionario de personas.")
    elif diccionario_tareas[0] != "tareas":
        print("¡ATENCIÓN!: El elemento pasado como diccionario_tareas no es un diccionario de tareas.")
    elif matriz_asignaciones[0] != "asignaciones":
        print("¡ATENCIÓN!: El elemento pasado como matriz_asignaciones no es una matriz de asignaciones.")
    else:
        contador_asignacion = 0
        for asignacion in matriz_asignaciones:
            #Formatos de la tabla
            ancho_id_asignacion = 14
            ancho_id_tarea = 7
            ancho_descripcion_tarea = 50
            ancho_nombre_completo = 25
            ancho_estado = 10
            ancho_total = 137
            ancho_fecha_limite = 16
            
            if asignacion == "asignaciones":
                print("-" * ancho_total)
                print(asignacion.upper().center(ancho_total))
                print("-" * ancho_total)
                print(f"{'asignación'.capitalize().center(ancho_id_asignacion)} | {'tarea'.capitalize().center(ancho_id_tarea)} | {'descripcion'.capitalize().center(ancho_descripcion_tarea)} | {'asignados'.capitalize().center(ancho_nombre_completo)} | {'estado'.capitalize().center(ancho_estado)} | {'fecha límite'.capitalize().center(ancho_fecha_limite)}")
                print("-" * ancho_total)
                contador_asignacion +=1
                continue
            
            #Datos de la tabla
            id_asignacion = matriz_asignaciones[contador_asignacion][0]
            id_tarea = matriz_asignaciones[contador_asignacion][1]
            descripcion_tarea = diccionario_tareas[id_tarea]["descripcion"]
            if diccionario_tareas[id_tarea]["estado"] == 0:
                estado = "retrasada" 
            elif diccionario_tareas[id_tarea]["estado"] == 1:
                estado = "pendiente"
            elif diccionario_tareas[id_tarea]["estado"] == 2:
                estado = "en proceso"
            else:
                estado = "finalizada"
            estado = estado.center(ancho_estado)
            fecha_limite = diccionario_tareas[id_tarea]["fecha_límite"].strftime("%d-%m-%Y")
            
            contador_persona = 0
            for i in range(1, len(matriz_asignaciones[contador_asignacion][2])+1):
                if contador_persona == 0:
                    nombre_completo = f"{diccionario_personas[matriz_asignaciones[contador_asignacion][2][0]]['nombre_completo'][0]} {diccionario_personas[matriz_asignaciones[contador_asignacion][2][0]]['nombre_completo'][1]}".center(ancho_nombre_completo)
                    print(f"{str(id_asignacion).center(ancho_id_asignacion)} | {str(id_tarea).center(ancho_id_tarea)} | {str(descripcion_tarea).capitalize().center(ancho_descripcion_tarea)} | {str(nombre_completo).title().center(ancho_nombre_completo)} | {str(estado).capitalize().center(ancho_estado)} | {str(fecha_limite).center(ancho_fecha_limite)}")
                    contador_persona += 1
                else:
                    nombre_completo = f"{diccionario_personas[matriz_asignaciones[contador_asignacion][2][contador_persona]]['nombre_completo'][0]} {diccionario_personas[matriz_asignaciones[contador_asignacion][2][contador_persona]]['nombre_completo'][1]}".center(ancho_nombre_completo)
                    print(f"{' '.center(ancho_id_asignacion)} | {' '.center(ancho_id_tarea)} | {' '.center(ancho_descripcion_tarea)} | {str(nombre_completo).title().center(ancho_nombre_completo)} | {' '.center(ancho_estado)} | {' '.center(ancho_fecha_limite)}")
                    contador_persona += 1
            contador_asignacion +=1
            print("-" * ancho_total)
def imprimir_tareas(diccionario_tareas: dict):
    """Imprime la tabla de tareas que hay en la memoria

    Args:
        diccionario_tareas (dict): Diccionario de tareas
    """    
    # Formato de la tabla
    ancho_id_tarea = 7
    ancho_descripcion_tarea = 50
    ancho_estado = 12
    ancho_fecha_limite = 16
    ancho_total = 92
    
    for id_tarea in diccionario_tareas.keys():
        if id_tarea == 0:
            print("-" * ancho_total)
            print(f"{str(diccionario_tareas[id_tarea]).upper().center(ancho_total)}")
            print("-" * ancho_total)
            print(f"{'tarea'.capitalize().center(ancho_id_tarea)} | {'descripción'.capitalize().center(ancho_descripcion_tarea)} | {'estado'.capitalize().center(ancho_estado)} | {'fecha límite'.capitalize().center(ancho_fecha_limite)}")
            print("-" * ancho_total)
        else:
            descripcion_tarea = str(diccionario_tareas[id_tarea]["descripcion"])
            if diccionario_tareas[id_tarea]["estado"] == 0:
                estado = "retrasada" 
            elif diccionario_tareas[id_tarea]["estado"] == 1:
                estado = "pendiente"
            elif diccionario_tareas[id_tarea]["estado"] == 2:
                estado = "en proceso"
            else:
                estado = "finalizada"
            fecha_limite = diccionario_tareas[id_tarea]["fecha_límite"].strftime("%d-%m-%Y")
            
            print(f"{str(id_tarea).center(ancho_id_tarea)} | {descripcion_tarea.capitalize().center(ancho_descripcion_tarea)} | {estado.capitalize().center(ancho_estado)} | {str(fecha_limite).center(ancho_fecha_limite)}")
            print("-" * ancho_total)
def imprimir_personas(diccionario_personas: dict):
    """Imprime el diccionario de personas que hay en memoria

    Args:
        diccionario_personas (dict): diccionario de personas
    """    
    # Formato de la tabla
    ancho_id_persona = 11
    ancho_nombre_completo = 25
    ancho_usuario = 15
    ancho_email = 30
    ancho_telefono = 17
    ancho_contrasenia = 25
    ancho_total = 138
    
    for id_persona in diccionario_personas.keys():        
        if id_persona == 0:
            print("-" * ancho_total)
            print(str(diccionario_personas[id_persona]).upper().center(ancho_total))
            print("-" * ancho_total)
            print(f"{'persona'.capitalize().center(ancho_id_persona)} | {'nombre completo'.capitalize().center(ancho_nombre_completo)} | {'usuario'.capitalize().center(ancho_usuario)} | {'email'.capitalize().center(ancho_email)} | {'teléfono'.capitalize().center(ancho_telefono)} | {'contraseña'.capitalize().center(ancho_contrasenia)}")
            print("-" * ancho_total)
        else:
            # Datos de la tabla
            nombre_completo = f"{diccionario_personas[id_persona]['nombre_completo'][0]} {diccionario_personas[id_persona]['nombre_completo'][1]}"
            usuario = diccionario_personas[id_persona]["usuario"]
            email = diccionario_personas[id_persona]["email"]
            telefono = diccionario_personas[id_persona]["telefono"]
            contrasenia = diccionario_personas[id_persona]["contrasenia"]   
            print(f"{str(id_persona).center(ancho_id_persona)} | {nombre_completo.capitalize().center(ancho_nombre_completo)} | {str(usuario).center(ancho_usuario)} | {str(email).center(ancho_email)} | {str(telefono).center(ancho_telefono)} | {str(contrasenia).center(ancho_contrasenia)}")
            print("-" * ancho_total)

# Escritura de datos en los archivos
def escribir_archivo_personas(diccionario_personas: dict):
    """Escribqe en el archivo personas.json los datos de personas guardados en memoria

    Args:
        diccionario_personas (dict): Diccionario de personas
    """    
    if diccionario_personas[0] == "personas":
        try:
            with open("personas.json", "w", encoding="UTF-8") as arch_personas:
                json.dump(diccionario_personas, arch_personas, indent=4, ensure_ascii=False)
                print("Info: Se ha escrito la información de personas procesada en el archivo personas.json")
        except OSError as error:
            print(f"ERROR: No se ha podido escribir el archivo personas.json por un error del sistema operativo: {error}")
        except PermissionError as error:
            print(f"ERROR: No se ha podido escribir el archivo personas.json por falta de permisos del programa: {error}")
        except Exception as error:
            print(f"ERROR: No se ha podido escribir el archivo personas.json: {error}")
    else:
        print("¡ATENCIÓN!: Se ha intentado escribir otro tipo de dato en el archivo personas.json pero se ha evitado")
        print("Info: No se ha escrito ningún dato en personas.json")
def escribir_archivo_tareas(diccionario_tareas: dict):
    """Escribe en el archivo tareas.josn los datos de las tareas que hay en memoria

    Args:
        diccionario_tareas (dict): Diccionario de tareas
    """    
    # Verifico que el diccionario sea efectivamente de tareas.
    if diccionario_tareas[0] == "tareas":
        # Convierto los datos de fecha a un formato legible por un archivo JSON (DD/MM/AAAA)
        for id, elemento in diccionario_tareas.items():
            if isinstance(elemento, dict) and "fecha_límite" in elemento:
                elemento["fecha_límite"] = elemento["fecha_límite"].strftime("%d-%m-%Y")
        # Paso a escribir directamente los datos luego de ser adaptados..
        try:
            with open("tareas.json", "w", encoding="UTF-8") as arch_tareas:
                json.dump(diccionario_tareas, arch_tareas, indent=4, ensure_ascii=False)
                print("Info: Se ha escrito la información de tareas procesada en el archivo tareas.json")
        except OSError as error:
            print(f"ERROR: No se ha podido escribir el archivo tareas.json por un error del sistema operativo: {error}")
        except PermissionError as error:
            print(f"ERROR: No se ha podido escribir el archivo tareas.json por falta de permisos del programa: {error}")
        except Exception as error:
            print(f"ERROR: No se ha podido escribir el archivo tareas.json: {error}")
    else:
        print("¡ATENCIÓN!: Se ha intentado escribir otro tipo de dato en el archivo tareas.json pero se ha evitado")
        print("Info: No se ha escrito ningún dato en tareas.json")
def escribir_archivo_asignaciones(matriz_asignaciones: list):
    """Escribe en el archivo asignaciones.txt los datos de las asignaciones que hay en memoria

    Args:
        matriz_asignaciones (list): Matriz de asignaciones
    """    
    try:
        with open("asignaciones.txt", "w", encoding="UTF-8") as arch_asignaciones:
            for linea in matriz_asignaciones:
                if linea == "asignaciones":
                    arch_asignaciones.write(f"{linea}\n")
                    continue
                id_asignacion = linea[0]
                id_tarea = linea[1]
                personas_asignadas = "|".join(map(str, linea[2]))
                arch_asignaciones.write(f"{id_asignacion},{id_tarea},{personas_asignadas}\n")
            print("Info: Se ha escrito la información de asignaciones procesada en el archivo asignaciones.txt")
    except OSError as error:
        print(f"ERROR: No se ha podido escribir el archivo asignaciones.txt por un error del sistema operativo: {error}")
    except PermissionError as error:
        print(f"ERROR: No se ha podido escribir el archivo asignaciones.txt por falta de permisos del programa: {error}")
    except Exception as error:
        print(f"ERROR: No se ha podido escribir el archivo asignaciones.txt: {error}")

# Lectura de datos en consola
# NOTA: Su propósito es evitar que el programa colapse si el usuario proporciona un dato con formato inválido o de tipo incorrecto cuando sea solicitado.
def solicitar_entero(mensaje_en_consola: str):
    """Permite solicitar una entrada y que sólo sea aceptada cuando esta sea un número entero.

    Args:
        mensaje_en_consola (str): Mensaje que se desee mostrar en consola al esperar la entrada

    Returns:
        entrada (str): El valor que se aceptará
    """    
    while True:
        try:
            entrada = int(input(mensaje_en_consola))
            return entrada
        except ValueError:
            print()
            print("¡ATENCIÓN!: Entrada inválida. Por favor, ingrese un número entero.")
def solicitar_fecha(mensaje_en_consola: str):
    """Permite solicitar una entrada y que sólo sea aceptada cuando esta sea una fecha con formato válido.

    Args:
        mensaje_en_consola (str): Mensaje que se desee mostrar en consola al esperar la entrada

    Returns:
        entrada (str): El valor que se aceptará
    """   
    while True:
        try:
            entrada = datetime.datetime.strptime(input(mensaje_en_consola), "%d/%m/%Y").date()
            return entrada
        except ValueError:
            print()
            print("¡ATENCIÓN!: Fecha inválida. Por favor, ingrese una fecha con formato (DD/MM/AAAA)")

os.system("cls") # NOTA: Esta función permite limpiar la consola al momento de iniciarse el programa.
print("Iniciando programa...")
print("----------------------------------------------------------------------")
print("Lectura/generación de datos:")
diccionario_personas = leer_archivo_personas()
diccionario_tareas = leer_archivo_tareas()
matriz_asignaciones = leer_archivo_asignaciones()
print("----------------------------------------------------------------------")
print("Programa iniciado con éxito.")

mensaeje_de_situacion = "Bienvenido"

# Menú de navegación
while True:
    os.system("cls")
    print(mensaeje_de_situacion)
    print()
    print("Menú principal")
    print("1. Ver asignaciones")
    print("2. Ver tareas")
    print("3. Ver personas")
    print("4. Finalizar programa")
    print()
    opcion = input()
    
    if opcion == str(1):
        os.system("cls")
        imprimir_asignaciones(matriz_asignaciones, diccionario_tareas, diccionario_personas)
        print()
        print("Ver asignaciones")
        print("1. Crear asignación")
        print("2. Actualizar asignación")
        print("3. Eliminar asignación")
        print("4. Volver")
        print()
        opcion = input()
        
        if opcion == str(1):
            os.system("cls")
            imprimir_tareas(diccionario_tareas)
            print()
            print("Crear asignación")
            id_tarea = solicitar_entero("Ingrese el ID de la tarea a asignar (Ingrese -1 para volver): ")
            if id_tarea != -1:
                personas_asignadas = []
                while True:
                    os.system("cls")
                    imprimir_personas(diccionario_personas)
                    print()
                    print("Crear asignación")
                    if len(personas_asignadas) != 0:
                        print(f"Info: Personas asignadas: {personas_asignadas}")
                    persona = solicitar_entero("Ingrese el ID de la siguiente persona a asignar (-1 para terminar): ")
                    if not persona == -1:
                        personas_asignadas.append(persona)
                    else:
                        break
                if len(personas_asignadas) > 0:
                    mensaeje_de_situacion = asignaciones.crear_asignacion(matriz_asignaciones, list(diccionario_personas.keys()), list(diccionario_tareas.keys()), id_tarea, personas_asignadas)
                else:
                    mensaeje_de_situacion = "Info: No se ha asignado a ninguna persona al no haber proporcionado ninguna."
            else:
                mensaeje_de_situacion = "Volviendo al menú principal... "

        elif opcion == str(2):
            os.system("cls")
            imprimir_asignaciones(matriz_asignaciones, diccionario_tareas, diccionario_personas)
            print()
            print("Actualizar asignación")
            id_tarea = solicitar_entero("Ingrese el ID de la tarea cuya asignación que desee actualizar (Ingrese -1 para volver): ")
            if id_tarea != -1:
                personas_asignadas = []
                while True:
                    os.system("cls")
                    imprimir_personas(diccionario_personas)
                    print()
                    print("Actualizar asignación")
                    if len(personas_asignadas) != 0:
                        print(f"Info: Personas asignadas: {personas_asignadas}")
                    persona = solicitar_entero("Ingrese el ID de la siguiente persona a asignar (-1 para terminar): ")
                    if not persona == -1:
                        personas_asignadas.append(persona)
                    else:
                        break
                if len(personas_asignadas) > 0:
                    mensaeje_de_situacion = asignaciones.actualizar_asignacion(matriz_asignaciones, list(diccionario_personas.keys()), list(diccionario_tareas.keys()), id_tarea, personas_asignadas)
                else: 
                    mensaeje_de_situacion = "Info: No se ha actualizado ninguna asignación al no haberse proporcionado ninguna persona"
            else:
                mensaeje_de_situacion = "Volviendo al menú principal... "

        elif opcion == str(3):
            os.system("cls")
            imprimir_asignaciones(matriz_asignaciones, diccionario_tareas, diccionario_personas)
            print()
            print("Eliminar asignación")
            id_tarea = solicitar_entero("Ingrese el ID tarea cuya asignación desee eliminar (Ingrese -1 para volver): ")
            if id_tarea != -1:
                mensaeje_de_situacion = asignaciones.eliminar_asignacion(matriz_asignaciones, id_tarea)
            else:  
                mensaeje_de_situacion = "Volviendo al menú principal..."
        else:
            mensaeje_de_situacion = "Volviendo al menú principal..."

    elif opcion == str(2):
        os.system("cls")
        imprimir_tareas(diccionario_tareas)
        print()
        print("Ver tareas")
        print("1. Crear tarea")
        print("2. Actualizar tarea")
        print("3. Eliminar Tarea")
        print("4. Volver")
        print()
        opcion = input()
        
        if opcion == str(1):
            os.system("cls")
            imprimir_tareas(diccionario_tareas)
            print()
            print("Crear tarea")
            descripcion_tarea = input("Ingrese la descripción de su nueva tarea: ")
            fecha_limite = solicitar_fecha("Ingrese la fecha límite de entrega para su nueva tarea (DD/MM/AAAA): ")
            mensaeje_de_situacion = tareas.crear_tarea(diccionario_tareas, descripcion_tarea, fecha_limite)

        elif opcion == str(2):
            os.system("cls")
            imprimir_tareas(diccionario_tareas)
            print()
            print("Actualizar tarea")
            print("1. Actualizar descripción de la tarea")
            print("2. Actualizar estado de la tarea")
            print("3. Actualizar fecha límite de entrega de la tarea")
            print("4. Volver")
            print()
            opcion = input()

            if opcion == str(1):
                os.system("cls")
                imprimir_tareas(diccionario_tareas)
                print()
                print("Actualizar descripción de la tarea")
                id_tarea = solicitar_entero("Ingrese el ID de la tarea cuya descripción desee actualizar (Ingrese -1 para volver): ")
                if id_tarea != -1:
                    descripcion = input("Ingrese la descripción de la tarea: ")
                    mensaeje_de_situacion = tareas.actualizar_tarea(diccionario_tareas, id_tarea, descripcion, diccionario_tareas[id_tarea]["fecha_límite"].strftime("%d/%m/%Y"), diccionario_tareas[id_tarea]["estado"])
                else:
                    mensaeje_de_situacion = "Volviendo al menú principal..."

            elif opcion == str(2):
                os.system("cls")
                imprimir_tareas(diccionario_tareas)
                print()
                print("Actualizar estado de la tarea")
                id_tarea = solicitar_entero("Ingrese el ID de la tarea cuya descripción desee actualizar (Ingrese -1 para volver): ")
                if id_tarea != -1:
                    estado = solicitar_entero("Ingrese el estado a asignarle a la tarea seleccionadada (1: Pendiente, 2: En proceso, 3: Finalizada): ")
                    while estado < 1 or estado > 3:
                        print("¡ATENCIÓN!: El estado que has ingresado es inválido. Por favor, ingresa un estado valido")
                        estado = solicitar_entero("1: Pendiente, 2: En proceso, 3: Finalizada: ")
                    mensaeje_de_situacion = tareas.actualizar_tarea(diccionario_tareas, id_tarea, diccionario_tareas[id_tarea]["descripcion"], diccionario_tareas[id_tarea]["fecha_límite"].strftime("%d/%m/%Y"), estado)
                else:
                    mensaeje_de_situacion = "Volviendo al menú principal..."

            elif opcion == str(3):
                os.system("cls")
                imprimir_tareas(diccionario_tareas)
                print()
                print("Actualizar fecha límite de entrega de la tarea")
                id_tarea = solicitar_entero("Ingrese el ID de la tarea cuya descripción desee actualizar (Ingrese -1 para volver): ")
                if id_tarea != -1:
                    fecha_limite = solicitar_fecha("Ingrese la fecha límite de entrega para su nueva tarea (DD/MM/AAAA): ")
                    mensaeje_de_situacion = tareas.actualizar_tarea(diccionario_tareas, id_tarea, diccionario_tareas[id_tarea]["descripcion"], fecha_limite.strftime("%d/%m/%Y"), diccionario_tareas[id_tarea]["estado"])
                else:
                    mensaeje_de_situacion = "Volviendo al menú principal..."
            else:
                mensaeje_de_situacion = "Volviendo al menú principal..."
        elif opcion == str(3):
            os.system("cls")
            imprimir_tareas(diccionario_tareas)
            print()
            print("Eliminar tarea")
            id_tarea = solicitar_entero("Ingrese el ID de la tarea que desee eliminar (Ingrese -1 para volver): ")
            mensaeje_de_situacion = tareas.eliminar_tarea(diccionario_tareas, id_tarea)
            asignaciones.eliminar_asignacion(matriz_asignaciones, id_tarea, "Eliminar")
        else:
            mensaeje_de_situacion = "Volviendo al menú principal..."

    elif opcion == str(3):
        os.system("cls")
        imprimir_personas(diccionario_personas)
        print()
        print("Ver personas")
        print("1. Crear persona")
        print("2. Actualizar persona")
        print("3. Eliminar persona")
        print("4. Volver")
        print()
        opcion = input()
        
        if opcion == str(1):
            os.system("cls")
            imprimir_personas(diccionario_personas)
            print()
            print("Crear persona")
            # Se solicitan todos los datos de la nueva persona.
            nombre, apellido = personas.validar_nombre_completo(input("* Ingrese el primer nombre de su nueva persona: "), input("* Ingrese el apellido de su nueva persona: "))
            usuario = personas.generar_usuario(nombre, apellido, diccionario_personas)
            print(f"Info: Se ha generado su nombre de usuario: {usuario}")
            email = personas.validar_email(diccionario_personas, input("* Ingrese el email de su nueva persona: "))
            telefono = personas.validar_telefono(diccionario_personas, input("* Ingrese el número de teléfono de su nueva persona: "))
            contrasenia = personas.validar_contrasenia(input("* Ingrese una contrasenia para su nuevo usuario: "))
            mensaeje_de_situacion = personas.crear_persona(diccionario_personas, nombre, apellido, usuario, email, telefono, contrasenia)
        
        elif opcion == str(2):
            os.system("cls")
            imprimir_personas(diccionario_personas)
            print()
            print("Actualizar persona")
            print("1. Actualizar nombre completo")
            print("2. Actualizar nombre de usuario")
            print("3. Actualizar email")
            print("4. Actualizar número de teléfono")
            print("5. Actualizar contraseña")
            print("6. Volver")
            print()
            opcion = input()
            
            if opcion == str(1):
                os.system("cls")
                imprimir_personas(diccionario_personas)
                print()
                print("Actualizar nombre completo")
                id_persona = solicitar_entero("Ingrese el ID de la persona cuyo nombre completo quiera actualizar (Ingrese -1 para volver): ")
                if id_persona != -1:
                    nombre, apellido = personas.validar_nombre_completo(input("Ingrese el nuevo nombre de la persona: "), input("Ingrese el nuevo apellido de la persona: "))
                    mensaeje_de_situacion = personas.actualizar_persona(diccionario_personas, id_persona, nombre, apellido, diccionario_personas[id_persona]["usuario"], diccionario_personas[id_persona]["email"], diccionario_personas[id_persona]["telefono"], diccionario_personas[id_persona]["contrasenia"])
                else:
                    mensaeje_de_situacion = "Volviendo al menú principal..."
            
            elif opcion == str(2):
                os.system("cls")
                imprimir_personas(diccionario_personas)
                print()
                print("Actualizar nombre de usuario")
                id_persona = solicitar_entero("Ingrese el ID de la persona cuyo nombre de usuario quiera actualizar (Ingrese -1 para volver): ")
                if id_persona != -1:
                    usuario = input("Ingrese el nuevo nombre de usuario de la persona: ")
                    mensaeje_de_situacion = personas.actualizar_persona(diccionario_personas, id_persona, diccionario_personas[id_persona]["nombre_completo"][0], diccionario_personas[id_persona]["nombre_completo"][1], usuario, diccionario_personas[id_persona]["email"], diccionario_personas[id_persona]["telefono"], diccionario_personas[id_persona]["contrasenia"])
                else:
                    mensaeje_de_situacion = "Volviendo al menú principal..."
            
            elif opcion == str(3):
                os.system("cls")
                imprimir_personas(diccionario_personas)
                print()
                print("Actualizar email")
                id_persona = solicitar_entero("Ingrese el ID de la persona cuyo email quiera actualizar (Ingrese -1 para volver): ")
                if id_persona != -1:
                    email = personas.validar_email(diccionario_personas, input("Ingrese el nuevo email de la persona: "))
                    mensaeje_de_situacion = personas.actualizar_persona(diccionario_personas, id_persona, diccionario_personas[id_persona]["nombre_completo"][0], diccionario_personas[id_persona]["nombre_completo"][1], diccionario_personas[id_persona]["usuario"], email, diccionario_personas[id_persona]["telefono"], diccionario_personas[id_persona]["contrasenia"])
                else:
                    mensaeje_de_situacion = "Volviendo al menú principal..."
                
            elif opcion == str(4):
                os.system("cls")
                imprimir_personas(diccionario_personas)
                print()
                print("Actualizar número de teléfono")
                id_persona = solicitar_entero("Ingrese el ID de la persona cuyo número de teléfono quiera actualizar (Ingrese -1 para volver): ")
                if id_persona != -1:
                    telefono = personas.validar_telefono(diccionario_personas, input("Ingrese el nuevo número de teléfono de la persona: "))
                    mensaeje_de_situacion = personas.actualizar_persona(diccionario_personas, id_persona, diccionario_personas[id_persona]["nombre_completo"][0], diccionario_personas[id_persona]["nombre_completo"][1], diccionario_personas[id_persona]["usuario"], diccionario_personas[id_persona]["email"], telefono, diccionario_personas[id_persona]["contrasenia"])
                else:
                    mensaeje_de_situacion = "Volviendo al menú principal..."
            
            elif opcion == str(5):
                os.system("cls")
                imprimir_personas(diccionario_personas)
                print()
                print("Actualizar contraseña")
                id_persona = solicitar_entero("Ingrese el ID de la persona cuya contraseña quiera actualizar (Ingrese -1 para volver): ")
                if id_persona != -1:
                    contrasenia = personas.validar_contrasenia(input("Ingrese la nueva contraseña de la persona: "))
                    mensaeje_de_situacion = personas.actualizar_persona(diccionario_personas, id_persona, diccionario_personas[id_persona]["nombre_completo"][0], diccionario_personas[id_persona]["nombre_completo"][1], diccionario_personas[id_persona]["usuario"], diccionario_personas[id_persona]["email"], diccionario_personas[id_persona]["telefono"], contrasenia)
                else:
                    mensaeje_de_situacion = "Volviendo al menú principal..."
            else:
                mensaeje_de_situacion = "Volviendo al menú principal..."

        elif opcion == str(3):
            os.system("cls")
            imprimir_personas(diccionario_personas)
            print()
            print("Eliminar persona")
            id_persona = solicitar_entero("Ingrese el ID de la persona que desee eliminar (Ingrese -1 para volver): ")
            if id_persona != -1:
                mensaeje_de_situacion = personas.eliminar_persona(diccionario_personas, id_persona)
                # Elimino todas las vinculaciones que tenga la persona en las asignaciones
                for asignacion in matriz_asignaciones[1:]:
                    personas_asignadas = asignacion[2]
                    if id_persona in personas_asignadas:
                        personas_asignadas.remove(id_persona)
                    # Verifica si una asignación se quedó sin personas asignadas. De ser así, elimina directamente la asignación
                    if len(asignacion[2]) == 0:
                        del matriz_asignaciones[asignacion[0]]
            else:
                mensaeje_de_situacion = "Volviendo al menú principal..."
        
        else:
            mensaeje_de_situacion = "Volviendo al menú principal..."
                    
    elif opcion == str(4):
        break

os.system("cls")

print("-------------------------------------------------------------------------------------------")
escribir_archivo_personas(diccionario_personas)
escribir_archivo_tareas(diccionario_tareas)
escribir_archivo_asignaciones(matriz_asignaciones)
print("-------------------------------------------------------------------------------------------")

print()
print("Fin del programa. ¡Gracias por ver!")