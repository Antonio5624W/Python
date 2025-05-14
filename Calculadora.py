def calculadora():
    print("Bienvenido a la calculadora Tono de Voz")
    print("Operaciones basicas a realizar")

    operacion = input("Introduce la operacion que quieres realizar: ").lower()
    Num1 = float(input("Introduce el Primer Numero "))
    Num2 = float(input("Introduce el Segundo Numero "))

    if operacion == "suma":
        print(f"El resultado es: {Num1 + Num2}")
    elif operacion == "resta":
        print(f"El resultado es: {Num1 - Num2}")
    elif operacion == "multiplicacion":
        print(f"El resultado es : {Num1 * Num2}")
    elif operacion == "division":
         if Num2 != 0:
            print(f"El resultado es: {Num1 / Num2}")
         else:
             print("No se puede dividir entre 0.")
    else:
        print("Operacion No Valida.")
calculadora()