# Se crea una función para ingresar cantidad de número que se quieren analizar
def pedirNumeros(lista, cantidad):
    # Pido la cantidad     
    cantidad = int(input("Ingrese la cantidad de numeros a analizar: ")) 
    # En un bucle for se recorre hasta la cantidad ingresada anteriormente
    for k in range(cantidad):
        # Se ingresan los valores en una lista para buscar la constante de Kaprekar en una función después 
        lista.append(input("Ingrese un número: "))
    # Retorna la cantidad de número a analizar     
    return cantidad 