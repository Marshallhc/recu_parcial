import random
def lista_aleatoria():
    lista = [0] * 100
    for i in range(len(lista)):
        lista[i] = random.randint(0, 9)
    return lista