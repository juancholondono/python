# recorer tupla
# Definicion de la tupla

tupla = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
# Definicion de la funcion
def recorrer_tupla(t):
    """
    Recorrer una tupla de tuplas y mostrar los elementos en forma de tabla.
    """
    for i in range(len(t)):
        for j in range(len(t[i])):
            print(t[i][j], end="\t")
        print()
# Llamada a la funcion
recorrer_tupla(tupla)
