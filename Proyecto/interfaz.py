from tkinter import ttk
from tkinter import *
import sqlite3


class Vista:
    db_name = 'mibase.db'

    def __init__(self, ventana):
        self.vent = ventana
        self.vent.title('Compra Fácil')

        # Crear contenedor Frame
        frame = LabelFrame(self.vent, text='Lista de productos:')
        frame.grid(row=1, column=0, columnspan=10, pady=40, padx=40)

if __name__ == '__main__':
    ventana = Tk()
    app = Vista(ventana)
    ventana.mainloop()