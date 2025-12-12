
# -------------------------------------------------------------
# TAREA: Promedio semanal del clima - Programación Tradicional
# Elaborado por: Gabriela
# -------------------------------------------------------------

# Función que devuelve las temperaturas de la semana
def obtener_temperaturas():
    # Temperaturas registradas (añadidas directamente)
    temperaturas = [22, 24, 23, 25, 21, 26, 24]
    return temperaturas

# Función que calcula el promedio semanal
def calcular_promedio(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

# ---------------- PROGRAMA PRINCIPAL ----------------
temperaturas_semana = obtener_temperaturas()
promedio = calcular_promedio(temperaturas_semana)

print("=== PROGRAMACIÓN TRADICIONAL ===")
print("Temperaturas de la semana:", temperaturas_semana)
print(f"Promedio semanal del clima: {promedio:.2f}°C")
