def convertir_longitud():
    print("\n--- Conversión de Longitud ---")
    print("1. Metros a Kilómetros")
    print("2. Kilómetros a Metros")
    print("3. Metros a Millas")
    print("4. Millas a Metros")
    opcion = input("Elige una opción: ")

    valor = float(input("Ingresa el valor a convertir: "))

    if opcion == '1':
        resultado = valor / 1000
        print(f"{valor} metros son {resultado} kilómetros")
    elif opcion == '2':
        resultado = valor * 1000
        print(f"{valor} kilómetros son {resultado} metros")
    elif opcion == '3':
        resultado = valor * 0.000621371
        print(f"{valor} metros son {resultado} millas")
    elif opcion == '4':
        resultado = valor / 0.000621371
        print(f"{valor} millas son {resultado} metros")
    else:
        print("Opción no válida.")

def convertir_peso():
    print("\n--- Conversión de Peso ---")
    print("1. Kilogramos a Libras")
    print("2. Libras a Kilogramos")
    opcion = input("Elige una opción: ")

    valor = float(input("Ingresa el valor a convertir: "))

    if opcion == '1':
        resultado = valor * 2.20462
        print(f"{valor} kg son {resultado} libras")
    elif opcion == '2':
        resultado = valor / 2.20462
        print(f"{valor} libras son {resultado} kg")
    else:
        print("Opción no válida.")

def convertir_temperatura():
    print("\n--- Conversión de Temperatura ---")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    opcion = input("Elige una opción: ")

    valor = float(input("Ingresa la temperatura a convertir: "))

    if opcion == '1':
        resultado = (valor * 9/5) + 32
        print(f"{valor} °C son {resultado} °F")
    elif opcion == '2':
        resultado = (valor - 32) * 5/9
        print(f"{valor} °F son {resultado} °C")
    else:
        print("Opción no válida.")

def menu():
    while True:
        print("\n=== Conversor de Unidades ===")
        print("1. Conversión de Longitud")
        print("2. Conversión de Peso")
        print("3. Conversión de Temperatura")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            convertir_longitud()
        elif opcion == '2':
            convertir_peso()
        elif opcion == '3':
            convertir_temperatura()
        elif opcion == '4':
            print("\nGracias por usar el conversor de unidades. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
