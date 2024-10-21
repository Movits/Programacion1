import random
import string
import re

def validar_diccionario_personas(diccionario: dict):
    """La función `validar_diccionario_personas` verifica si un elemento es de tipo `dict` y si éste a su vez representa personas.

    Args:
        diccionario (dict): Diccionario de personas objetivo.

    Returns:
        True/False: Valor booleano que representa la validez del diccionario.
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
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        usuario = generar_usuario(nombre, apellido, diccionario_personas)
        email = generar_email(nombre, apellido)
        telefono = generar_telefono()
        contrasenia = generar_contrasenia()
        
        diccionario_personas[i] = {
            "nombre_completo": (nombre, apellido),
            "usuario": usuario,
            "email": email,
            "telefono": telefono,
            "contrasenia": contrasenia
        }

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
        usuario = generar_usuario(nombre_, apellido_, diccionario)
        email = generar_email(nombre_, apellido_)
        telefono = generar_telefono()
        contrasenia = generar_contrasenia()
        
        diccionario[len(diccionario)] = {
            "nombre_completo": (nombre_, apellido_),
            "usuario": usuario,
            "email": email,
            "telefono": telefono,
            "contrasenia": contrasenia
        }

def actualizar_persona(diccionario: dict,id: int, nombre: str,apellido: str):
    """ Actualiza el nombre y apellido de la persona con el ID dado en el diccionario.

    Args:
        diccionario (dict): Diccionario objetivo
        id (int): ID de la persona objetivo
        nombre (str): Nombre de la persona
        apellido (str): Apellido de la persona
    """    
    nombre_, apellido_ = validar_nombre_completo(nombre, apellido)
    
    if validar_diccionario_personas(diccionario):
        if id not in diccionario:
            print(f"Error: El ID '{id}' no se encuentra en el diccionario.")
            return  # Return early to avoid updating a non-existent entry
        
        usuario = generar_usuario(nombre_, apellido_, diccionario)
        email = generar_email(nombre_, apellido_)
        
        diccionario[id]["nombre_completo"] = (nombre_, apellido_)
        diccionario[id]["usuario"] = usuario
        diccionario[id]["email"] = email

def eliminar_persona(diccionario: dict,id: int):
    """Elimina la persona con el ID dado del diccionario.

    Args:
        diccionario (dict): Diccionario objetivo
        id (int): ID de la persona a eliminar
    """    
    #Verifico el diccionario y el ID
    if validar_diccionario_personas(diccionario):
        if id in diccionario.keys():
            #Elimino el elemnto con el ID correspondiente
            diccionario.pop(id)
        else: 
            print(f"Error: El ID '{id}' no se encuentra en el diccionario.")
            

def generar_usuario(nombre: str, apellido: str, diccionario: dict):
    usuario_base = f"{nombre[0].lower()}{apellido.lower()}"
    usuario = usuario_base
    cont = 1
    usuarios_existentes = set()
    for persona in diccionario.values(): #Recorro el diccionario para verificar si el usuario ya existe.
        if isinstance(persona, dict) and "usuario" in persona:
            usuarios_existentes.add(persona["usuario"])
    while usuario in usuarios_existentes: 
        usuario = f"{usuario_base}{cont}" 
        cont += 1
    return usuario


def actualizar_usuario(diccionario: dict, id: int, nuevo_usuario: str):
    usuarios_existentes = set()
    for persona in diccionario.values():
        if isinstance(persona, dict) and "usuario" in persona:
            usuarios_existentes.add(persona["usuario"])
    
    if nuevo_usuario in usuarios_existentes:
        raise ValueError(f"El nombre de usuario '{nuevo_usuario}' ya existe.")
    
    diccionario[id]["usuario"] = nuevo_usuario
    
        
def eliminar_usuario(diccionario: dict, id: int):
    diccionario[id].pop("usuario")
    diccionario[id].pop("contrasenia")
    diccionario[id].pop("email")
    diccionario[id].pop("telefono")
    
    
def generar_contrasenia():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasenia = "".join(random.choices(caracteres, k=8)) #8 caracteres
    return contrasenia

def actualizar_contrasenia(diccionario: dict, id: int, contrasenia: str):
    posee_caracter_especial = re.search(r"[!@#$%^&*]" ,contrasenia)
    posee_numero = re.search(r"\d", contrasenia)
    if posee_caracter_especial and posee_numero and len(contrasenia) >= 8:
        diccionario[id]["contrasenia"] = contrasenia
    else:
        print("ATENCIÓN: La contraseña otorgada es inválida. Debe poseer 8 carácteres, conteniendo uno especial y un número.")

def generar_email(nombre: str, apellido: str):
    dominios = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com"]
    email = f"{nombre.lower()}.{apellido.lower()}@{random.choice(dominios)}"
    return email

def actualizar_email(diccionario: dict, id: int, email: str):
    if re.match(r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}", email):
        diccionario[id]["email"] = email
    else:
        print("ATENCIÓN: El email otorgado es inválido. Debe de tener el formato direccion@dominio.com.")

def generar_telefono():
    telefono = f"011-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
    return telefono

def actualizar_telefono(diccionario: dict, id: int, telefono: str):
    if re.match(r"\d{3}-\d{4}-\d{4}", telefono):
        diccionario[id]["telefono"] = telefono