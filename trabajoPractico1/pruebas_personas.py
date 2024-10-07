import personas

#NOTA PARA EL PROFESOR:
#La lógica de una aplicación CRUD está aplicada en su mayoría en las funciones del archivo "personas.py". El archivo "funciones_propias.py" contiene funciones que usé en otras oportuniades, pero creo que son importantes para su inclusión aquí.

diccionario = personas.generar_diccionario_personas(4)

print("GENERACIÓN")
for key, valor in diccionario.items():
    print(f"{key}, {valor}")
print()

personas.crear_persona(diccionario, "Tiago", "Nicolaisen")

print("CREACIÓN")
for key, valor in diccionario.items():
    print(f"{key}, {valor}")
print()

personas.actualizar_persona(diccionario, 15, "Silvina", "Oliva")

print("ACTUALIZACIÓN")
for key, valor in diccionario.items():
    print(f"{key}, {valor}")
print()

personas.eliminar_persona(diccionario,1)

print("ELIMINACIÓN")
for key, valor in diccionario.items():
    print(f"{key}, {valor}")
print()

personas.crear_persona(diccionario, "Diego", "Nicolaisen")

print("VERIFICACIÓN DEL COMPORTAMIENTO DEL ID POS ELIMINACIÓN")
for key, valor in diccionario.items():
    print(f"{key}, {valor}")
print()