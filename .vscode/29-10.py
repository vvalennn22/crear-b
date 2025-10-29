def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def main():
    try:
        n = int(input("Ingrese cantidad de términos (n): ").strip())
    except Exception:
        print("Entrada inválida.")
        return
    if n <= 0:
        print("n debe ser mayor que 0.")
        return
    print("Secuencia de Fibonacci:")
    print(*fibonacci(n))

if __name__ == "__main__":
    main()