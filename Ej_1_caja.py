"""
Ejercicio 1— “Caja del Kiosco”
Objetivo: Simular una compra con validaciones y cálculo de total.
Requisitos
1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while).
2. Pedir cantidad de productos a comprar (número entero positivo, validar con
.isdigit() en while).
3. Por cada producto (usar for):
o Pedir precio (entero, validar .isdigit()).
o Pedir si tiene descuento S/N (validar con while, aceptar s o n en
cualquier mayuscula/minuscula).
o Si tiene descuento: aplicar 10% al precio de ese producto.
4. Al final mostrar:
o Total sin descuentos
o Total con descuentos
o Ahorro total
o Promedio por producto (usar float y formatear con :.2f, ejem:
x = 3.14159
print(f"{x:.2f}"))
Validaciones obligatorias
• Sin try/except.
• No aceptar vacío en nombre (si queda vacío, es error).
• Cantidad > 0 (si ingresa 0, volver a pedir).
"""

print("*--------- Caja del Kiosco ---------*")

# 1. Pedir nombre del cliente (validar que no sea vacío y solo letras)
while True:
    name = input("Ingrese el nombre del cliente: ")
    if name.isalpha() and name != "":
        break
    print("Error: El nombre no puede estar vacío y solo debe contener letras.")

# 2. Pedir cantidad de productos (entero positivo)
while True:
    quantity_input = input("Ingrese la cantidad de productos a comprar: ")
    if quantity_input.isdigit():
        quantity = int(quantity_input)
        if quantity > 0:
            break
    print("Error: Ingrese un número entero mayor a 0.")

sum_not_discount = 0
sum_with_discount = 0
DISCOUNT_RATE = 0.10

# 3. Ciclo por cada producto
for i in range(1, quantity + 1):
    print(f"\n--- Producto {i} ---")

    # Validar precio
    while True:
        price_input = input(f"Ingrese el precio del producto {i}: ")
        if price_input.isdigit():
            price = int(price_input)
            break
        print("Error: El precio debe ser un número entero.")

    # Validar si tiene descuento
    while True:
        has_discount = input("¿Tiene descuento? (S/N): ").lower()
        if has_discount == "s" or has_discount == "n":
            break
        print("Error: Ingrese 'S' para sí o 'N' para no.")

    # Acumular totales
    sum_not_discount = sum_not_discount + price

    if has_discount == "s":
        # Aplicamos el 10% de descuento
        precio_final = price * (1 - DISCOUNT_RATE)
        sum_with_discount = sum_with_discount + precio_final
    else:
        sum_with_discount = sum_with_discount + price

# 4. Mostrar resultados finales con f-strings
ahorro = sum_not_discount - sum_with_discount
promedio = sum_with_discount / quantity

print(
    f"""
---------- Ticket de salida ----------
Cliente: {name}
Total sin descuentos:  ${sum_not_discount}
Total con descuentos:  ${sum_with_discount:.2f}
Ahorro total:          ${ahorro:.2f}
Promedio por producto: ${promedio:.2f}
--------------------------------------
"""
)
