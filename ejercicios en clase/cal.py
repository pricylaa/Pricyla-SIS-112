def calculadora():
    print("Selecciona la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    operacion = input("Introduce el número de la operación (1/2/3/4): ")

    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if operacion == '1':
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")

    if operacion == '2':
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")

    if operacion == '3':
        resultado = num1 * num2
        print(f"Resultado: {num1} * {num2} = {resultado}")

    if operacion == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("Error: División por cero no es posible")

    if operacion not in ['1', '2', '3', '4']:
        print("Operación no válida")

calculadora()
