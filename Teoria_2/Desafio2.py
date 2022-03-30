# Ingresar palabras desde teclado hasta ingresar la palabra FIN.
# Imprimir aquellas que empiecen y terminen con la misma letra.

cadena = input("Ingrese una palabra: ")

while cadena != "FIN":
    if cadena[0] == cadena[-1]:
        print(cadena)
    cadena = input("Ingrese una palabra: ")