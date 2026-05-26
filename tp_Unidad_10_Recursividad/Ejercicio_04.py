# ------------------------------------------------------------
# Ejercicio 4: Conversión de decimal a binario
# ------------------------------------------------------------


def decimal_a_binario(n):
    # Caso base: si el número es 0 o 1, devolvemos directamente su cadena
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    # Caso recursivo: tomamos el resto y lo agregamos al resultado anterior
    return decimal_a_binario(n // 2) + str(n % 2)


print("\n" + "=" * 40)
print("Ejercicio 4: Decimal a Binario")
print("=" * 40)
numero = int(input("Ingresá un número entero positivo: "))
print(f"{numero} en binario es: {decimal_a_binario(numero)}")
