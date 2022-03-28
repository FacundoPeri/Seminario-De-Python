# Dadas dos cadenas ingresadas desde el teclado,
# imprimir aquella que tenga mas caracteres.

cadena_1 = input("Ingrese la primer cadena: ")
cadena_2 = input("Ingrese la segunda cadena: ")

if len(cadena_1) > len(cadena_2):
    print(cadena_1)
elif len(cadena_1) == len(cadena_2):
    print("Las dos cadenas tienen la misma longitud.")
else:
    print(cadena_2)