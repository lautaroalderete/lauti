def encontrar_par(numero):
    if numero % 2 == 0:
        mensaje = "Es par"
    else:
        mensaje= "Es impar"
    return mensaje
numero = input("Ingrese un número: ")
numero = int(numero)
print(encontrar_par(numero))