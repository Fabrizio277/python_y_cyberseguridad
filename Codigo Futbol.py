'''
Tópico Elegido: Fútbol
Propósito del Código: Este programa pide datos básicos de un jugador para calcular
                     su promedio de goles por partido. Determina si el promedio
                     supera un umbral mínimo.

Variables y Tipos:
- nombre (str): Almacena el nombre del jugador.
- partidos (str -> int): Total de partidos jugados (se pide como string y se
                         convierte a entero).
- goles (int): Número total de goles anotados.
- promedio_goles (float): Resultado de la división Goles / Partidos.
- es_eficiente (bool): Resultado de la comparación, verdadero si el promedio supera
                       el umbral mínimo.

Constantes:
- UMBRAL_MINIMO_PROMEDIO (float): Mínimo promedio de goles por partido requerido (0.5).
'''

# --- CONSTANTES ---
# Mínimo de 0.5 goles por partido para ser considerado 'eficiente'
UMBRAL_MINIMO_PROMEDIO = 0.5
# --------------------

# 1. PIDE DATOS AL USUARIO

print("--- ⚽ CÁLCULO DE PROMEDIO DE GOLES ---")

# Tipo 1: str
nombre = input("Introduce el nombre del jugador: ")

# Tipo 2: int
goles = int(input(f"¿Cuántos goles anotó {nombre}? "))

# 2. CONVERSIÓN DE DATOS
# Tipo 3: str -> int
partidos_str = input(f"¿Cuántos partidos jugó {nombre}? ")
partidos = int(partidos_str) # Conversión de string a entero

print("\n--- Analizando rendimiento... ---")

# 3. OPERACIONES ENTRE VARIABLES (Aritméticas)

# Cálculo Aritmético: División
if partidos > 0:
    promedio_goles = goles / partidos
else:
    promedio_goles = 0.0

# 4. OPERACIONES ENTRE VARIABLES (Comparación y Lógicas)

# Operación de Comparación: >= (Mayor o igual que)
es_eficiente_comparacion = promedio_goles >= UMBRAL_MINIMO_PROMEDIO

# Operación Lógica: AND (Asegura que el promedio sea positivo para ser 'eficiente')
# Tipo: bool
es_eficiente = es_eficiente_comparacion and (partidos > 0)


# 5. ENSEÑA DATOS AL USUARIO

print("\n--- 📊 RESULTADOS ---")
print(f"Jugador: **{nombre.upper()}**")
print(f"Goles: {goles} | Partidos: {partidos}")

# Muestra el resultado de la operación aritmética
print(f"**Promedio de Goles por Partido:** **{promedio_goles:.2f}**")

# Muestra el resultado de la operación lógica/comparación
print(f"Umbral Mínimo Requerido: {UMBRAL_MINIMO_PROMEDIO}")
print(f"¿Rendimiento Eficiente? {es_eficiente}")

if es_eficiente:
    print("¡Excelente! Ha superado el umbral.")
else:
    print("El jugador necesita mejorar su cuota goleadora.")