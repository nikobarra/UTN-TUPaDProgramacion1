# ------------------------------------------------------------
# Ejercicio 3: Potencia de un número
# ------------------------------------------------------------


def potencia(base, exponente):
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    # Caso recursivo: n^m = n * n^(m-1)
    return base * potencia(base, exponente - 1)


print("\n" + "=" * 40)
print("Ejercicio 3: Potencia")
print("=" * 40)
base = int(input("Ingresá la base: "))
exp = int(input("Ingresá el exponente: "))
resultado = potencia(base, exp)
print(f"{base} elevado a {exp} = {resultado}")
