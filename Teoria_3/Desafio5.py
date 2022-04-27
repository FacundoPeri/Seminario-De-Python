# Usando expresiones lambda escribir una función que permita codificar una
# frase según el siguiente algoritmo:
# encripto("a") --> "b"
# encripto("ABC") --> "BCD"
# encripto("Rock2021") --> "Spdl3132"

def encripto(c):
    return chr(ord(c) + 1)

frase = input("Ingrese una frase: ")
while (frase != "FIN"):
    # print("".join(list(map(encripto, frase))))
    print("".join(map(lambda c : chr(ord(c) + 1), frase)))
    frase = input("Ingrese una frase: ")