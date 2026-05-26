# ------------------------------------------------------------
# Ejercicio 7: Pirámide de bloques
# ------------------------------------------------------------


def contar_bloques(n):
    # Caso base: si hay un solo nivel, hay un solo bloque
    if n == 1:
        return 1
    # Caso recursivo: sumamos el nivel actual con los niveles anteriores
    return n + contar_bloques(n - 1)


print("\n" + "=" * 40)
print("Ejercicio 7: Pirámide de bloques")
print("=" * 40)
niveles = int(input("¿Cuántos bloques hay en la base de la pirámide? "))
total = contar_bloques(niveles)
print(
    f"Para una pirámide con base de {niveles} bloques se necesitan {total} bloques en total."
)
