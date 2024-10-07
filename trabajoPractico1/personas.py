import random

def validar_diccionario_personas(diccionario: dict):
    """La función `validar_diccionario_personas` verifica si un elemento es de tipo `dict` y si éste a su vez representa personas.

    Args:
        diccionario (dict): Diccionario de personas objetivo

    Returns:
        True/False: Valor booleano que representa la validez del diccionario
    """    
    valido = True
    if not isinstance(diccionario, dict):
        print("ERROR FATAL: El elemento ingresado como lista no es un diccionario.")
        valido = False
    elif diccionario[0] != "personas":
        print("ERROR FATAL: El diccionario ingresada no es un diccionario de personas.")
        valido = False
    return valido

def validar_nombre_completo(nombre: str,apellido: str):
    """La función `validar_nombre_completo` verifica que los atributos sean nombres de personas, sin carácteres especiales. De lo contrario, los solicita nuevamente por consola.

    Args:
        nombre (str): Nombre a validar
        apellido (str): Apellido a validar

    Raises:
        Exception: En caso de que algún parámetro no sea de tipo str, lanza una excepción programada indicando el error.

    Returns:
        tuple: Tupla que contiene el nombre y el apellido validados.
    """    
    try:
        nombre_ = nombre
        apellido_ = apellido
        nombre_valido = nombre.isalpha()
        apellido_valido = apellido.isalpha()
        if not nombre_valido:
            print()
            print("ATENCIÓN: El nombre ingresado es inválido. Debe poseer sólo caracteres alfabéticos.")
            while not nombre_valido:
                nombre_ = input("Reingrese el nombre: ")
                print()
                if nombre_.isalpha():
                    nombre_valido = True
        elif not apellido_valido:
            print()
            print("ATENCIÓN: El apellido ingresado es inválido. Debe poseer sólo caracteres alfabéticos.")
            while not apellido_valido:
                apellido_ = input("Reingrese el apellido: ")
                print()
                if apellido_.isalpha():
                    apellido_valido = True
        return nombre_, apellido_
    except AttributeError:
        raise Exception(f"El/los atributo(s) pasado(s), '{nombre}' y/o '{apellido}', no son de tipo str, son de tipo {type(nombre)} y {type(apellido)}")

def generar_diccionario_personas(cantidad: int):
    """ La función `generar_diccionario_personas` crea un elemento de tipo `dict` en el cual cada `key` de su contenido representa el ID de cada persona, y el `value` representa los datos de la misma. En este caso, cada `value` posee dentro un sub-diccionario cuya `key` representa el tipo de dato, nombre completo, y su `value` esta compuesta por un `set` de nombre_apellido.

    Args:
        cantidad (int): La cantidad de personas que tenga el diccionario.

    Returns:
        dict: Diccionaro creado que representa las personas.
    """    
    
    #En base a una dos listas de nombres y apellidos, se genera un diccionario con la cantidad de personas solicitadas. El ID corresponde al key de cada elemento del diccionario.
    nombres = ["juan","maría","carlos","ana","pedro","laura","josé","marta","luis","sofía"]
    apellidos = ["garcía","lópez","martínez","pérez","rodríguez","sánchez","ramírez","torres","gómez","fernández"]
    diccionario_personas = {0: "personas"}
    for i in range(1, cantidad + 1):
        diccionario_personas[i] = {"nombre_completo": (random.choice(nombres), random.choice(apellidos))}
    return diccionario_personas

def crear_persona(diccionario: dict, nombre: str, apellido: str):
    """ La función `crear_persona` añade un nuevo elemento al diccionario solicitado con los datos del nombre y apellido otorgados.

    Args:
        diccionario (dict): Diccionario de personas objetivo
        nombre (str): Nombre de la persona
        apellido (str): Apellido de la persona
    """    
    #Verifico si los nombres ingresados son válidos.
    nombre_, apellido_ = validar_nombre_completo(nombre, apellido)
    
    #Cargo los datos, de ser válida, en el diccionario.
    if validar_diccionario_personas(diccionario):
        diccionario[len(diccionario)] = {"nombre_completo" : (nombre_, apellido_)}

def actualizar_persona(diccionario: dict,id: int, nombre: str,apellido: str):
    """ La función `actualizar_persona` actualiza los datos nombre y apellido del elemento solicitado presente el el diccionario dado.

    Args:
        diccionario (dict): Diccionario objetivo
        id (int): ID de la persona objetivo
        nombre (str): Nombre de la persona
        apellido (str): Apellido de la persona
    """    
    id_ = id
    nombre_, apellido_ = validar_nombre_completo(nombre, apellido)
    #Verifico el diccionario
    if validar_diccionario_personas(diccionario):
        #Verifico si el ID está presente en el diccionario.
        if not(id in diccionario.keys()):
            while not id_ in diccionario.keys():
                print(f"ATENCIÓN: El ID '{id}' no se encuentra presente dentro del diccionario.")
                id_ = input("Reingrese el ID: ")
                print()
        #Cambio el dato solicitado.
        diccionario[id_] = {"nombre_completo": (nombre_, apellido_)}

def eliminar_persona(diccionario: dict,id: int):
    """La función `eliminar_persona` elimina la persona objetivo del diccionario otorgado en base a su ID dado.

    Args:
        diccionario (dict): Diccionario objetivo
        id (int): ID de la persona a eliminar
    """    
    #Verifico el diccionario y el ID
    if validar_diccionario_personas(diccionario):
        if id in diccionario.keys():
            #Elimino el elemnto con el ID correspondiente
            diccionario.pop(id)