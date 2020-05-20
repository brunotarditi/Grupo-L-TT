# Importamos la función de parte1.py
from parte1 import pedirNumeros
# Importamos la función de parte2.py
from parte2 import buscarConstante
# Se crear una variable que contendra una lista
lista = []
# Variable cantidad en 0
cantidad = 0
# Retorna la cantidad de la función de parte1
cantidad = pedirNumeros(lista, cantidad)
# Se busca la constante de kaprekar de la función parte2
buscarConstante(lista, cantidad)