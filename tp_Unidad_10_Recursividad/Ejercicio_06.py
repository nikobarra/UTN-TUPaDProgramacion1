# ------------------------------------------------------------
# Ejercicio 6: Suma de dígitos
# ------------------------------------------------------------


def suma_digitos(n):
    # Caso base: si el número tiene un solo dígito, lo devolvemos
    if n < 10:
        return n
    # Caso recursivo: sumamos el último dígito y continuamos con el resto
    return (n % 10) + suma_digitos(n // 10)


print("\n" + "=" * 40)
print("Ejercicio 6: Suma de dígitos")
print("=" * 40)
numero = int(input("Ingresá un número entero positivo: "))
print(f"La suma de los dígitos de {numero} es: {suma_digitos(numero)}")
