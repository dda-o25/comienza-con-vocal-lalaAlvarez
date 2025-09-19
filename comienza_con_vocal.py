"""
Larisa Carolina Alvarez Gonzalez 763374
"""

# Entradas
palabra = input("Escribe una palabra: ")


# Proceso
if ord(palabra[0]) in [65, 69, 73, 79, 85]:
    salida = "'" + palabra + "' comienza con vocal"
elif ord(palabra[0]) in [97, 101, 105, 111, 117]:
    salida = "'" + palabra + "' comienza con vocal"
elif ord(palabra[0]) in [225, 233, 237, 243, 250, 252, 220]:
    salida = "'" + palabra + "' comienza con vocal"
elif ord(palabra[0]) in [193, 201, 205, 211, 218]:
    salida = "'" + palabra + "' comienza con vocal"
elif 129 <= ord(palabra[0]) <= 134 or 136 <= ord(palabra[0]) <= 144 or 147 <= ord(palabra[0]) <= 151 or 153 <= ord(palabra[0]) <= 154 or 160 <= ord(palabra[0]) <= 163:
    salida = "'" + palabra + "' comienza con vocal"
elif 181 <= ord(palabra[0]) <= 183 or ord(palabra[0]) in [198, 199] or 210 <= ord(palabra[0]) <= 216 or ord(palabra[0]) == 224 or 226 <= ord(palabra[0]) <= 229 or 233 <= ord(palabra[0]) <= 235:
    salida = "'" + palabra + "' comienza con vocal"
elif 49 <= ord(palabra[0]) <= 57:
    salida = "'" + palabra + "' no comienza con vocal"
else:
    salida = "'" + palabra + "' no comienza con vocal"


# Salidas
print(salida)
