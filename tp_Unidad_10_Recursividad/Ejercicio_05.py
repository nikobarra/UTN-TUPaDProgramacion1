# ------------------------------------------------------------
# Ejercicio 5: Palíndromo
# ------------------------------------------------------------


def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 letras, es palíndromo
    if len(palabra) <= 1:
        return True
    # Si la primera y la última letra no coinciden, no es palíndromo
    if palabra[0] != palabra[-1]:
        return False
    # Caso recursivo: verificamos el interior de la palabra
    return es_palindromo(palabra[1:-1])


print("\n" + "=" * 40)
print("Ejercicio 5: Palíndromo")
print("=" * 40)
palabra = input("Ingresá una palabra (sin tildes ni espacios): ")
if es_palindromo(palabra.lower()):
    print(f'"{palabra}" ES un palíndromo.')
else:
    print(f'"{palabra}" NO es un palíndromo.')
