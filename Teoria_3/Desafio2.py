def imprimo_muchos_valores(mensaje_inicial, *en_otro_idioma, **en_detalle):
    print("Mensaje original")
    print(mensaje_inicial)
    print("\nEn otros idiomas")
    print("-" * 40)
    for val in en_otro_idioma:
        print(val)
    print("\nEn detalle")
    print("-" * 40)
    for clave in en_detalle:
        print(f"{clave}: {en_detalle[clave]}")
    print("\nFuente: traductor de Google. ")

imprimo_muchos_valores("Hola","Hello", "Hallo", "Aloha ", "Witam", "Kia ora",
Ingles= "Hello",
Aleman="Hallo",
Hawaiano="Aloha",
Polaco="Witam",
Maori="Kia ora")
