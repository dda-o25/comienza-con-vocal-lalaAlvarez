"""
Inserta el encabezado aquí y escribe tu código abajo
"""


# Entradas
palabra = input("Escribe una palabra: ")


# Proceso

if ord(palabra[0]) == 65 or ord(palabra[0]) == 69 or ord(palabra[0]) == 73 or  ord(palabra[0]) == 79 or ord(palabra[0]) == 85:
    salida = "'" + palabra + "' comienza con vocal"
elif ord(palabra[0]) == 181 or ord(palabra[0]) == 144 or ord(palabra[0]) == 214 or ord(palabra[0]) ==224 or ord(palabra[0]) == 233:
    salida = "'" + palabra + "' comienza con vocal"
elif ord(palabra[0]) == 97 or ord(palabra[0]) == 111 or ord(palabra[0]) == 101 or ord(palabra[0]) == 105 or ord(palabra[0]) == 117:
        salida = "'" + palabra + "' comienza con vocal"
else:
    salida = "'" + palabra + "' no comienza con vocal"

# Salidas
print(salida)
