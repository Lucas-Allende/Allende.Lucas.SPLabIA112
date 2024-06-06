from funciones_movies import *
import json





archivo_csv = "movies.csv"
archivo_cargado = 0


while True:
    match menu():
        case "1":
            lista_csv = cargar_csv(archivo_csv)
            archivo_cargado = 1
            print("Archivo cargado con exito ")
        case "2":
            if archivo_cargado == 0:
                print("Primero debemos cargar el archivo ")
            else:
                for pelicula in lista_csv:
                    print(pelicula)
        case "3":
            if archivo_cargado == 0:
                print("Primero debemos cargar el archivo ")
            else:
                lista_con_ratings = asignar_ratings(lista_csv)
                print("Los ratings se cargaron con exito")            
        case "4":
            if archivo_cargado == 0:
                print("Primero debemos cargar el archivo ")
            else:
                lista_con_generos = asignar_genero(lista_csv)
                print("Los generos se cargaron con exito")
        case "5":
            if archivo_cargado == 0:
                print("Primero debemos cargar el archivo ")
            else:
                genero_elegido = input("Ingrese género: ")
                try:
                    peliculas_filtradas = filtrar_peliculas_genero(lista_csv, genero_elegido)
                except ValueError:
                    print(f"El género '{genero_elegido}' no existe en la lista de películas.")
                with open(get_path_actual("genero.csv"), "w", encoding="utf-8") as archivos:
                    encabezado = ",".join(list(peliculas_filtradas[0].keys())) + "\n"
                    archivos.write(encabezado)
                    for pelicula in peliculas_filtradas:
                        values = list(pelicula.values())
                        l = []
                        for value in values:
                            if isinstance(value, int):
                                l.append(str(value))
                            elif isinstance(value, float):
                                l.append(str(value))
                            else:
                                l.append(value)
                        linea = ",".join(l) + "\n"
                        archivos.write(linea)
                    print(f"Archivo con películas del género {genero_elegido} guardado con éxito")
        case "6":
            if archivo_cargado == 0:
                print("Primero debemos cargar el archivo ")
            else:
                ordenar_peliculas_genero_rating(lista_csv, "genero", "rating")
                for pelicula in lista_csv:
                    print(pelicula)
        case "7":
            if archivo_cargado == 0:
                print("Primero debemos cargar el archivo ")
            else:
                buscar_mejor_rating(lista_csv)                                                                                                                                                                      
        case "8":
            with open(get_path_actual("peliculas_ordenadas.json"), "w", encoding="utf-8") as archivo:
                json.dump(lista_csv, archivo, indent=4)
                print("Archivo con las peliculas ordenadas guardado con éxito") 
        case "9":
            break
    pausar()

print("fin del programa")