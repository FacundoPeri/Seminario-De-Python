# Queremos escribir una funcion que imprima sus argumentos agregando de
# que tipo son.

def imprimo(*args):
    for i in range(len(args)):
        print(f"{args[i]} es de tipo {type(args[i])}")

num = 4
str = "prueba"
list = ["prueba2",3]
tupl = (1,2)

imprimo(num,str,list,tupl)
