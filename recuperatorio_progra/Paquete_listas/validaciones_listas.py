def validar_lista(lista):
    return lista != []

def lista_creada(lista):
    if validar_lista(lista):
        return True
    else:
        print("\n debe elegir la opción 1 primero.")
        return False
        
def cargo_columna(columna, lista, matrie):
    for i in range(len(lista)):
        matrie[i][columna] = lista[i]
    return matrie

def repetidos(lista):
    final = [0] * 10
    for i in range(len(lista)):
        final[lista[i]] += 1
    return final

def menos_repetido(lista):
    cantidad_minima = float("inf")
    minimo_indice = 0
    resultados = [0] * 2
    
    for i in range(len(lista)):
        if lista[i] < cantidad_minima:
            cantidad_minima = lista[i]
            minimo_indice = i

    resultados[0] = minimo_indice
    resultados[1] = cantidad_minima
    
    return resultados

def mas_repetido(lista):
    cantidad_maxima = float("-inf")
    maximo_indice = 0
    resultado = [0] * 2
    
    for i in range(len(lista)):
        if lista[i] > cantidad_maxima:
            cantidad_maxima = lista[i]
            maximo_indice = i

    resultado[1] = cantidad_maxima
    resultado[0] = maximo_indice
    
    return resultado