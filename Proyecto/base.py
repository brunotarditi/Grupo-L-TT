import sqlite3

#Crear conexión
#conexion = sqlite3.connect("mibase.db")


#Crear puntero
#cursor = conexion.cursor()


#Se crea una tabla de categorias para mi base de datos

"""cursor.execute('''
CREATE TABLE CATEGORIAS(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
NOMBRE TEXT NOT NULL)''')"""


"""categorias = [
    (1, "Electro"),
    (2, "Hogar y textil"),
    (3, "Tiempo Libre"),
    (4,	"Bebés y Niños"),
    (5,	"Almacén"),
    (6,	"Bebidas"),
    (7,	"Frutas y Verduras"),
    (8,	"Carnes"),
    (9, "Pescados y Mariscos"),
    (10, "Quesos y Fiambres"),
    (11, "Lácteos"),
    (12, "Congelados"),
    (13, "Panadería y Repostería"),
    (14, "Perfumería"),
    (15, "Limpieza"),
    (16, "Mascotas") ]"""

#Inserto datos a la tabla categorias
#cursor.executemany("INSERT INTO CATEGORIAS VALUES (?, ?)", categorias)

#Crear una tabla de productos para mi base de datos

"""cursor.execute('''
CREATE TABLE PRODUCTOS(
"Nombre" TEXT NOT NULL,
"IdCategoria" INTEGER NOT NULL,
FOREIGN KEY("IdCategoria") REFERENCES "CATEGORIAS"("ID"))''')"""

"""productos = [

("Aire Acondicionado", 1),
("Ventilador", 1),
("Equipo de Audio", 1),
("Calefón",	1),
("Caloventor", 1),
("Estufa", 1),
("Microondas", 1),
("Horno", 1),
("Anafe", 1),
("Consola de Video Juegos", 1),
("Heladera", 1),
("Freezer", 1),
("Mouse", 1),
("Teclado", 1),
("Impresora", 1),
("PC Escritorio", 1),
("Notebook", 1),
("Tablet", 1),
("Celular", 1),
("Teléfono Fijo", 1),
("TV", 1),
("DVD", 1),
("Blu Ray", 1),
("Lavarropas", 1),
("Secarropas", 1),
("Pava Eléctica", 1),
("Cafetera", 1),
("Licuadora", 1),
("Plancha", 1),
("Batidora", 1),
("Toalla", 2),
("Toallón", 2),
("Repasador", 2),
("Delantal", 2),
("Colchón", 2),
("Almohada", 2),
("Alfombra", 2),
("Mantel", 2),
("Acolchado", 2),
("Frazada", 2),
("Sábanas", 2),
("Cubiertos", 2),
("Vaso", 2),
("Taza", 2),
("Mesa", 2),
("Silla", 2),
("Tablón", 2),
("Caballetes", 2),
("Mesa de Luz", 2),
("Lámpara", 2),
("Ténder", 2),
("Tabla de Planchar", 2),
("Cesto de Basura", 2),
("Contina de Baño", 2),
("Jabonera", 2),
("Bicicleta", 3),
("Corta Cesped", 3),
("Parrilla", 3),
("Reposera", 3),
("Sombrilla", 3),
("Gacebo", 3),
("Libro", 3),
("Cuaderno", 3),
("Resma", 3),
("Cartuchera", 3),
("Carpeta", 3),
("Tijera", 3),
("Lapicera", 3),
("Mochila", 3),
("Valija", 3),
("Pañales", 4),
("Mamadera", 4),
("Chupete", 4),
("Babero", 4),
("Juguete", 4),
("Cochecito", 4),
("Sillita", 4),
("Bañadera", 4),
("Cambiador", 4),
("Ropa", 4),
("Aceite", 5),
("Vinagre", 5),
("Aderezo", 5),
("Arroz", 5),
("Porotos", 5),
("Garbanzos", 5),
("Lentejas", 5),
("Caldo", 5),
("Sopa", 5),
("Puré", 5),
("Azucar", 5),
("Edulcorante",	5),
("Cacao", 5),
("Café", 5),
("Cereal", 5),
("Galletas Dulces", 5),
("Galletas Saladas", 5),
("Leche", 5),
("Mermelada", 5),
("Yerba", 5),
("Té", 5),
("Bizcochuelo", 5),
("Alfajores", 5),
("Caramelos", 5),
("Chocolates", 5),
("Harina", 5),
("Avena", 5),
("Pan Integral", 5),
("Pan de Salvado", 5),
("Pan Lactal", 5),
("Pan Rallado", 5),
("Tostadas", 5),
("Sal", 5),
("Pimienta", 5),
("Fideos", 5),
("Snacks", 5),
("Agua", 6),
("Cerveza", 6),
("Champagne", 6),
("Energizante", 6),
("Gaseosa", 6),