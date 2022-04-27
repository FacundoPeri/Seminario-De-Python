# Queremos implementar una función que dada una colección con datos de usuarios de un
# determinado juego (por ejemplo nombre, nivel y puntaje), queremos retornar esta colección
# ordenada de acuerdo al nombre.


def ordenar(usuarios):
    return sorted(usuarios, key=lambda usuarios : usuarios[0])


usuarios = []
nombre = input("Ingrese el nombre del usuario: ")

while (nombre != "FIN"):
    nivel  = int(input("Ingrese el nivel del usuario: "))
    puntaje = float(input("Ingrese el puntaje del usuario: "))
    usuarios.append((nombre,nivel,puntaje))
    nombre = input("\nIngrese el nombre del usuario: ")

print(usuarios)

print(ordenar(usuarios))
