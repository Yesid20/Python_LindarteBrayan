def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def main():
    print("¡Bienvenido al Generador de Secuencia de Fibonacci!")
    print("La Secuencia de Fibonacci comienza con 0 y 1, y cada término subsiguiente es la suma de los dos términos anteriores.")
    
    while True:
        try:
            n = int(input("\nIngrese el valor de 'n' para generar la secuencia (0 para salir): "))
            
            if n < 0:
                print("Por favor, ingrese un valor no negativo.")
            elif n == 0:
                print("¡Hasta luego!")
                break
            
            fib_result = fibonacci_sequence(n)
            print(f"\nSecuencia de Fibonacci hasta el término {n}: {fib_result}")
            
        except ValueError:
            print("Por favor, ingrese un valor entero válido.")

if __name__ == "__main__":
    main()
