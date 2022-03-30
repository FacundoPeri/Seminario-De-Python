# Vamos a modificar Desafio1.py para que se impima "TIENE R" si la palabra
# contiene r y sino, imprima "NO TIENE R".

for i in range(4):
    cadena = input("Ingrese una palabra: ")
    if "r" in cadena:
        print("TIENE R")
    else:
        print("NO TIENE R")