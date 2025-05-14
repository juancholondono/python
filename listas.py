## recorrer listas 

listas = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
def recorrer_vistas(l):
    """
    Recorrer una lista de listas y mostrar los elementos en forma de tabla.
    """
    for i in range(len(l)):
     for j in range(len(l[i])):
            print(l[i][j], end="\t")
    print()
recorrer_vistas(listas)


dicionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
def recorrer_diccionario(d):
    """
    Recorrer un diccionario y mostrar las claves y valores.
    """
    for clave, valor in d.items():
        print(f"{clave}: {valor}")
recorrer_diccionario(dicionario)

tupla = (1, 2, 3, 4, 5)
def recorrer_tupla(t):
    """
    Recorrer una tupla y mostrar los elementos.
    """
    for i in t:
        print(i, end="\t")
    print()
recorrer_tupla(tupla)
