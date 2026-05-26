# ------------------------------------------------------------
# Ejercicio 2: Serie de Fibonacci
# ------------------------------------------------------------


def fibonacci(n):
    # Caso base: posición 0 y 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Caso recursivo: F(n) = F(n-1) + F(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)


print("\n" + "=" * 40)
print("Ejercicio 2: Serie de Fibonacci")
print("=" * 40)
posicion = int(input("¿Hasta qué posición querés ver la serie? "))
print("Serie de Fibonacci:")
for i in range(posicion + 1):
    print(f"  Posición {i}: {fibonacci(i)}")
