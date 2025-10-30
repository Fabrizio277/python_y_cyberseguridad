'''
Descripción del Código:
Este programa es una calculadora interactiva que permite al usuario elegir entre
siete operaciones aritméticas: suma, resta, multiplicación, división normal,
división entera, potencia, y resto de la división (módulo).

Manejo de Errores:
- Valida que la operación seleccionada sea una opción válida (1-7).
- Valida que los operandos sean números válidos (enteros o decimales).
- Maneja específicamente la División por Cero, solicitando un nuevo divisor.
- Permite al usuario realizar múltiples operaciones de forma continua.

Variables utilizadas:
- **opcion (str):** Almacena la selección de la operación del usuario. Tipo: string (se convierte a int para la validación).
- **num1 (float):** Primer operando (dividendo/base). Tipo: float.
- **num2 (float):** Segundo operando (divisor/exponente). Tipo: float.
- **continuar (str):** Opción del usuario para seguir usando la calculadora. Tipo: string.
'''

def pedir_operando(mensaje):
    """
    Función para solicitar un operando al usuario y validar que sea un número.
    Maneja el error de ValueError si el input no puede convertirse a float.
    """
    while True:
        try:
            # Pide datos al usuario y convierte a float (permite decimales)
            numero = float(input(mensaje))
            return numero
        except ValueError:
            # Manejo de input incorrecto
            print("❌ ERROR: Input no válido. Por favor, ingrese un número (entero o decimal).")


def obtener_operacion():
    """
    Muestra el menú y solicita la opción de operación, validando que sea una
    opción válida (1 a 7).
    """
    while True:
        print("\n--- 🔧 MENÚ DE OPERACIONES ---")
        print("1. Suma (a + b)")
        print("2. Resta (a - b)")
        print("3. Multiplicación (a * b)")
        print("4. División Normal (a / b)")
        print("5. División Entera (a // b)")
        print("6. Potencia (a ** b)")
        print("7. Resto de División (a % b)")
        
        # Pide datos al usuario (operación)
        opcion = input("Elige la operación (1-7): ")
        
        # Validación de la opción
        if opcion.isdigit() and 1 <= int(opcion) <= 7:
            return int(opcion)
        else:
            print("❌ ERROR: Opción no válida. Por favor, elige un número del 1 al 7.")
            # Vuelve a pedir los datos al usuario

def calculadora():
    """
    Función principal que contiene el algoritmo de la calculadora.
    """
    continuar = 's'
    
    # Bucle principal: Permite al usuario realizar otra operación
    while continuar.lower() == 's':
        
        # 1. Pide la operación
        opcion = obtener_operacion()
        
        # 2. Pide los dos operandos
        num1 = pedir_operando("Introduce el primer número (a): ")
        
        # Lógica especial para la división (manejo de división por cero)
        if opcion in [4, 5, 7]:
            while True:
                num2 = pedir_operando("Introduce el segundo número (b): ")
                # Manejo de error: división por cero
                if num2 == 0:
                    # Informa al usuario y pide que elija otro número
                    print("🚫 ERROR: No se puede dividir por cero. Por favor, introduce un divisor diferente.")
                    # Vuelve a pedir los datos al usuario (el bucle while True lo hace)
                else:
                    break # Sale del bucle de validación si num2 es válido
        else:
            # Para operaciones sin riesgo de división por cero
            num2 = pedir_operando("Introduce el segundo número (b): ")

        # 3. Realiza y enseña el resultado (Manejo de las operaciones)
        resultado = None
        operacion_str = ""
        
        if opcion == 1:
            resultado = num1 + num2
            operacion_str = f"{num1} + {num2}"
        elif opcion == 2:
            resultado = num1 - num2
            operacion_str = f"{num1} - {num2}"
        elif opcion == 3:
            resultado = num1 * num2
            operacion_str = f"{num1} * {num2}"
        elif opcion == 4:
            resultado = num1 / num2
            operacion_str = f"{num1} / {num2}"
        elif opcion == 5:
            # Asegura que la división entera trabaje con enteros si es posible
            resultado = int(num1) // int(num2)
            operacion_str = f"{num1} // {num2}"
        elif opcion == 6:
            resultado = num1 ** num2
            operacion_str = f"{num1} ** {num2}"
        elif opcion == 7:
            # Asegura que el módulo trabaje con enteros si es posible
            resultado = int(num1) % int(num2)
            operacion_str = f"{num1} % {num2}"
        
        # Enseña el resultado al usuario
        print(f"\n✅ El resultado de la operación: {operacion_str} es = **{resultado}**")
        
        # 4. Opción para seguir
        print("\n------------------------------------")
        continuar = input("¿Quieres realizar otra operación? (s/n): ")
        print("------------------------------------")

    print("\n👋 ¡Gracias por usar la calculadora! Hasta pronto.")


if __name__ == "__main__":
    calculadora()