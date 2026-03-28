"""
Ejercicio 2 — “Acceso al Campus y Menú Seguro”
Objetivo: Login con intentos + menú de acciones con validación estricta.
Requisitos
1. Definir credenciales fijas en el código:
o usuario correcto: "alumno"
o clave correcta: "python123"
2. Permitir máximo 3 intentos para ingresar usuario y clave.
3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar.
4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir:
1. Ver estado de inscripción (mostrar “Inscripto”)
2. Cambiar clave (pedir nueva clave y confirmación; deben
coincidir)
3. Mostrar mensaje motivacional (1 frase)
4. Salir
5. Validación del menú:
o Debe ser número (.isdigit())
o Debe estar entre 1 y 4
Cambio de clave
• La nueva clave debe tener mínimo 6 caracteres (validar con len()), si no,
rechazar.
"""

print("*--------- Acceso al Campus ---------*")

# 1. Credenciales fijas
USER_CORRECT = "alumno"
PASS_CORRECT = "python123"
intentos = 0
acceso_concedido = False

# 2 y 3. Bucle de login (máximo 3 intentos)
while intentos < 3:
    intentos = intentos + 1
    print(f"\nIntento {intentos}/3")
    user_input = input("Usuario: ")
    pass_input = input("Clave: ")

    if user_input == USER_CORRECT and pass_input == PASS_CORRECT:
        print("Acceso concedido.")
        acceso_concedido = True
        break
    else:
        if intentos < 3:
            print("Error: credenciales inválidas.")
        else:
            print("Cuenta bloqueada.")

# 4. Menú repetitivo (si el acceso fue exitoso)
while acceso_concedido:
    print("\n--- MENÚ DE ACCIONES ---")
    print("1. Ver estado de inscripción")
    print("2. Cambiar clave")
    print("3. Mostrar mensaje motivacional")
    print("4. Salir")

    opcion = input("Opción: ")

    # 5. Validación del menú
    if opcion.isdigit():
        opcion = int(opcion)

        if opcion == 1:
            print("Estado: Inscripto")

        elif opcion == 2:
            nueva_clave = input("Nueva clave: ")
            # Validación de longitud (mínimo 6)
            if len(nueva_clave) >= 6:
                confirmacion = input("Confirme su nueva clave: ")
                if nueva_clave == confirmacion:
                    PASS_CORRECT = nueva_clave
                    print("Clave cambiada con éxito.")
                else:
                    print("Error: Las claves no coinciden.")
            else:
                print("Error: La clave debe tener mínimo 6 caracteres.")

        elif opcion == 3:
            print(
                "Mensaje: 'El éxito es la suma de pequeños esfuerzos repetidos día tras día.'"
            )

        elif opcion == 4:
            print("Saliendo del sistema...")
            acceso_concedido = False  # Rompe el ciclo del menú

        else:
            print("Error: opción fuera de rango (1-4).")
    else:
        print("Error: ingrese un número válido.")
