# ------------------------------------------------------------
# Ejercicio 8: Contar apariciones de un dígito
# ------------------------------------------------------------


def contar_digito(numero, digito):
    # Caso base: si el número tiene un solo dígito
    if numero < 10:
        if numero == digito:
            return 1
        else:
            return 0
    # Verificamos si el último dígito coincide
    if numero % 10 == digito:
        coincide = 1
    else:
        coincide = 0
    # Caso recursivo: seguimos con el resto del número
    return coincide + contar_digito(numero // 10, digito)


print("\n" + "=" * 40)
print("Ejercicio 8: Contar dígito")
print("=" * 40)
numero = int(input("Ingresá un número entero positivo: "))
digito = int(input("Ingresá el dígito que querés buscar (0-9): "))
veces = contar_digito(numero, digito)
print(f"El dígito {digito} aparece {veces} vez/veces en {numero}.")
