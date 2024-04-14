def encontrar_maximo():
    maximo = 0
    for i in range(3):
        numero = input("Ingrese un número: ")
        numero = int(numero)
        if numero > maximo:
            maximo = numero
    return maximo
print(encontrar_maximo())