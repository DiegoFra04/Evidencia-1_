import datetime 

ejemplares={}

while True: 
  opcion=int(input("MENÚ PRINCIPAL\nIngrese un numero de opcion a ejecutar:\n=Opción 1: Registrar un nuevo ejemplar\n=Opción 2: Consultas y reportes de un ejemplar\n=Opción 3: Salir del Programa\n> "))
  if opcion > 3 or opcion < 1:
    print("La opción no es compatible, intente de nuevo")
    continue
  if opcion == 1:
    titulo=input("Ingrese el titulo del nuevo ejemplar:\n> ").upper()

    autor=input(f"Ingrese el nombre del autor del ejemplar {titulo}:\n> ").upper()

    genero=input(f"Ingrese el tipo de género que tiene el ejemplar:\n> ").upper()

    año_publicacion=input(f"Ingrese el año de publicación del ejemplar:\n> ")
    año=año_publicacion

    isbn=input("Ingrese el ISBN del ejemplar:\n> ").upper()

    fecha_adquisicion=input("Ingrese la fecha de adquisición del ejemplar con el siguiente formato(dd/mm/aaaa):\n> ")
    fecha=datetime.datetime.strptime(fecha_adquisicion, '%d/%m/%Y').date()

    clave=max(ejemplares, default=0)+1
    ejemplares[clave]=[titulo, autor, genero, año,isbn, fecha]


  if opcion == 2:
    while True:
      consultas_reportes=int(input("MENÚ DE CONSULTAS Y REPORTES\nSeleccione una de las siguientes opciónes que desee ejecutar:\n=Opción 1: Consultar titulo\n=Opción 2: Reporte\n=Opción 3: Volver al Menú Principal\n> "))
      if consultas_reportes == 1:

          consultas_titulo=int(input("Consultas de Titulo:\n-Opción 1: Consultar por medio de título:\n-Opción 2: Volver al Menú de Consultas y Reportes\n> "))
          if consultas_titulo == 1:
            lista_titulo=[titulo for titulo, autor, genero, año, isbn, fecha in ejemplares.values()]
            print(f"Titulos de ejemplares existentes:")
            print(f"{lista_titulo}")
            consulta_reporte=input("Ingrese el titulo que desee consultar para mostrar sus datos:\n> ").upper()
            for titulo, autor, genero, año, isbn, fecha in ejemplares.values():
              if titulo == consulta_reporte:
                print(f"=Titulo: {titulo}\n=Autor: {autor}\n=Genero: {genero}\n=Año de Publicación: {año}\n=ISBN: {isbn}\n=Fecha: {fecha}")
          if consultas_titulo == 2:
            break
      if consultas_reportes == 2:
        while True:
          reportes=int(input("*MENÚ DE REPORTES*\nSeleccione el tipo de Reporte que desee:\n=Opción 1: Catálogo completo\n=Opción 2: Reporte por Autor\n=Opción 3: Reporte por Género\n=Opción 4: Reporte por Publicación de Año\n=Opción 5: Volver al Menú de Consultas y Reportes\n>"))
          if reportes == 1:
            print(f"="* 30)
            print("*EJEMPLARES*")
            print(f"="* 30)
            for titulo, autor, genero, año, isbn, fecha in ejemplares.values():
              print(f"=Titulo: {titulo}\n=Autor: {autor}\n=Genero: {genero}\n=Año de Publicación: {año}\n=ISBN: {isbn}\n=Fecha: {fecha}")
              print(f"="* 30)
          if reportes == 2:
            lista_autores=[autor for titulo, autor, genero, año, isbn, fecha in ejemplares.values()]
            autores_unicos=set(lista_autores)
            print(f"Autores de ejemplares existentes:")
            print(f"{autores_unicos}")
            consulta_reporte=input("Ingrese el autor que desee consultar para mostrar sus datos:\n> ").upper()
            print(f"="*30)
            print(f"Ejemplares del autor {consulta_reporte}")
            print(f"="*30)
            for titulo, autor, genero, año, isbn, fecha in ejemplares.values():
              if autor == consulta_reporte:
                print(f"=Titulo: {titulo}\n=Autor: {autor}\n=Genero: {genero}\n=Año de Publicación: {año}\n=ISBN: {isbn}\n=Fecha: {fecha}")
                print(f"-"*30)  
          if reportes == 3:
            lista_generos=[genero for titulo, autor, genero, año, isbn, fecha in ejemplares.values()]
            generos_unicos=set(lista_generos)
            print(f"Géneros de ejemplares existentes:")
            print(f"{generos_unicos}")
            consulta_reporte=input("Ingrese el género que desee consultar para mostrar sus datos:\n> ").upper()
            print(f"="*30)
            print(f"Ejemplares del género {consulta_reporte}")
            print(f"="*30)
            for titulo, autor, genero, año, isbn, fecha in ejemplares.values():
              if genero == consulta_reporte:
                print(f"=Titulo: {titulo}\n=Autor: {autor}\n=Genero: {genero}\n=Año de Publicación: {año}\n=ISBN: {isbn}\n=Fecha: {fecha}")
                print(f"-"*30) 
          if reportes == 4:
            lista_años=[año for titulo, autor, genero, año, isbn, fecha in ejemplares.values()]
            años_unicos=set(lista_años)
            print(f"Años de publicación de ejemplares existentes:")
            print(f"{años_unicos}")
            consulta_reporte=input("Ingrese el año de publicación que desee consultar para mostrar sus datos:\n> ").upper()
            print(f"="*40)
            print(f"Ejemplares del año de publicación {consulta_reporte}")
            print(f"="*40)
            for titulo, autor, genero, año, isbn, fecha in ejemplares.values():
              if año == consulta_reporte:
                print(f"=Titulo: {titulo}\n=Autor: {autor}\n=Genero: {genero}\n=Año de Publicación: {año}\n=ISBN: {isbn}\n=Fecha: {fecha}")
                print(f"-"*30) 
          if reportes == 5:
            break
      
      if consultas_reportes == 3:
        break
  if opcion == 3:
    print("---Programa Finalizado, que tenga un lindo día---")
    break1
    