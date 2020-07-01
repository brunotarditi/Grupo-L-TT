import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3


class Vista:
    # Me conecto con la base de datos.
    db_name = 'mibase.db'

    # Método init.
    def __init__(self, ventana):
        self.vent = ventana

        # Defino un nombre para la ventana.
        self.vent.title('Compra Fácil')
        self.Producto = ""

        # Defino un ícono para la app.
        self.vent.iconbitmap('compra-facil.ico')

        # Defino un ícono de botón.
        self.imgCancelar = PhotoImage(file=['cancelar.png'])

        # Defino un ícono de botón.
        self.imgGuardar = PhotoImage(file=['guardar.png'])

        # Defino un ícono de botón.
        self.imgEditar = PhotoImage(file=['editar.png'])

        # Defino un ícono de botón.
        self.imgSalir = PhotoImage(file=['salir.png'])

        # Creo un contenedor Frame.
        frame = LabelFrame(self.vent, text='Agregar y editar:')
        # Defino su lugar.
        frame.grid(row=0, column=0, pady=20, padx=17)

        # Creo una caja de texto para Nombre.
        Label(frame, text='Nombre: ').grid(row=1, column=0)
        self.nombre = tk.StringVar(frame)
        entry = ttk.Entry(ventana, textvariable=self.nombre)
        # Defino su lugar.
        entry.place(x=75, y=38)

        # Creo una caja de texto para Precio.
        Label(frame, text='Precio: ').grid(row=2, column=0)
        self.p = Entry(frame)
        self.p.grid(row=2, column=1)
        self.precio = tk.StringVar(frame)
        entry = ttk.Entry(ventana, textvariable=self.precio)
        # Defino su lugar.
        entry.place(x=75, y=58)

        # Creo una caja de texto para Marca.
        Label(frame, text='Marca: ').grid(row=1, column=2)
        self.m = Entry(frame)
        self.m.grid(row=1, column=3)
        self.marca = tk.StringVar(frame)
        entry = ttk.Entry(ventana, textvariable=self.marca)
        # Defino su lugar.
        entry.place(x=258, y=38)

        # Creo una caja de texto para Cantidad.
        Label(frame, text='Cantidad: ').grid(row=2, column=2)
        self.c = Entry(frame)
        self.c.grid(row=2, column=3)
        self.cantidad = tk.StringVar(frame)
        entry = ttk.Entry(ventana, textvariable=self.cantidad)
        # Defino su lugar.
        entry.place(x=258, y=58)

        # Creo una caja de texto para Total.
        Label(self.vent, text='TOTAL : ').grid(row=2, column=2)
        self.total = tk.StringVar()
        entry = ttk.Entry(ventana, textvariable=self.total, state='readonly')
        # Defino su lugar.
        entry.place(x=935, y=135)

        # Creo un mensaje saliente para errores y operaciones.
        self.mensaje = Label(text='', fg='red')
        # Defino su lugar.
        self.mensaje.grid(row=3, column=0, columnspan=3, sticky=W + E)

        # Creo un mensaje informativo fijo.
        Label(self.vent, text='*El total solo considera productos con precio distinto de cero.',
              foreground='green').place(x=820, y=160)

        # Creo una tabla para mostrar categorías.
        self.tree = ttk.Treeview(height=22)
        # Defino sus columnas.
        self.tree["columns"] = ("1")
        self.tree.column("0", width=50, minwidth=30, stretch=tk.NO)
        self.tree.column("1", width=200, minwidth=100, stretch=tk.NO)
        # Defino su lugar.
        self.tree.grid(row=4, column=0)
        # Defino las cabeceras de columnas.
        self.tree.heading('#0', text='Codigo', anchor=CENTER)
        self.tree.heading('#1', text='Categorías', anchor=CENTER)

        # Creo una tabla1 para mostrar los productos de cada categoría.
        self.tree1 = ttk.Treeview(height=22)
        # Defino sus columnas.
        self.tree1.heading('#0', text='Productos', anchor=CENTER)
        # Defino su lugar.
        self.tree1.grid(row=4, column=1)

        # Creo una tabla2 para mostrar mi lista de compras.
        self.tree2 = ttk.Treeview(height=22, columns=(1, 2, 3, 4), show="headings")
        # Defino sus columnas.
        self.tree2.column(1, width=150, minwidth=150, stretch=tk.NO)
        self.tree2.column(2, width=150, minwidth=150, stretch=tk.NO)
        self.tree2.column(3, width=150, minwidth=150, stretch=tk.NO)
        self.tree2.column(4, width=150, minwidth=150, stretch=tk.NO)
        # Defino su lugar.
        self.tree2.grid(row=4, column=2)
        # Defino las cabeceras de columnas.
        self.tree2.heading(1, text='Nombre', anchor=CENTER)
        self.tree2.heading(2, text='Marca', anchor=CENTER)
        self.tree2.heading(3, text='Precio', anchor=CENTER)
        self.tree2.heading(4, text='Cantidad', anchor=CENTER)
        # Defino el color de las filas.
        self.tree2.tag_configure('color', background='green', foreground='white')

        # Creo botón con su lugar y su ícono.
        ttk.Button(text='Desplegar >>>', command=self.desplegar).grid(row=5, column=0, sticky=W + E)

        # Creo botón con su lugar y su ícono.
        ttk.Button(text='Agregar ^ ^ ^', command=self.agregarProducto).grid(row=5, column=1, sticky=W + E)

        # Creo botón con su lugar y su ícono.
        ttk.Button(text='    Borrar    ', command=self.borrarProducto, image=self.imgCancelar, compound="left").grid(
            row=5, column=2, sticky=W)

        # Creo botón con su lugar y su ícono.
        ttk.Button(text='    Editar    ', command=self.editarProducto, image=self.imgEditar, compound="left").grid(
            row=5, column=2, sticky=E)

        # Creo botón con su lugar y su ícono.
        ttk.Button(text='Guardar Producto', command=self.guardarProducto, image=self.imgGuardar, compound="left").grid(
            row=2, column=0, sticky=W + E)

        # Creo botón con su lugar y su ícono.
        ttk.Button(text='  Borrar Campos  ', command=self.borrarCampos, image=self.imgSalir, compound="left").grid(
            row=1, column=0, sticky=W + E)

        # Llamo al método.
        self.get_productos()

        # Llamo al método.
        self.calcularTotal()

    # Método que ejecuta la consulta a la base de datos.
    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    # Método que muestra las categorías.
    def get_productos(self):
        records = self.tree.get_children()
        for elementos in records:
            self.tree.delete(elementos)
        # Consulto a la base de datos.
        query = 'SELECT * FROM CATEGORIAS ORDER BY ID DESC'
        # Llamo al método.
        db_rows = self.run_query(query)
        # Inserto en la tabla.
        for row in db_rows:
            self.tree.insert('', 0, text=row[0], values=row[1])

    # Método que muestra los productos en mi lista de compras.
    def get_productosLista(self):
        # Limpio la lista.
        records = self.tree2.get_children()
        for elementos in records:
            self.tree2.delete(elementos)
        # Consulto a la base de datos.
        query = 'SELECT * FROM LISTA WHERE Precio > 0'
        # Llamo al método.
        db_rows = self.run_query(query)
        # Inserto en la tabla productos con precio mayor a cero y pinto las filas de verde.
        for row in db_rows:
            self.tree2.insert('', 0, values=row, tags=('color',))
        # Consulto a la base de datos.
        query = 'SELECT * FROM LISTA WHERE Precio <= 0'
        # Llamo al método.
        db_rows = self.run_query(query)
        # Inserto en la tabla productos sin precio.
        for row in db_rows:
            self.tree2.insert('', 0, values=row)
        # Llamo al método.
        self.calcularTotal()

    # Método que calcula el total de la lista, considerando precio y cantidad.
    def calcularTotal(self):
        # Consulto a la base de datos.
        query = "SELECT sum(Precio * Cantidad) FROM LISTA"
        # Llamo al método.
        db_rows = self.run_query(query)
        # Inserto en la caja de texto el total.
        for row in db_rows:
            self.total.set(row)

    # Método que muestra los productos de cada categoría.
    def desplegar(self):
        # Mensaje saliente en caso de no seleccionar una categoría.
        self.mensaje['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.mensaje['text'] = 'Por favor selecciona una categoría.'
            return

        # Tomo el índice de la selección del usuario.
        fila = self.tree.item(self.tree.selection())['text']
        indice = int(fila)

        # Si se selcciona la categoría 1.
        if (indice == 1):
            # Limpio la lista.
            records = self.tree1.get_children()
            for elementos in records:
                self.tree1.delete(elementos)
            # Consulto a la base de datos.
            query = 'SELECT Nombre FROM PRODUCTOS WHERE IdCategoria=1'
            # Llamo al método.
            db_rows = self.run_query(query)
            # Muestro los productos de la categoría.
            for row in db_rows:
                self.tree1.insert('', 0, text=row[0])

        # Si se selcciona la categoría 2.
        if (indice == 2):
            # Limpio la lista.
            records = self.tree1.get_children()
            for elementos in records:
                self.tree1.delete(elementos)
            # Consulto a la base de datos.
            query = 'SELECT Nombre FROM PRODUCTOS WHERE IdCategoria=2'
            # Llamo al método.
            db_rows = self.run_query(query)
            # Muestro los productos de la categoría.
            for row in db_rows:
                self.tree1.insert('', 0, text=row[0])

        # Si se selcciona la categoría 3.
        if (indice == 3):
            # Limpio la lista.
            records = self.tree1.get_children()
            for elementos in records:
                self.tree1.delete(elementos)
            # Consulto a la base de datos.
            query = 'SELECT Nombre FROM PRODUCTOS WHERE IdCategoria=3'
            # Llamo al método.
            db_rows = self.run_query(query)
            # Muestro los productos de la categoría.
            for row in db_rows:
                self.tree1.insert('', 0, text=row[0])

        # Si se selcciona la categoría 4.
        if (indice == 4):
            # Limpio la lista.
            records = self.tree1.get_children()
            for elementos in records:
                self.tree1.delete(elementos)
            # Consulto a la base de datos.
            query = 'SELECT Nombre FROM PRODUCTOS WHERE IdCategoria=4'
            # Llamo al método.
            db_rows = self.run_query(query)
            # Muestro los productos de la categoría.
            for row in db_rows:
                self.tree1.insert('', 0, text=row[0])

        # Si se selcciona la categoría 5.
        if (indice == 5):
            # Limpio la lista.
            records = self.tree1.get_children()
            for elementos in records:
                self.tree1.delete(elementos)