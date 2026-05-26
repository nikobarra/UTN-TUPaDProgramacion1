# No agrego el enunciado para no hacer demasiado extenso el codigo en general

print("=== BIENVENIDO A LA ARENA ===")

while True:
    nombre = input("Nombre del Gladiador: ")
    if nombre.isalpha():
        break
    print("Error: Solo se permiten letras.")

hp_jugador = 100
hp_enemigo = 100
pociones = 3
ataque_base = 15
ataque_enemigo = 12

while hp_jugador > 0 and hp_enemigo > 0:
    print(
        f"\n{nombre} (HP: {hp_jugador}) vs Enemigo (HP: {hp_enemigo}) | Pociones: {pociones}"
    )
    print("1. Ataque Pesado / 2. Ráfaga Veloz / 3. Curar")

    op = input("Opción: ")
    if not op.isdigit() or op not in ["1", "2", "3"]:
        print("Error: Ingrese un número válido (1-3).")
        continue

    # TURNO JUGADOR
    if op == "1":
        danio = float(ataque_base)
        if hp_enemigo < 20:
            danio = danio * 1.5
            print("¡GOLPE CRÍTICO!")
        hp_enemigo -= int(danio)
        print(f"Atacaste por {danio} puntos.")

    elif op == "2":
        print(">> ¡Inicias ráfaga!")
        for _ in range(3):
            hp_enemigo -= 5
            print("> Golpe conectado por 5 de daño.")

    elif op == "3":
        if pociones > 0:
            hp_jugador += 30
            pociones -= 1
            print("Te has curado +30 HP.")
        else:
            print("¡No quedan pociones! Pierdes el turno.")

    # TURNO ENEMIGO (si sigue vivo)
    if hp_enemigo > 0:
        hp_jugador -= ataque_enemigo
        print(f"¡El enemigo te atacó por {ataque_enemigo} puntos!")

# Resultado final
if hp_jugador > 0:
    print(f"\n¡VICTORIA! {nombre} ha ganado.")
else:
    print("\nDERROTA. Has caído en combate.")
