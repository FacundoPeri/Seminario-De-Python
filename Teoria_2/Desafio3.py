# Procesar las notas de los estudiantes de un curso. Queremos saber:
# - Promedio de las notas.
# - Cuantos estudiantes estan por debajo del promedio.

nota = int(input("Ingrese una nota (-1 para finalizar): "))
lista_notas = []
suma_notas = 0

while (nota != -1):
    suma_notas += nota
    lista_notas.append(nota)
    nota = int(input("Ingrese una nota(-1 para finalizar): "))

cant_notas = len(lista_notas)
cant_menor = 0 
promedio = suma_notas / cant_notas

for i in range(cant_notas):
    if lista_notas[i] < promedio:
        cant_menor += 1

print("Lista de notas: ",lista_notas)
print("El promedio de las notas es: ", promedio)
print("La cantidad de alumnos por debajo del promedio es: ", cant_menor)
