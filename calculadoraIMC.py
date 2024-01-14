def calculadora():
    personas = int(input("personas: "))

    while personas > 0:
        nombre = input("Su nombre por favor: ")
        while validarCadena(nombre): #aca indicamos que si la funcion nos devuelve True, seguiraEs pidiendo el nombre
            nombre = input("Ingrese un nombre valido por favor: ")
        apellidoPaterno = input("Su apellido paterno por favor: ")
        while validarCadena(apellidoPaterno):
            apellidoPaterno = input("Ingrese un apellido paterno valido por favor: ")
        apellidoMaterno = input("Su apellido materno por favor: ")
        while validarCadena(apellidoMaterno):
            apellidoMaterno = input("Ingrese un apellido materno valido por favor: ")

        edad = validarEdad(input("Ingrese su edad: "))#validarEdad() devuelve 0, pediremos nuevamnte la edad ya que es ingresaron un valor no numerico
        while edad == 0:
            edad = validarEdad(input("Por favor ingresa un dato numerico: "))
        altura = validarAltura(input("Ingrese su altura con punto decimal por favor: "))
        while altura == 0:
            altura = validarAltura(input("Por favor ingrese un dato numerico con punto decimal por favor y que sea menor a 2 metros: "))

        masa = float(input("Su masa en kilogramos por favor :"))
        IMC = masa /altura ** 2
        if (edad < 18):
            print("Usted es menor de edad")
        else:
            print("Usted es mayor de edad")
        # Le imprimos el IMC para que se ponga sad
        print("IMC: " + str(IMC))

        # Hacemos las distintas validaciones
        if IMC >= 0 and IMC <= 15.99:
            print("Delgadez severa")
        elif IMC >= 16.00 and IMC <= 16.99:
            print("Delgadez moderada")
        elif IMC >= 17.00 and IMC <= 18.49:
            print("Delgadez leve")
        elif IMC >= 18.50 and IMC <= 24.99:
            print("Normal")
        elif IMC >= 25.00 and IMC <= 29.99:
            print("Sobrepeso")
        elif IMC >= 30.00 and IMC <= 34.99:
            print("obesidad leve")
        elif IMC >= 35.00 and IMC <= 39.00:
            print("obesidad media")
        elif IMC >= 40.00:
            print("obesidad morbida")

        print(nombre + " muchas gracias por utilizar nuestra calculadora de IMC.")

        # Por cada persona a la que le pedimos los datos debemos restarle una (Porque ya la recorrimos)
        # si no el ciclo se vuelve infinito
        personas = personas - 1



def validarCadena(texto):
    if texto == "":
        return True
    else:
        return False

def validarPesoAltura(numero):
    try:
        numero_valido = float(numero)
        return numero_valido
    except ValueError:
        return 0

def validarEdad(numero):
    try:
        numero_valido = int(numero)
        return numero_valido
    except ValueError:
        return 0

def validarAltura(numero):
    altura_valida = validarPesoAltura(numero)
    if altura_valida > 2:
        return 0
    else:
        return altura_valida

calculadora()