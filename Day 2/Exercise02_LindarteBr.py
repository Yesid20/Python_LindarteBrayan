import random

def jugar_adivinanza():
    numero_secreto = random.randint(1, 100)
    max_intentos = 10

    print("¡Bienvenido al Juego de Adivinanza del Número Secreto!")
    print(f"Adivina el número secreto entre 1 y 100. Tienes un total de {max_intentos} intentos.")

    for intento_actual in range(1, max_intentos + 1):
        try:
            suposicion = int(input(f"\nIntento {intento_actual}: Ingresa tu suposición: "))

            if 1 <= suposicion <= 100:
                if suposicion == numero_secreto:
                    print(f"\n¡Felicidades! Adivinaste el número secreto {numero_secreto} en {intento_actual} intentos.")
                    break
                elif suposicion < numero_secreto:
                    print("El número secreto es mayor. ¡Sigue intentando!")
                else:
                    print("El número secreto es menor. ¡Sigue intentando!")
            else:
                print("Por favor, ingresa un número dentro del rango permitido (1-100).")

        except ValueError:
            print("Por favor, ingresa un número entero válido.")

    else:
        print(f"\nLo siento, has agotado tus {max_intentos} intentos. El número secreto era {numero_secreto}.")

if __name__ == "__main__":
    jugar_adivinanza()
