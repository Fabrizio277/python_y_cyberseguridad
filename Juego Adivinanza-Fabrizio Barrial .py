#CODIGO ADIVINANZA
#Primero la maquina eligira un numero aleatorio del 1 al 10
#Luego definimos cuantos intentos tendra el participante.
#Despues pediremos al participante que intente advinar el numero que fue elegido por la maquina.
#Si el participante logra acertar le damos el mensaje de "Ganador"
#Si el participante no logra acartar le damos el mensaje de "Perdedor"

import random

print("-" * 50)
print("Bienvenido al juego de adivina el numero")
print("Tendras adivinar el numero del 1 al 10 pero tendras intentos limitados")
print("Venga a currar chaval")
print("-" * 50)

rango_min = 1
rango_max = 10
limite = 5

numero_secreto = random.randint(rango_min,rango_max)
intentos_restantes = limite
juego_terminado = False

while intentos_restantes > 0 and not juego_terminado:
    print(f"\nTe quedan {intentos_restantes} intentos.")

    try:
        entrada_usuario = input("Ingresa tu intento: ")
        intento_usuario = int(entrada_usuario)
        if intento_usuario == numero_secreto:
             juego_terminado = True
        else:
             print("Intento incorrecto. ¡Muy mal, dame otro numero!")
             intentos_restantes -= 1
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingresa un número entero.")

print("-" * 50)
if juego_terminado:
    intentos_utilizados = limite - intentos_restantes
    print(f"¡ACERTASTESSS!!!! Adivinaste el número secreto BOBO ({numero_secreto}) en {intentos_utilizados} intentos.")
    print("¡VIVAAA EL FLAMENGOOOOOOO!")
else:
    print("Fua... FALLASTE, no hay mas intentos bobo")
    print("¡VIVAAA EL FLAMENGOOOOOO!")
    print(f"El número secreto era: {numero_secreto}.")
print("-" * 50)