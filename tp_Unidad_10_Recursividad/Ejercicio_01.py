# ------------------------------------------------------------
# Ejercicio 1: Factorial de un número
# ------------------------------------------------------------


def factorial(n):
    # Caso base: el factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n! = n * (n-1)!
    return n * factorial(n - 1)


print("=" * 40)
print("Ejercicio 1: Factorial")
print("=" * 40)
numero = int(input("Ingresá un número entero positivo: "))
for i in range(1, numero + 1):
    print(f"{i}! = {factorial(i)}")
