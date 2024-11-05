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
        nombre_completo (tuple): Tupla que contiene el nombre y el apellido validados.
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

def crear_persona(diccionario: dict, nombre: str, apellido: str, usuario: str, email: str, telefono: str, contrasenia: str):
    """ La función `crear_persona` añade un nuevo elemento al diccionario solicitado con los datos del nombre y apellido otorgados.

    Args:
        diccionario (dict): Diccionario de personas objetivo
        nombre (str): Nombre de la persona
        apellido (str): Apellido de la persona
    Returns:
        mensaeje_de_situacion (str): Mensaje del resultado del proceso
    """    
    #Cargo los datos, de ser válida, en el diccionario.
    if validar_diccionario_personas(diccionario):
        diccionario[len(diccionario)] = {
            "nombre_completo": (nombre, apellido),
            "usuario": usuario,
            "email": email,
            "telefono": telefono,
            "contrasenia": contrasenia
        }
        mensaeje_de_situacion = "Info: Se ha creado una nueva persona con éxito."
        return mensaeje_de_situacion

def actualizar_persona(diccionario: dict,id_persona: int, nombre: str,apellido: str, usuario: str, email: str, telefono: str, contrasenia: str):
    """ Actualiza el nombre y apellido de la persona con el ID dado en el diccionario.

    Args:
        diccionario (dict): Diccionario objetivo
        id (int): ID de la persona objetivo
        nombre (str): Nombre de la persona
        apellido (str): Apellido de la persona
    Returns:
        mensaeje_de_situacion (str): Mensaje del resultado del proceso
    """    
    if validar_diccionario_personas(diccionario):
        if id_persona not in diccionario:
            mensaeje_de_situacion = f"Error: El ID '{id_persona}' no se encuentra en el diccionario."
            return mensaeje_de_situacion
        else:
            diccionario[id_persona]["nombre_completo"] = (nombre, apellido)
            diccionario[id_persona]["usuario"] = usuario
            diccionario[id_persona]["email"] = email
            diccionario[id_persona]["telefono"] = telefono
            diccionario[id_persona]["contrasenia"] = contrasenia
            mensaeje_de_situacion = "Info: Persona actualizada correctamente"
            return mensaeje_de_situacion

def eliminar_persona(diccionario: dict,id: int):
    """Elimina la persona con el ID dado del diccionario.

    Args:
        diccionario (dict): Diccionario objetivo
        id (int): ID de la persona a eliminar
    Return:
        mensaeje_de_situacion (str): Mensaje del resultado del proceso
    """    
    #Verifico el diccionario y el ID
    if validar_diccionario_personas(diccionario):
        if id in diccionario.keys():
            confirmacion = input(f"Para confirmar la eliminación del la persona cuyo ID es {id}, escriba 'Eliminar': ")
            if confirmacion == "Eliminar" or confirmacion == "eliminar":
                diccionario.pop(id)
                mensaeje_de_situacion = f"Info: Se ha eliminado la persona {id}"
                return mensaeje_de_situacion
            else:
                mensaeje_de_situacion = "Info: No se ha eliminado ninguna persona"
                return mensaeje_de_situacion
        else: 
            mensaeje_de_situacion = f"Error: El ID '{id}' no se encuentra en el diccionario."
            return mensaeje_de_situacion

def generar_usuario(nombre: str, apellido: str, diccionario: dict):
    """
    Genera un nombre de usuario único basado en el nombre y apellido dados, verificando que no exista en el diccionario de personas.

    Args:
        nombre (str): Nombre de la persona
        apellido (str): Apellido de la persona
        diccionario (dict): Diccionario de personas para verificar la unicidad del usuario

    Returns:
        str: Nombre de usuario único generado
    """
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
    
    diccionario[id]["usuario"] = nuevo_usuario
    
    
def generar_contrasenia():
    """
    Genera una contraseña aleatoria de 8 caracteres, compuesta por letras, números y símbolos.

    Returns:
        str: Contraseña generada aleatoriamente
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasenia = "".join(random.choices(caracteres, k=8)) #8 caracteres
    return contrasenia

def validar_contrasenia(contrasenia: str):
    posee_caracter_especial = re.search(r"[!@#$%^&*]" ,contrasenia)
    posee_numero = re.search(r"\d", contrasenia)
    while not posee_caracter_especial and not posee_numero and not len(contrasenia) >= 8:
        print("¡ATENCIÓN!: La contraseña debe poseer al menos un carácter especial, un número y poseer 8 carácteres como mínimo.")
        contrasenia = input("Ingrese una nueva contraseña válida: ")
        posee_caracter_especial = re.search(r"[!@#$%^&*]" ,contrasenia)
        posee_numero = re.search(r"\d", contrasenia)
    return contrasenia

def generar_email(nombre: str, apellido: str):
    """
    Genera una dirección de correo electrónico usando el nombre y apellido dados, seleccionando un dominio aleatorio.

    Args:
        nombre (str): Nombre de la persona
        apellido (str): Apellido de la persona

    Returns:
        str: Dirección de correo electrónico generada
    """
    dominios = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com"]
    email = f"{nombre.lower()}{apellido.lower()}@{random.choice(dominios)}"
    return email

def validar_email(diccionario: dict, email: str):
    for id_persona in diccionario.keys():
        if id_persona == 0:
            continue
        else:
            if diccionario[id_persona]["email"] == email:
                email_preexistente = True
                while email_preexistente:
                    print("Info: El email ingresado ya está vincuado a otro usuario.")
                    email = input("Ingrese otro email: ")
                    if diccionario[id_persona]["email"] != email:
                        email_preexistente = False
    while not re.match(r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}", email):
        print("Info: Email con formato inválido. Por favor, verifique su entrada.")
        email = input("Reingrese el email correctamente: ")
    return email

def generar_telefono():
    """
    Genera un número de teléfono aleatorio con el formato '011-xxxx-xxxx'.

    Returns:
        str: Número de teléfono generado aleatoriamente
    """
    telefono = f"011-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
    return telefono

def validar_telefono(diccionario: dict, telefono: str):
    for id_persona in diccionario.keys():
        if id_persona == 0:
            continue
        else:
            if telefono == diccionario[id_persona]["telefono"]:
                telefono_preexistente = True
                while telefono_preexistente:
                    print("Info: El número de teléfono ingresado ya está asociado a otro usuario.")
                    telefono = input("Por favor, ingrese otro número de teléfono: ")
                    if telefono != diccionario[id_persona]["telefono"]:
                        telefono_preexistente = False
    while not re.match(r"\d{3}-\d{4}-\d{4}", telefono):
        print("Info: Teléfono ingresado con formato inválido. Por favor, verifique su entrada. (###-####-####)")
        telefono = input("Reingrese el teléfono correctamente: ")
    return telefono