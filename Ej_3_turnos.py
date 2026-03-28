"""
✅ Ejercicio 3 (Alta) — “Agenda de Turnos con
Nombres (sin listas)”
Contexto
Hay 2 días de atención: Lunes y Martes.
Cada día tiene cupos fijos:
• Lunes: 4 turnos
• Martes: 3 turnos
Reglas
1. Pedir nombre del operador (solo letras).
2. Menú repetitivo hasta salir:
1. Reservar turno
2. Cancelar turno (por nombre)
3. Ver agenda del día
4. Ver resumen general
5. Cerrar sistema
3. Reservar:
o Elegir día (1=Lunes, 2=Martes).
o Pedir nombre del paciente (solo letras).
o Verificar que no esté repetido en ese día (comparando con las variables
ya cargadas).
o Guardar en el primer espacio libre (ej. lunes1, lunes2…).
4. Cancelar:
o Elegir día.
o Pedir nombre del paciente (solo letras).
o Si existe, cancelar y dejar el espacio vacío ("").
5. Ver agenda del día:
o Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si
está vacío.
6. Resumen general:
o Turnos ocupados y disponibles por día.
o Día con más turnos (o empate).
Restricciones
• ❌ No listas, no diccionarios, no sets, no tuplas.
• ✅ Se permite usar "" como “vacío”.
• ✅ Validaciones con .isalpha() y .isdigit() (sin try/except).
"""

print("*--------- Agenda de Turnos UTN ---------*")

# Variables de los turnos de Lunes (4 cupos)
l1 = ""
l2 = ""
l3 = ""
l4 = ""
# Variables de los turnos de Martes (3 cupos)
m1 = ""
m2 = ""
m3 = ""

# Ingreso del operador
while True:
    operador = input("Nombre del operador: ")
    if operador.isalpha():
        break
    print("Error: El nombre solo debe contener letras.")

while True:
    print(f"\n>>> MENU AGENDA - Operador: {operador} <<<")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Resumen general")
    print("5. Cerrar sistema")

    op = input("Seleccione una opción (1-5): ")

    if not op.isdigit():
        print("Error: Debe ingresar un número.")
        continue

    op = int(op)

    if op == 1:  # RESERVAR
        dia = input("Elija día (1: Lunes / 2: Martes): ")
        if dia == "1" or dia == "2":
            while True:
                paciente = input("Nombre del paciente: ")
                if paciente.isalpha():
                    break
                print("Error: Nombre inválido.")

            if dia == "1":
                # Verificar si ya existe en Lunes
                if paciente == l1 or paciente == l2 or paciente == l3 or paciente == l4:
                    print("Error: El paciente ya tiene un turno este día.")
                # Buscar primer lugar libre
                elif l1 == "":
                    l1 = paciente
                    print("Turno 1 asignado.")
                elif l2 == "":
                    l2 = paciente
                    print("Turno 2 asignado.")
                elif l3 == "":
                    l3 = paciente
                    print("Turno 3 asignado.")
                elif l4 == "":
                    l4 = paciente
                    print("Turno 4 asignado.")
                else:
                    print("Día Lunes sin cupos disponibles.")

            else:  # Martes
                if paciente == m1 or paciente == m2 or paciente == m3:
                    print("Error: El paciente ya tiene un turno este día.")
                elif m1 == "":
                    m1 = paciente
                    print("Turno 1 asignado.")
                elif m2 == "":
                    m2 = paciente
                    print("Turno 2 asignado.")
                elif m3 == "":
                    m3 = paciente
                    print("Turno 3 asignado.")
                else:
                    print("Día Martes sin cupos disponibles.")
        else:
            print("Día incorrecto.")

    elif op == 2:  # CANCELAR
        dia = input("Elija día (1: Lunes / 2: Martes): ")
        paciente = input("Nombre del paciente a cancelar: ")

        encontrado = False
        if dia == "1":
            if l1 == paciente:
                l1 = ""
                encontrado = True
            elif l2 == paciente:
                l2 = ""
                encontrado = True
            elif l3 == paciente:
                l3 = ""
                encontrado = True
            elif l4 == paciente:
                l4 = ""
                encontrado = True
        elif dia == "2":
            if m1 == paciente:
                m1 = ""
                encontrado = True
            elif m2 == paciente:
                m2 = ""
                encontrado = True
            elif m3 == paciente:
                m3 = ""
                encontrado = True

        if encontrado:
            print(f"Turno de {paciente} cancelado con éxito.")
        else:
            print("No se encontró al paciente en ese día.")

    elif op == 3:  # VER AGENDA
        dia = input("Ver día (1: Lunes / 2: Martes): ")
        if dia == "1":
            print(f"Turno 1: {l1 if l1 != '' else '(libre)'}")
            print(f"Turno 2: {l2 if l2 != '' else '(libre)'}")
            print(f"Turno 3: {l3 if l3 != '' else '(libre)'}")
            print(f"Turno 4: {l4 if l4 != '' else '(libre)'}")
        elif dia == "2":
            print(f"Turno 1: {m1 if m1 != '' else '(libre)'}")
            print(f"Turno 2: {m2 if m2 != '' else '(libre)'}")
            print(f"Turno 3: {m3 if m3 != '' else '(libre)'}")

    elif op == 4:  # RESUMEN GENERAL
        # Contar ocupados Lunes
        ocu_l = 0
        if l1 != "":
            ocu_l += 1
        if l2 != "":
            ocu_l += 1
        if l3 != "":
            ocu_l += 1
        if l4 != "":
            ocu_l += 1

        # Contar ocupados Martes
        ocu_m = 0
        if m1 != "":
            ocu_m += 1
        if m2 != "":
            ocu_m += 1
        if m3 != "":
            ocu_m += 1

        print(f"Lunes: {ocu_l} ocupados / {4 - ocu_l} disponibles.")
        print(f"Martes: {ocu_m} ocupados / {3 - ocu_m} disponibles.")

        if ocu_l > ocu_m:
            print("Día con más turnos: Lunes")
        elif ocu_m > ocu_l:
            print("Día con más turnos: Martes")
        else:
            print("Empate en cantidad de turnos.")

    elif op == 5:
        print(f"Cerrando sistema. ¡Hasta luego {operador}!")
        break

    else:
        print("Opción fuera de rango.")
