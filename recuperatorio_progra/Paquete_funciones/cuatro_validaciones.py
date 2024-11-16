def valido_alfabetica(palabrita):
    return not no_debe_tener_int(palabrita) and tiene_str(palabrita)

def tiene_str(palabrita):
    flag = False
    for i in range(len(palabrita)):
        if palabrita[i].isalpha():
            flag = True
    return flag

def no_debe_tener_int(palabrita):
    flag = False
    for i in range(len(palabrita)):
        if palabrita[i].isnumeric():
            flag = True
    return flag