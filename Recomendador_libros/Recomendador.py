import csv

class Libro:
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion

lista_libros = []

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 4.5)

libro2 = Libro("1984", "George Orwell", "Ciencia Ficción", 4.3)

libro3 = Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", 4.7)

libro4 = Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2)

libro5 = Libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clásico", 4.4)

libro6 = Libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1)

libro7 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", 4.6)

libro8 = Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía", 4.8)

libro9 = Libro("Los Pilares de la Tierra", "Ken Follett", "Histórica", 4.4)

libro10 = Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasía", 4.0)


lista_libros = [libro1, libro2, libro3, libro4, libro5, libro6, libro7, libro8, libro9, libro10]


with open('libros.csv', 'w', newline='', encoding='utf-8') as f:
    escritor = csv.writer(f)
    for libro in lista_libros:
        escritor.writerow([libro.titulo, libro.autor, libro.genero, libro.puntuacion])

    
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
            lista_libros.append(Libro(titulo, autor, genero, puntuacion))
            print('Libro agregado correctamente\n')
            accion = ''

        case 'b':
            genero = input('Ingrese el genero del libro: ')
            print(f'Libros en el genero {genero}:')
            for libro in lista_libros:
                if libro.genero == genero:
                    print(f'{libro.titulo}')
                    print('\n')
                    accion = ''

        case 'r':
            genero = input('Ingrese el genero de interes: ')
            libros_genero = [libro for libro in lista_libros if libro.genero == genero]
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