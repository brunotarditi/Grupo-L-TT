import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3

class Vista:
    db_name = 'mibase.db'
    
    def __init__(self, ventana):
        self.vent = ventana
        self.vent.title('Compra Fácil')
        self.Producto=""
        #self.vent.iconbitmap('compra-facil-logo.ico')
        self.imgCancelar = PhotoImage(file = ['cancelar.png'])
        self.imgGuardar = PhotoImage(file = ['guardar.png'])
        self.imgEditar = PhotoImage(file = ['editar.png'])
        self.imgSalir = PhotoImage(file = ['salir.png'])

        # Crear contenedor Frame
        frame = LabelFrame(self.vent, text='Agregar y editar:')
        frame.grid(row=0, column=0, pady=20, padx=17)

        # Nombre
        Label(frame, text='Nombre: ').grid(row=1, column=0)
        self.nombre = tk.StringVar(frame)
        entry = ttk.Entry(ventana, textvariable=self.nombre)
        entry.place(x=75, y=38)

        # Precio
        Label(frame, text='Precio: ').grid(row=2, column=0)
        self.p = Entry(frame)
        self.p.grid(row=2, column=1)
        self.precio = tk.StringVar(frame)
        entry = ttk.Entry(ventana, textvariable=self.precio)
        entry.place(x=75, y=58)

        # Marca
        Label(frame, text='Marca: ').grid(row=1, column=2)
        self.m = Entry(frame)
        self.m.grid(row=1, column=3)
        self.marca = tk.StringVar(frame)
        entry = ttk.Entry(ventana, textvariable=self.marca)
        entry.place(x=258, y=38)

        # Cantidad
        Label(frame, text='Cantidad: ').grid(row=2, column=2)
        self.c = Entry(frame)
        self.c.grid(row=2, column=3)
        self.cantidad = tk.StringVar(frame)
        entry = ttk.Entry(ventana, textvariable=self.cantidad)
        entry.place(x=258, y=58)

        # Total
        Label(self.vent, text='TOTAL : ').grid(row=2, column=2)
        self.total = tk.StringVar()
        entry = ttk.Entry(ventana, textvariable=self.total, state='readonly')
        entry.place(x=935, y=135)

        # Mensaje saliente
        self.mensaje = Label(text = '', fg = 'red' )
        self.mensaje.grid(row=3, column=0, columnspan=3, sticky=W + E)

        # Mensaje informativo
        Label(self.vent, text = '*El total solo considera productos con precio distinto de cero.', foreground = 'green' ).place(x=820, y=160)
    
        # Tabla
        self.tree = ttk.Treeview(height=22)
        self.tree["columns"]=("1")
        self.tree.column("0", width=50, minwidth=30, stretch=tk.NO)
        self.tree.column("1", width=200, minwidth=100, stretch=tk.NO)
        self.tree.grid(row=4, column=0)
        self.tree.heading('#0', text='Codigo', anchor=CENTER)
        self.tree.heading('#1', text='Categorías', anchor=CENTER)

        # Tabla1
        self.tree1 = ttk.Treeview(height=22)
        self.tree1.grid(row=4, column=1)
        self.tree1.heading('#0', text='Productos', anchor=CENTER)

        # Tabla2
        self.tree2 = ttk.Treeview(height=22, columns=(1,2,3,4), show="headings")
        self.tree2.column(1, width=150, minwidth=150, stretch=tk.NO)
        self.tree2.column(2, width=150, minwidth=150, stretch=tk.NO)
        self.tree2.column(3, width=150, minwidth=150, stretch=tk.NO)
        self.tree2.column(4, width=150, minwidth=150, stretch=tk.NO)
        self.tree2.grid(row=4, column=2)
        self.tree2.heading(1, text='Nombre', anchor=CENTER)
        self.tree2.heading(2, text='Marca', anchor=CENTER)
        self.tree2.heading(3, text='Precio', anchor=CENTER)
        self.tree2.heading(4, text='Cantidad', anchor=CENTER)
        self.tree2.tag_configure('color', background='green', foreground='white')

        # Botones
        ttk.Button(text='Desplegar >>>', command=self.desplegar).grid(row=5, column=0, sticky=W + E)
        ttk.Button(text='Agregar ^ ^ ^', command=self.agregarProducto).grid(row=5, column=1, sticky=W + E)
        ttk.Button(text='    Borrar    ', command=self.borrarProducto, image=self.imgCancelar, compound="left").grid(row=5, column=2, sticky=W)
        ttk.Button(text='    Editar    ', command=self.editarProducto, image=self.imgEditar, compound="left").grid(row=5, column=2, sticky=E)
        ttk.Button(text='Guardar Producto', command=self.guardarProducto, image=self.imgGuardar, compound="left").grid(row=2, column=0, sticky=W + E)
        ttk.Button(text='  Borrar Campos  ', command=self.borrarCampos, image=self.imgSalir, compound="left").grid(row=1, column=0, sticky=W + E)
        
        self.get_productos()
        
        self.calcularTotal()

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def get_productos(self):
        records = self.tree.get_children()
        for elementos in records:
            self.tree.delete(elementos)
        query = 'SELECT * FROM CATEGORIAS ORDER BY ID DESC'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('', 0, text=row[0], values=row[1])
    
    def get_productosLista(self):
        records = self.tree2.get_children()
        for elementos in records:
            self.tree2.delete(elementos)
        query = 'SELECT * FROM LISTA WHERE Precio > 0'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree2.insert('' ,0 ,values=row, tags=('color',))
        query = 'SELECT * FROM LISTA WHERE Precio <= 0'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree2.insert('' ,0 ,values=row)
        self.calcularTotal()

    def calcularTotal(self):
        query = "SELECT sum(Precio * Cantidad) FROM LISTA"
        db_rows = self.run_query(query)
        for row in db_rows:
            self.total.set(row)

    def desplegar(self):
        self.mensaje['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.mensaje['text'] = 'Por favor selecciona una categoría.'
            return
        fila = self.tree.item(self.tree.selection())['text']
        indice = int(fila)
        if  (indice==1):
            records = self.tree1.get_children()
            for elementos in records:
                self.tree1.delete(elementos)
            query = 'SELECT Nombre FROM PRODUCTOS WHERE IdCategoria=1'
            db_rows = self.run_query(query)
            for row in db_rows:
                self.tree1.insert('', 0, text=row[0])
        if  (indice==2):
            records = self.tree1.get_children()
            for elementos in records:
                self.tree1.delete(elementos)
            query = 'SELECT Nombre FROM PRODUCTOS WHERE IdCategoria=2'
            db_rows = self.run_query(query)
            for row in db_rows:
                self.tree1.insert('', 0, text=row[0])
        if  (indice==3):
            records = self.tree1.get_children()
            for elementos in records:
                self.tree1.delete(elementos)
            query = 'SELECT Nombre FROM PRODUCTOS WHERE IdCategoria=3'
            db_rows = self.run_query(query)
            for row in db_rows:
                self.tree1.insert('', 0, text=row[0])
        if  (indice==4):
            records = self.tree1.get_children()
            for elementos in records:
                self.tree1.delete(elementos)