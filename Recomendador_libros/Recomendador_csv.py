import csv

lista_csv = []
with open('libros.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
    lista_csv.append(Libro(row[0], row[1], row[2], float(row[3])))


accion = ''
while not accion in ('a', 'b', 'r', 's'):
    accion = input('''Seleccione la accion deseada
Agregar libro (a), buscar por genero (b), recibir recomendacion (r), salir (s): ''').lower()

    match accion:
        case 'a':
            titulo = input('Ingrese el titulo del libro: ')
            autor = input('Ingrese el autor del libro: ')
            genero = input('Ingrese el genero del libro: ')
            puntuacion = ''
            while not puntuacion.replace('.','',1).isnumeric():
                puntuacion = input('Ingrese la puntuacion del libro: ')
            puntuacion = float(puntuacion)
            lista_csv.append(Libro(titulo, autor, genero, puntuacion))
            print('Libro agregado correctamente\n')
            accion = ''

        case 'b':
            genero = input('Ingrese el genero del libro: ')
            print(f'Libros en el genero {genero}:')
            for libro in lista_csv:
                if libro.genero == genero:
                print(f'{libro.titulo}')
                print('\n')
                accion = ''

        case 'r':
            genero = input('Ingrese el genero de interes: ')
            libros_genero = [libro for libro in lista_csv if libro.genero == genero]
            if libros_genero:
                libro_mas_popular = max(libros_genero, key=lambda x: x.puntuacion)
                print(f'El libro mas popular en el genero {genero} es {libro_mas_popular.titulo} con una puntuacion de {libro_mas_popular.puntuacion}\n')
                accion = ''
            else:
                print(f'No hay libros en el genero {genero}\n')
                accion = ''

        case 's':
            print('Saliendo del programa...')
            break