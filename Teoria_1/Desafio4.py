# Dado un caracter ingresado por el teclado,
# queremos saber si es comilla o no.

char = input("Ingrese un caracter: ")

if char == "\"" or char == "\'":
    print("El caracter ingresado es comilla")
else:
    print("El caracter ingresado no es comilla")