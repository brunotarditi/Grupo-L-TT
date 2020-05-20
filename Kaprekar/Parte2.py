def buscarConstante(lista, cantidad):
    for k in range(cantidad):
        numero = lista[k]
        n = int(numero)
        for k in range(10):
            numero = "{:04d}".format(n)
            if n == 6174:
                k = -1
                break
            descendente = "".join(sorted(numero,reverse = True))
            ascendente = "".join(sorted(numero))
            n = int(descendente) - int(ascendente)
            if n == 0:
                k = 7
                break
            if n == 6174:
                break
        print("--------------")
        print(k + 1)