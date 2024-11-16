def validacion_de_numero(numero, minimo, maximo):
    try:
        if minimo <= numero <= maximo:
            return numero
        
    except ValueError:
        return None
    
def validacion_largo(str, largo):
    try: 
        if len(str) <= largo:
            return str
    except ValueError:
        return None