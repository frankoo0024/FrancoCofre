def menu_principal():
    print("1.- Cupos por género")
    print("2.- Búsqueda de películas por rango de precio")
    print("3.- Actualizar precio de película")
    print("4.- Agregar película")
    print("5.- Eliminar película")
    print("6.- Salir")

peliculas = {
    ´P101´:[´Luz De Otoño´, ´drama´,110, ´B´,´español´, False],
    ´P102´:[´Noche de Neón´, ´Acción´125, ´C´, ´ingles´,True],
    ´P103´:[´Planeta agua´,´Documental´,90, ´A´, ´español´,False],
    ´P104´:[´Risa total´, ´comedia´,105, ´A´,´´español, True],
    ´P105´:[´Codigo cero´, ´thiller´, ´118´, ´C´, ´Ingles´, False],
            
    }
def opcion_1():
    print("Ingrese el genero a consultar()")
