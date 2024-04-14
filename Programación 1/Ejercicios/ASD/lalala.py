def sumar_1():
    numero_uno = input("Ingrese un numero: ")
    numero_uno = int(numero_uno)
    numero_dos = input("Ingrese otro numero: ")
    numero_dos = int(numero_dos)

    suma = numero_dos + numero_uno

    print(f"La suma es {suma}")

#sumar_1() #Llamar a la función, esta funcion NO recibe parametros y NO devuelve nada


def sumar_2(numero_uno,numero_dos):
    suma = numero_uno + numero_dos

    print(f"La suma es {suma}")

#numero_uno = input("Ingrese un numero: ")
#numero_uno = int(numero_uno)
#numero_dos = input("Ingrese otro numero: ")
#numero_dos = int(numero_dos)
#sumar_2(numero_uno, numero_dos) #Esta función recibe parametros pero NO devuelve nada.

def sumar_3():
    numero_uno = input("Ingrese un numero: ")
    numero_uno = int(numero_uno)
    numero_dos = input("Ingrese otro numero: ")
    numero_dos = int(numero_dos)

    suma = numero_dos + numero_uno
    return suma

#resultado = sumar_3()
#print(f"La suma es {resultado}")

def sumar_4(numero_uno, numeros_dos):  #INDEPENDIENTE Y REUTILIZABLE
    suma = numero_uno + numeros_dos

    return suma

un_numero = input("Ingrese un numero: ")
un_numero = int(un_numero)
otro_numero = input("Ingrese otro numero: ")
otro_numero = int(otro_numero)
resultado = sumar_4(un_numero,otro_numero)

print(f"La suma es {resultado}")