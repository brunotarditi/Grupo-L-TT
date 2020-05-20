def pedirNumeros(lista, cantidad):
    cantidad = int(input("Ingrese la cantidad de numeros a analizar: "))
    for k in range(cantidad):
        lista.append(input("Ingrese un número: "))
    return cantidad