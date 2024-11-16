import random
#inicio la matriz general, para definir luego cualquier tamaño
def inicializar_matriz(filas, columnas, valor_inicial):
    matriz = []
    for i in range(filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]
    return matriz


#imprimo la matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)
    print()

#recorro la matriz y la relleno con caracteres alfanuméricos

def cargar_caracteres(matriz):
    libro = ""
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            libro = random.choices("abcdefghijklmnññopqrstuvwxyz", k = 5)
            matriz[i][j] = libro
    return matriz

#testeo y funciona JOOYAAA  nashe

#inicio_matriz = inicializar_matriz(5, 20, "")
#print(cargar_caracteres(inicio_matriz))