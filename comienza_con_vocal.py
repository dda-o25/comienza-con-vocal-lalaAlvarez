"""
Larisa Carolina Alvarez Gonzalez 763374

"""


# Entradas

palabra = input("Escribe una palabra: ")


# Proceso


#mayusculas
if ord(palabra[0]) == 65 or ord(palabra[0]) == 69 or ord(palabra[0]) == 73 or  ord(palabra[0]) == 79 or ord(palabra[0]) == 85:
    salida = "'" + palabra + "' comienza con vocal"
# minusculas
elif  ord(palabra[0]) == 97 or ord(palabra[0]) == 101 or ord(palabra[0]) == 105 or ord(palabra[0]) == 111 or ord(palabra[0]) == 117:
    salida = "'" + palabra + "' comienza con vocal"
# caracteres raros
elif ord(palabra[0]) >= 129 and ord(palabra[0]) <=134 or ord(palabra[0]) >= 136 and ord(palabra[0]) <=144:
        salida = "'" + palabra + "' comienza con vocal"
elif ord(palabra[0]) >= 147 and ord(palabra[0]) <= 151 or ord(palabra[0]) >= 153 and ord(palabra[0]) <= 154 or ord(palabra[0]) >= 160 and ord(palabra[0]) <= 163:
    salida = "'" + palabra + "' comienza con vocal"
#mayus raras
elif ord(palabra[0]) >= 181 and ord(palabra[0]) <= 183 or ord(palabra[0]) == 198 or ord(palabra[0]) == 199:
    salida = "'" + palabra + "' comienza con vocal"
elif ord(palabra[0]) >= 210 and ord(palabra[0]) <= 216 or ord(palabra[0]) == 224:
    salida = "'" + palabra + "' comienza con vocal"
elif ord(palabra[0]) >= 226 and ord(palabra[0]) <= 229:
    salida = "'" + palabra + "' comienza con vocal"
elif ord(palabra[0]) >= 233 and ord(palabra[0]) <= 235:
    salida = "'" + palabra + "' comienza con vocal"
elif ord(palabra[0]) >= 49 and ord(palabra[0]) <= 57:
    salida = "'" + palabra + "' no comienza con vocal"
else:
    salida = "'" + palabra + "' no comienza con vocal"

# Salidas
print(ord(palabra[0]))
print(salida)
