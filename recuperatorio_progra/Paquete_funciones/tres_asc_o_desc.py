def ordenar_lista(lista, eleccion = "ASC"): #si el user no elige, ya de prepo es asc
    if eleccion == "ASC":
        for i in range(len(lista)):
            for x in range(0, len(lista)- i - 1):
                if lista[x] > lista[x + 1]:
                    pa = lista[x]
                    lista[x] = lista[x+ 1]
                    lista[x + 1] = pa
        return lista
    elif eleccion == "DESC":
        for i in range(len(lista)):
            for x in range(0, len(lista)- i - 1):
                if lista[x] < lista[x + 1]:
                    pa = lista[x]
                    lista[x] = lista[x+ 1]
                    lista[x + 1] = pa
        return lista