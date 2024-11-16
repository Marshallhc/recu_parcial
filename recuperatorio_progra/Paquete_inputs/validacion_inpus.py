from .validaciones import validacion_de_numero, validacion_largo
def get_int(mensaje:str, mensaje_de_error:str, mini:int, maxi:int, reintentos:int):
    for i in range(reintentos):
        user_inpus = int(input(mensaje))
        numero = validacion_de_numero(user_inpus, mini, maxi)
        if numero is not None:
            return numero
        else:
            print(mensaje_de_error)
    return None

def get_str(mensaje:str, mensaje_error, largos:int):
    user_inpus = str(input(mensaje))
    cadena = validacion_largo(user_inpus, largos)
    if cadena is not None:
        return cadena
    else:
        print(mensaje_error)
    return None
