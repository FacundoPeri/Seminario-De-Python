# Dada una letra ingresada por el teclado,
# queremos saber si es mayuscula o minuscula

char = input("Ingrese una letra: ")

if char >= "a" and char <= "z":
    print("La letra ingresada es minuscula")
elif char >= "A" and char <= "Z":
    print("La letra ingresada es Mayuscula")
else:
    print("No ingresaste una letra")
