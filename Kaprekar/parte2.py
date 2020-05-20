def buscarConstante(lista, cantidad): #Método que busca las iteraciones para llegar a la constante. Recibe una lista de valores y el largo de dicha lista.
    for k in range(cantidad): # Para todos los elementos de la lista.
        numero = lista[k] # Guardo el elemento en una variable auxiliar.
        n = int(numero) # Casteo y guardo como entero dicho valor en otra variable.
        for k in range(10): # En un máximo de 10 iteraciones.
            numero = "{:04d}".format(n) # Si el valor ingresado no tiene 4 cifras lo completo con ceros.
            if n == 6174: # Si el valor es igual a la constante, salgo y muestro 0.
                k = -1
                break
            descendente = "".join(sorted(numero,reverse = True)) # Ordeno las cifras de mayor a menor.
            ascendente = "".join(sorted(numero)) # Ordeno las cifras de menor a mayor.
            n = int(descendente) - int(ascendente) # Resto ambos números ordenados.
            if n == 0: # Si el valor se convierte en 0, significa que ingresé 4 cifras iguales (ej: 1111). Salgo y muestro 8.
                k = 7
                break
            if n == 6174: # Si el valor se convierte en la constante, salgo y muestro el número de iteraciones k.
                break
        print("--------------") # Imprimo un separador.
        print(k + 1) # Imprimo el número de iteraciones k.