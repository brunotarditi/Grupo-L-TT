from tkinter import ttk
from tkinter import *
import sqlite3

class Vista:
    db_name = 'mibase.db'

    def _init_(self, ventana):
        self.vent = ventana
        self.vent.title('Compra Fácil')

        # Crear contenedor Frame
        frame = LabelFrame(self.vent, text='Lista de productos:')
        frame.grid(row=1, column=0, columnspan=10, pady=40, padx=40)
    
        # Tabla
        self.tree = ttk.Treeview(height=20, column=2)
        self.tree.grid(row=3, column=0)
        self.tree.heading('#0', text='Codigo', anchor=CENTER)
        self.tree.heading('#1', text='Categorías', anchor=CENTER)

        # Tabla
        self.tree1 = ttk.Treeview(height=20)
        self.tree1.grid(row=3, column=4)
        self.tree1.heading('#0', text='Productos', anchor=CENTER)

        # Botón para desplegar categorias y para agregar productos a la lista del usuario
        ttk.Button(text='Desplegar', command=self.desplegar).grid(row=5, column=0, sticky=W + E)
        ttk.Button(text='Agregar').grid(row=5, column=4, sticky=W + E)

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def get_products(self):

        # Consultando datos
        records = self.tree.get_children()
        for elementos in records:
            self.tree.delete(elementos)
        query = 'SELECT * FROM CATEGORIAS ORDER BY ID DESC'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('', 0, text=row[0], values=row[1])

if __name__ == '__main__':
    ventana = Tk()
    app = Vista(ventana)
    ventana.mainloop()