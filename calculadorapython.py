def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def calculadora():
    print("Calculadora en Python siuuuuu")
    print("Operaciones: sumar, restar, multiplicar, dividir")
    
    operacion = input("Elige una operacion aritmetica: ").lower()
    a = float(input("Ingresa el primer nuumero: "))
    b = float(input("Ingresa el segundo numero: "))

    if operacion == "sumar":
        resultado = sumar(a, b)
    elif operacion == "restar":
        resultado = restar(a, b)
    elif operacion == "multiplicar":
        resultado = multiplicar(a, b)
    elif operacion == "dividir":
        resultado = dividir(a, b)
    else:
        resultado = "Operación no valida"

    print("Resultado:", resultado)

# Ejecutar la calculadora
calculadora()
