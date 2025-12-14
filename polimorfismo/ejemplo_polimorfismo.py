
class Figura:
    def area(self):
        pass


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio * self.radio


# Prueba
if __name__ == "__main__":
    figuras = [
        Cuadrado(4),
        Circulo(3)
    ]

    for figura in figuras:
        print(f"Área: {figura.area()}")

