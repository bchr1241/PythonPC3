class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "I"
        elif self.x < 0 and self.y > 0:
            return "II"
        elif self.x < 0 and self.y < 0:
            return "III"
        elif self.x > 0 and self.y < 0:
            return "IV"
        elif self.x == 0 and self.y != 0:
            return "sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "sobre el eje X"
        else:
            return "en el origen"

    def vector(self, otro_punto):
        return Punto(otro_punto.x - self.x, otro_punto.y - self.y)


class Rectangulo:
    def __init__(self, punto1=Punto(), punto2=Punto()):
        self.punto1 = punto1
        self.punto2 = punto2

    def base(self):
        return abs(self.punto2.x - self.punto1.x)

    def altura(self):
        return abs(self.punto2.y - self.punto1.y)

    def area(self):
        return self.base() * self.altura()

def main():
    # Crear puntos
    punto1 = Punto(3, 4)
    punto2 = Punto(-2, 5)
    punto3 = Punto(-3, -3)
    punto4 = Punto(0, 0)

    # Imprimir puntos y sus cuadrantes
    print(punto1)  # Output: (3,4)
    print(f"El punto {punto1} está en el cuadrante: {punto1.cuadrante()}")

    print(punto2)  # Output: (-2,5)
    print(f"El punto {punto2} está en el cuadrante: {punto2.cuadrante()}")

    print(punto3)  # Output: (-3,-3)
    print(f"El punto {punto3} está en el cuadrante: {punto3.cuadrante()}")

    print(punto4)  # Output: (0,0)
    print(f"El punto {punto4} está {punto4.cuadrante()}")

    # Calcular el vector entre dos puntos
    vector_resultante = punto1.vector(punto2)
    print(f"El vector entre {punto1} y {punto2} es {vector_resultante}")

    # Crear un rectángulo
    rectangulo = Rectangulo(punto1, punto3)
    
    # Mostrar base, altura y área del rectángulo
    print(f"La base del rectángulo es: {rectangulo.base()}")
    print(f"La altura del rectángulo es: {rectangulo.altura()}")
    print(f"El área del rectángulo es: {rectangulo.area()}")

if __name__ == "__main__":
    main()