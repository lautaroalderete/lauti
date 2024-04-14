def solicitar_int(numero):
    return numero
numero = input("Ingrese un número: ")
numero = int(numero)
print(solicitar_int(numero))

def solicitar_float(numero):
    return numero
numero = input("Ingrese un número: ")
numero = float(numero)
print(solicitar_int(numero))

def solicitar_cadena(cadena):
    return cadena
peticion_uno = input("Ingrese algo: ")
peticion_dos = input("Ingrese otra cosa: ")
cadena = peticion_uno + peticion_dos
print(solicitar_cadena(cadena))