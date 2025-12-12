
class Persona:
    def hablar(self):
        print("Hola, soy una persona")

class Estudiante(Persona):
    def estudiar(self):
        print("Estoy estudiando")

est = Estudiante()
est.hablar()
est.estudiar()
