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
