from Paquete_funciones import *
from Paquete_matriz import *
from Paquete_inputs import *
from Paquete_listas import *
def biblioteca():
    biblio = inicializar_matriz(5,20,"")
    cargar_caracteres(biblio)
def menu():
    lista = []  #esto por si eligen la opción opciones antes de formar la 1.🙄
    lista_posible = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        opcion_user = get_int("\n 1. generar lista de números aleatorios \n 2. ordenamiento de la lista de la anterior opción. \n 3. cuántas veces se repite cada número del 0 al 9 \n 4. muestra los números que más se repiten y los que menos se repiten. \n 5. generar matriz aleatoria de caracteres alfabéticos. \n 6. ingresar palabra. \n 7. SALIR:\n ", "probá de nuevo pa, tu opción no está dentro de los rangos", 1, 7, 5467)
        match opcion_user:
            case 1:
                lista = lista_aleatoria()
                print(f"{lista}")
            case 2:
                if validar_lista(lista):
                    eleccion = get_str("ingrese [ASC] (para ordenar la lista de forma ascendente) o [DESC] (para ordenar la lista de froma descendente): ", "OPCIÓN NO EXISTENTE, PORFAVOR ELIJA BIEN", 4).upper()
                    print(f"está en {eleccion}, y queda: {ordenar_lista(lista, eleccion)}")
            case 3:
                if lista_creada(lista):
                    print("NÚMERO | CANTIDAD")
                    numeros_cantidad = inicializar_matriz(10, 2, 0)
                    cargo_columna(0, lista_posible, numeros_cantidad)
                    cargo_columna(1, repetidos(lista), numeros_cantidad)
                    imprimir_matriz(numeros_cantidad)
                    print()
            case 4:
                if lista_creada(lista):
                    print(f"el más repetido es {mas_repetido(numeros_cantidad(lista))[0]}.\n cantidad: {mas_repetido(numeros_cantidad(lista))[1]}\n el menos repetido fué: {menos_repetido(numeros_cantidad(lista))[0]}\n cantidad: {menos_repetido(numeros_cantidad(lista))[1]}")
            case 5:
                imprimir_matriz(biblioteca())
            case 6:
                palabra = get_str("ingrese una palabra u oración yqc: ", "RANGO EXCEDIDO", 34235645)
                if valido_alfabetica():
                    print(f"fué cargado exitosamente {palabra}")
                else:
                    print("ERROR: NO DEBE TENER MENSAJES NUMÉRICOS")
            case 7:
                break
            
menu()