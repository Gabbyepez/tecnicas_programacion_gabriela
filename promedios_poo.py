
# -------------------------------------------------------------
# TAREA: Promedio semanal del clima - Programación Orientada a Objetos
# Elaborado por: Gabriela
# -------------------------------------------------------------

class ClimaSemanal:
    def __init__(self):
        # Encapsulamiento: atributo privado
        self.__temperaturas = [21, 24, 22, 25, 20, 26, 24]

    # Método para mostrar las temperaturas
    def mostrar_temperaturas(self):
        print("Temperaturas registradas:", self.__temperaturas)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        return sum(self.__temperaturas) / len(self.__temperaturas)

# ---------------- PROGRAMA PRINCIPAL ----------------
clima = ClimaSemanal()

print("\n=== PROGRAMACIÓN ORIENTADA A OBJETOS ===")
clima.mostrar_temperaturas()
promedio = clima.calcular_promedio()
print(f"Promedio semanal del clima: {promedio:.2f}°C")

