# No agrego el enunciado para no hacer demasiado extenso el codigo en general

# Variables iniciales fijas
energia = 100
tiempo = 12
cerraduras = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0  # Para la regla anti-spam

while True:
    agent = input("Nombre del agente: ")
    if agent.isalpha():
        break
    print("Solo letras.")

while energia > 0 and tiempo > 0 and cerraduras < 3 and not alarma:
    print(f"\n--- ESTADO: E:{energia} | T:{tiempo} | C:{cerraduras} ---")
    print("1. Forzar / 2. Hackear / 3. Descansar")

    op = input("Acción: ")
    if not op.isdigit():
        continue
    op = int(op)

    if op == 1:  # FORZAR
        racha_forzar += 1
        energia -= 20
        tiempo -= 2

        if racha_forzar >= 3:
            print("¡La cerradura se trabó! ALARMA ACTIVADA.")
            alarma = True
        else:
            if energia < 40:
                riesgo = input("Riesgo de alarma. Elija 1-3: ")
                if riesgo == "3":
                    alarma = True

            if not alarma:
                cerraduras += 1
                print("¡Cerradura abierta!")

    elif op == 2:  # HACKEAR
        racha_forzar = 0
        energia -= 10
        tiempo -= 3
        print("Hackeando...")
        for _ in range(4):
            codigo_parcial += "A"
            print(f"Progreso: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras < 3:
            cerraduras += 1
            print("¡Hackeo exitoso! Cerradura abierta.")

    elif op == 3:  # DESCANSAR
        racha_forzar = 0
        tiempo -= 1
        recupera = 15
        if alarma:
            recupera -= 10
        energia = min(100, energia + recupera)
        print(f"Energía recuperada. Total: {energia}")

    # Chequeo de bloqueo por alarma
    if alarma and tiempo <= 3 and cerraduras < 3:
        print("SISTEMA BLOQUEADO.")
        break

# Finalización
if cerraduras == 3:
    print("¡VICTORIA! Bóveda abierta.")
else:
    print("DERROTA. Misión fallida.")
