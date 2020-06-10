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

if __name__ == '__main__':
    ventana = Tk()
    app = Vista(ventana)
    ventana.mainloop()