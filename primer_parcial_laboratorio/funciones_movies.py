"""
Se dispone de un archivo con datos acerca de películas, que tiene el siguiente formato:
id_peli, titulo, genero, rating

1) Cargar archivo .CSV: Se pedirá el nombre del archivo y se cargará en una lista de
diccionarios los elementos
del mismo.
2) Imprimir lista: Se imprimirá por pantalla la tabla con los datos de las películas.
3) Asignar rating: Se deberá hacer uso de la función map. La cual recibirá la lista y una
función que asignará a la película un valor de rating flotante entre 1 y 10 con 1 decimal
calculado de manera aleatoria se mostrará por pantalla el mismo.
4) Asignar género: Se deberá hacer uso de la función map. La cual recibirá la lista y una
función que asignará a la película un género de acuerdo a un número aleatorio entre 1 y 4.
1: drama
2: comedia
3: acción
4: terror
5) Filtrar por género: Se deberá pedir un género y escribir un archivo igual al original, pero
donde solo
aparezcan películas del género seleccionado. El nombre del archivo será p.e. comedias.csv
6) Ordenar películas: Se deberá mostrar por pantalla un listado de las películas ordenadas por
género y dentro de las del mismo género que aparezcan ordenadas por rating descendente.
7) Informar Mejor Rating: Mostrar el titulo y el rating de la película con más rating
8) Guardar películas: Se deberá guardar el listado del punto anterior en un archivo JSON.
9) Salir.

"""

import random

"""
Funcion para limpiar la pantalla
"""
def limpiarPantalla():
    import os
    os.system("cls")

    """Funcion que pausa el programa hasta que el usuario presione una tecla
    """
def pausar():
    import os
    os.system("pause")

def menu()->str:
    """Funcion que muestra un menu de opciones y pide la opcion a ingresar al usuario

    Returns:
        str: retorna la opcion elegida por el usuario
    """
    limpiarPantalla()
    print(f"{'\n Menu de opciones' :^50s}")
    print("1-Cargar archivo ")
    print("2-Imprimir lista ")
    print("3-Asignar rating ")
    print("4-Asignar genero ")
    print("5-Filtrar por genero ")
    print("6-Ordenar peliculas ")
    print("7-Informar mejor rating ")
    print("8-Guardar peliculas ")
    print("9-Salir ")

    return input("Ingrese opcion: ")


def get_path_actual(nombre_archivo):
    """funcion que devuelve la ruta en la que se encuentra el archivo que vamos a abrir

    Args:
        nombre_archivo (_type_): nombre del archivo a abrir

    Returns:
        _type_: retorna la ruta completa en la que se encuentra el archivo
    """
    import os
    directorio_actual = os.path.dirname(__file__)

    return os.path.join(directorio_actual, nombre_archivo)


def cargar_csv(archivo_csv):
    """Funcion que utiliza un archivo de formato csv y lo convierte en diccionario

    Args:
        archivo_csv (_type_): nombre del archivo a utilizar

    Returns:
        _type_: retorna la lista de diccionarios
    """
    lista = []
    with open(get_path_actual(archivo_csv), "r" , encoding="utf-8") as archivo:  
        encabezado = archivo.readline().strip("\n").split(",")
        for linea in archivo.readlines():
            pelicula = {}
            linea = linea.strip("\n").split(",")
            id, titulo, genero, rating = linea
            pelicula["id"] = int(id)
            pelicula["titulo"] = titulo
            pelicula["genero"] = genero
            pelicula["rating"] = float(rating)
            lista.append(pelicula)

    return lista


def asignar_ratings(lista: list):
    """funcion que recorre la lista y asigna un rating random entre 1 y 10 con un decimal

    Args:
        lista (list): lista de peliculas

    Returns:
        _type_: retorna la lista de peliculas con los ratings asignados
    """
    for pelicula in lista:
        pelicula["rating"] = round(random.uniform(1, 10), 1)

    return lista


def asignar_genero(lista: list):
    """recorre la lista y asigna un genero random entre drama, accion, comedia y terror

    Args:
        lista (list): lista de peliculas

    Returns:
        _type_: retorna la lista de peliculas con un genero asignado
    """

    for pelicula in lista:
        generos = ["drama", "comedia", "acción", "terror"]
        pelicula["genero"] = random.choice(generos)

    return lista

def filtrar_peliculas_genero(lista:list, genero:str)->list:
    """filtra la lista de peliculas con las peliculas elegidas por el usuario

    Args:
        lista (list): lista de peliculas
        genero (str): genero ingresado por el usuario

    Returns:
        list: retorna la lista filtrada con el genero elegido
    """
    lista_filtrada = []
    for el in lista:
        if el["genero"] == genero:
            lista_filtrada.append(el)

    return lista_filtrada

def swap_lista(lista: list, i:int, j:int)->None:
    """funcion para ordenar

    Args:
        lista (list): _description_
        i (int): _description_
        j (int): _description_
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

def ordenar_peliculas_genero_rating(peliculas:list, campo_uno:str, campo_dos:str, asc:bool = True):
    """Ordena las peliculas por genero y a las del mismo genero por rating de manera descendente

    Args:
        peliculas (list): lista de peliculas
        campo_uno (str): primer campo de ordenamiento
        campo_dos (str): segundo campo de ordenamiento
        asc (bool, optional): segun True o False ordena de forma descendente o ascendente. Defaults to True.
    """
    tam = len(peliculas)
    for i in range(tam-1):
        for j in range(i+1, tam):
            if peliculas[i][campo_uno] == peliculas[j][campo_uno]:
                if peliculas[i][campo_dos] < peliculas[j][campo_dos] if asc else peliculas[i][campo_dos] > peliculas[j][campo_dos]:
                    swap_lista(peliculas, i, j)
            else:
                if peliculas[i][campo_uno] < peliculas[j][campo_uno] if asc else peliculas[i][campo_uno] > peliculas[j][campo_uno]:
                    swap_lista(peliculas, i, j)


def buscar_mejor_rating(lista):
    """Recorre la lista de peliculas y busca la pelicula con el mejor rating y printea un mensaje con su titulo y puntaje

    Args:
        lista (_type_): lista de peliculas
    """
    mejor_pelicula = ""
    mejor_rating = 0

    for pelicula in lista:
        if pelicula["rating"] > mejor_rating:
            mejor_rating = pelicula["rating"]
            mejor_pelicula = pelicula["titulo"]

    print(f"La pelicula con el mejor rating es {mejor_pelicula} con un puntaje de {mejor_rating}")

