# Escribir un programa que ingrese 4 palabras desde el teclado
# e imprima aquellas que contienen la letra r.

for i in range(4):
    cadena = input("Ingresa una palabra: ")
    if "r" in cadena:
        print(f"{cadena} tiene una letra r")