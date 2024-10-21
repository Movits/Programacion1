import personas

#NOTA PARA EL PROFESOR:
#La lógica de una aplicación CRUD está aplicada en su mayoría en las funciones del archivo "personas.py". El archivo "funciones_propias.py" contiene funciones que usé en otras oportuniades, pero creo que son importantes para su inclusión aquí.

print("GENERACIÓN")
print("NOTA: Se genera la tabla de personas con una longitud de 4.")
diccionario = personas.generar_diccionario_personas(4)

for key, valor in diccionario.items():
    if isinstance(valor, dict):
        nombre_completo = " ".join(valor["nombre_completo"])
        print(f"ID: {key}, Nombre Completo: {nombre_completo}, Usuario: {valor['usuario']}, "f"Email: {valor['email']}, Teléfono: {valor['telefono']}, Contraseña: {valor.get('contrasenia')}")
    else:
        print(f"ID: {key}, Tipo: {valor}")
print()


print("CREACIÓN")
print("NOTA: Se crea una persona dando el nombre 'Tiago Nicolaisen'.")
personas.crear_persona(diccionario, "Tiago", "Nicolaisen")

for key, valor in diccionario.items():
    if isinstance(valor, dict):
        nombre_completo = " ".join(valor["nombre_completo"])
        print(f"ID: {key}, Nombre Completo: {nombre_completo}, Usuario: {valor['usuario']}, "f"Email: {valor['email']}, Teléfono: {valor['telefono']}, Contraseña: {valor.get('contrasenia')}")
    else:
        print(f"ID: {key}, Tipo: {valor}")
print()

print("ACTUALIZACIÓN")
print("NOTA: Se cambia el nombre registrado de la persona a 'Silvina Oliva'.")
id_para_actualizar = list(diccionario.keys())[1]
personas.actualizar_persona(diccionario, id_para_actualizar, "Silvina", "Oliva") #id_para_actualizar

for key, valor in diccionario.items():
    if isinstance(valor, dict):
        nombre_completo = " ".join(valor["nombre_completo"])
        print(f"ID: {key}, Nombre Completo: {nombre_completo}, Usuario: {valor['usuario']}, "f"Email: {valor['email']},Teléfono: {valor['telefono']}, Contraseña: {valor.get('contrasenia')}")
    else:
        print(f"ID: {key}, Tipo: {valor}")
print()

print("ACTUALIZACIÓN DE USUARIO")
print("NOTA: De forma intencional se busca cambiar el usuario a 'thor'.")
personas.actualizar_usuario(diccionario, id_para_actualizar, "thor")

for key, valor in diccionario.items():
    if isinstance(valor, dict):
        nombre_completo = " ".join(valor["nombre_completo"])
        print(f"ID: {key}, Nombre Completo: {nombre_completo}, Usuario: {valor['usuario']}, "f"Email: {valor['email']},Teléfono: {valor['telefono']}, Contraseña: {valor.get('contrasenia')}")
    else:
        print(f"ID: {key}, Tipo: {valor}")
print()

print("ACTUALIZACIÓN DE CONTRASEÑA")
print("NOTA: Se actualiza la contrasenia a Uade2024$")
personas.actualizar_contrasenia(diccionario, id_para_actualizar, "Uade2024$")

for key, valor in diccionario.items():
    if isinstance(valor, dict):
        nombre_completo = " ".join(valor["nombre_completo"])
        print(f"ID: {key}, Nombre Completo: {nombre_completo}, Usuario: {valor['usuario']}, "
            f"Email: {valor['email']}, Teléfono: {valor['telefono']}, Contraseña: {valor.get('contrasenia')}")
    else:
        print(f"ID: {key}, Tipo: {valor}")
print() 

print("ACTUALIZACIÓN DE EMAIL")
print("NOTA: Se actualiza el email a 'joseDeSanMartin78@liberador.com.ar'")
personas.actualizar_email(diccionario, id_para_actualizar, "joseDeSanMartin78@liberador.com.ar")

for key, valor in diccionario.items():
    if isinstance(valor, dict):
        nombre_completo = " ".join(valor["nombre_completo"])
        print(f"ID: {key}, Nombre Completo: {nombre_completo}, Usuario: {valor['usuario']}, "
            f"Email: {valor['email']}, Teléfono: {valor['telefono']}, Contraseña: {valor.get('contrasenia')}")
    else:
        print(f"ID: {key}, Tipo: {valor}")
print()

print("ACTUALIZACIÓN DE TELÉFONO")
print("NOTA: Se actualiza el telefono a '011-4321-9876'")
personas.actualizar_telefono(diccionario, id_para_actualizar, "011-4321-9876")

for key, valor in diccionario.items():
    if isinstance(valor, dict):
        nombre_completo = " ".join(valor["nombre_completo"])
        print(f"ID: {key}, Nombre Completo: {nombre_completo}, Usuario: {valor['usuario']}, "
            f"Email: {valor['email']}, Teléfono: {valor['telefono']}, Contraseña: {valor.get('contrasenia')}")
    else:
        print(f"ID: {key}, Tipo: {valor}")
print()

print("ELIMINACIÓN")
id_para_eliminar = list(diccionario.keys())[1]
personas.eliminar_persona(diccionario, id_para_eliminar)

for key, valor in diccionario.items():
    if isinstance(valor, dict):
        nombre_completo = " ".join(valor["nombre_completo"])
        print(f"ID: {key}, Nombre Completo: {nombre_completo}, Usuario: {valor['usuario']}, "
            f"Email: {valor['email']}, Teléfono: {valor['telefono']}")
    else:
        print(f"ID: {key}, Tipo: {valor}")
print()


print("VERIFICACIÓN DEL COMPORTAMIENTO DEL ID POS ELIMINACIÓN")
personas.crear_persona(diccionario, "Diego", "Nicolaisen")

for key, valor in diccionario.items():
    if isinstance(valor, dict):
        nombre_completo = " ".join(valor["nombre_completo"])
        print(f"ID: {key}, Nombre Completo: {nombre_completo}, Usuario: {valor['usuario']}, "
            f"Email: {valor['email']}, Teléfono: {valor['telefono']}")
    else:
        print(f"ID: {key}, Tipo: {valor}")
print()