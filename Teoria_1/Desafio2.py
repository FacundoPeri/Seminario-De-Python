# Queremos ingresar un numero desde el teclado e
# imprimir si es multiplo de 2,3 o 5.

num = int(input(" Ingrese un numero: "))

if num % 2 == 0:
    print("--- El numero ingresado es multiplo de 2 ---")
elif num % 3 == 0:
    print("--- El numero ingresado es multiplo de 3 ---")
elif num % 5 == 0:
    print("--- El numero ingresado es multiplo de 5 ---")
else:
    print("--- El numero ingresado no es multiplo de 2,3 ni 5 ---")