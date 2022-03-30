# Necesitamos procesar las notas de los estudiantes de este curso.
# Queremos saber:
# Cual es el promedio de las notas.
# Que estudiantes estan por debajo del promedio.

nombre =  input("Ingrese el nombre del alunon (!= FIN): ")
dicci = {}
suma_notas = 0

while (nombre != "FIN"):
    nota = int(input(f"Ingrese la nota de {nombre}: "))
    dicci[nombre] = nota
    suma_notas += nota
    nombre = input("Ingrese el nombre de otro alumno (!=FIN): ")

cant_notas = len(dicci)
promedio = suma_notas / cant_notas

for elem in dicci:
    if (dicci[elem] < promedio):
        valor = dicci[elem]
        print(f"El alumno {elem} tiene una nota {valor} y esta por debajo del promedio.")

print(dicci) 
