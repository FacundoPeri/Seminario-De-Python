# INgresar las notas / Calcular promedio / Calcular cuantos tienen
# notas menores al promedio.
# Escribir dicho programa utilizando funciones.

def cargar_dicci():
    nombre  = input("Ingresar el nombre de un alumno: ")
    dicci = {}
    while nombre != "FIN":
        nota = int(input(f"Ingrese la nota del alumno {nombre}: "))
        dicci[nombre] = nota
        nombre = input("Ingrese el nombre de otro alumno: ")
    return dicci

def calcular_prom(diccionario):
    total_notas = 0
    for elem in diccionario:
        total_notas += diccionario[elem]
    promedio = total_notas / len(diccionario)
    return promedio

def bajo_promedio(diccionario,promedio):
    cant_debajo = 0
    for elem in diccionario:
        if diccionario[elem] < promedio:
            cant_debajo += 1
    return cant_debajo

dicci = cargar_dicci()
promedio = calcular_prom(dicci)
cant = bajo_promedio(dicci,promedio)

print(f"Promedio de notas de los alumnos: {promedio}")
print(f"La cantida de alumnos por debajo del promedio es: {cant}")

