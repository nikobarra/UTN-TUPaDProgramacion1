# TP Unidad 10: Recursividad 🌀

Este módulo contiene la resolución de una serie de ejercicios prácticos enfocados en el aprendizaje y aplicación del paradigma de **Recursividad** en Python.

La recursividad es una técnica donde una función se llama a sí misma para resolver subproblemas más pequeños del problema original, hasta alcanzar un **caso base**.

---

## 🧠 Conceptos Aplicados
- **Caso Base:** La condición que detiene la recursión.
- **Caso Recursivo:** La llamada a la función con un argumento reducido.
- **Pila de Llamadas (Stack):** Gestión de la memoria durante la ejecución.

---

## 📋 Lista de Ejercicios

A continuación se detallan los algoritmos implementados:

| Ejercicio | Título | Lógica Recursiva |
| :--- | :--- | :--- |
| **01** | **Factorial** | `n * factorial(n-1)`. Caso base: `n` es 0 o 1. |
| **02** | **Fibonacci** | `F(n-1) + F(n-2)`. Casos base: posiciones 0 y 1. |
| **03** | **Potencia** | `base * potencia(base, exp-1)`. Caso base: `exp == 0`. |
| **04** | **Decimal a Binario** | `n // 2` + resto `n % 2`. Caso base: `n < 2`. |
| **05** | **Palíndromo** | Compara extremos y recurre con `palabra[1:-1]`. |
| **06** | **Suma de Dígitos** | `n % 10 + suma(n // 10)`. Caso base: `n < 10`. |
| **07** | **Pirámide de Bloques** | `n + contar(n-1)` (Suma triangular). Caso base: `n == 1`. |
| **08** | **Contar Dígito** | Verifica `n % 10` y recurre con `n // 10`. |

---

## 🚀 Ejecución

Para probar cualquiera de los ejercicios, ejecuta el archivo correspondiente desde la terminal:

```bash
# Ejemplo para ejecutar el ejercicio de Factorial
python Ejercicio_01.py
```

---
*Este trabajo práctico forma parte de la formación en Programación 1 - UTN TUPAD.*
