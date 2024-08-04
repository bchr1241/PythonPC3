def main():
    while True:
        try:
            notas = input("Introduce una serie de calificaciones separadas por comas (,): ")
            notas_lista = notas.split(',')
            notas_int = [round(float(nota.strip())) for nota in notas_lista]
            print("Las calificaciones son: ", notas_int)

            break

        except ValueError:
            print("Favor de introducir solo números separados por comas")
        except Exception:
            print("Error inesperado. Favor de introducir nuevamente la función correctamente")

if __name__ == "__main__":
    main()
