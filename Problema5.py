class ALUMNO:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.edad = None
        self.notas = []

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Codigo: {self.codigo}")

    def setage(self, edad):
        if edad>0:
            self.edad = edad
        else: 
            raise ValueError("La edad debe de ser un número positivo")

    def setnota(self, *notas):
        if all(isinstance(nota, (int, float)) for nota in notas):
            self.notas.extend(notas)
        else:
            raise ValueError("Las notas deben de ser números válidos")
        

def main():
    while True:
        try:
            nombre = input("Ingrese el nombre del alumno: ")
            codigo = input("Ingrese el codigo de registro del alumno: ")

            ALUMNO1 = ALUMNO(nombre, codigo)

            edad = int(input("Ingrese la edad del alumno: "))
            ALUMNO1.setage(edad)

            notas = input("Ingrese las notas del alumno separadas por comas: ")
            notas = [float(nota.strip()) for nota in notas.split(',')]
            ALUMNO1.setnota(*notas)

            break

        except ValueError:
            print("Error. Ingrese las notas nuevamente")

        except Exception:
            print("Error. Ingrese los datos nuevamente")

    ALUMNO1.display()

if __name__ == "__main__":
    main()