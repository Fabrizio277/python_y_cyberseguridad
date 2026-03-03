#CIFRADO CESAR
#HAREMOS UN CIFRADO CESAR PARA LA PALABRA "INTER DE PORTO ALEGRE DESCENSO"
#LA CONSOLA NOS TIENE QUE PEDIR QUE DESPLAZAMIENTO QUEREMOS DESPUES DE PEDIRNOS LA PALABRA

print("=== CIFRADOR DE MENSAJES ===")

mensaje = input("mensaje: ").upper()
try:
    n = int(input("desplazamiento (1 al 25): "))
except:
    print("Error: El desplazamiento debe ser un número."); exit()

#CIFRADO
cifrado = ""
for car in mensaje:
    if 'A' <= car <= 'Z':
        nuevo_cod = ord(car) + n
        if nuevo_cod > ord('Z'):
            nuevo_cod -= 26
        cifrado += chr(nuevo_cod)
    else:
        cifrado += car

#DESCIFRADO
descifrado = ""
for car in cifrado:
    if 'A' <= car <= 'Z':
        nuevo_cod = ord(car) - n
        if nuevo_cod < ord('A'):
            nuevo_cod += 26
        descifrado += chr(nuevo_cod)
    else:
        descifrado += car

# IMPRESION
print(f"\n[+] cifrado:   {cifrado}")
print(f"[+] verificación: {descifrado}")