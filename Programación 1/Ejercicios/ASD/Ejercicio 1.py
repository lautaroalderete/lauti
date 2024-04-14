'''UTN TECHNOLOGIES

UTN Technologies, una reconocida software factory se encuentra en la búsqueda de ideas para su próximo desarrollo en Python, que promete revolucionar el mercado.

Las posibles aplicaciones son las siguientes:
Inteligencia artificial (IA),
Realidad virtual/aumentada (RV/RA),
Internet de las cosas (IOT)

Para ello, la empresa realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas.

A) Los datos a ingresar por cada empleado encuestado son:
nombre del empleado
edad (no menor a 18)
género (Masculino - Femenino - Otro)
tecnologia (IA, RV/RA, IOT)  
B) Cargar por terminal 10 encuestas.
C) Determinar:
1. Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
2. Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
2. Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.'''

contador = 0
contador_masculinos_iot_ia = 0
contador_no_ia_no_femenino_p2 = 0
maximo = 0
bandera = True
while contador <3:
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    edad = int(edad)
    while edad < 18:
        edad = input("Reingrese su edad: ")
        edad = int(edad)
    genero = input("Ingrese su género (Masculino - Femenino - Otro): ")
    while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        genero = input("Reingrese su género (Masculino - Femenino - Otro): ")
    tecnologia = input("Ingrese la tecnologia (IA, RV/RA, IOT): ")
    while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
        tecnologia = input("Reingrese la tecnologia (IA, RV/RA, IOT): ")
    contador += 1
    match genero:
        case "Masculino":
            if edad >25 and edad <= 50:
                if tecnologia == "IA" or tecnologia == "IOT":
                    contador_masculinos_iot_ia += 1
            if bandera == True or edad > maximo:
                maximo = edad
                nombre_maximo = nombre
                edad_maxima = edad
                bandera = False
    if tecnologia != "IA" and genero != "Femenino":
        if edad <33 or edad >40:
            contador_no_ia_no_femenino_p2 +=1
porcentaje_no_ia_no_femenino_p2 = (contador_no_ia_no_femenino_p2 * 100) / contador
print(f"La cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive fue de {contador_masculinos_iot_ia}")
print(f"El porcentaje de empleados que no votaron IA, su género no sea Femenino o su edad se encuentre entre los 33 y 40 es de {porcentaje_no_ia_no_femenino_p2}%")
print(f"El nombre y la edad del empleado masculino con más edad es: {nombre_maximo} con una edad de {edad_maxima} años")
