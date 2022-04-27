# Queremos implementar una funcion que dada una cadena de texto, retorne las palabras que
# contiene en orden alfabetico.

def ordeno1(cadena="ss"):
    lista = cadena.split()
    #lista.sort()
    lista.sort(key=str.upper)
    #lista.sort()
    return lista
    
cadena = "Hola que tal como le va"
print(ordeno1(cadena)) 