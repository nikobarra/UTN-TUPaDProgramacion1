📘 TP Integrador – Programación 1

Repetitivas, Condicionales y Secuenciales

📌 Descripción

Este repositorio contiene la resolución del Trabajo Práctico Integrador de la materia Programación 1, donde se aplican estructuras fundamentales de programación:

Secuenciales
Condicionales (if / elif / else)
Repetitivas (while / for)

Además, se hace foco en la validación estricta de datos utilizando métodos como:

.isalpha() → validación de texto
.isdigit() → validación numérica

❌ No se utiliza try/except
✅ Se prioriza la lógica estructurada

🧩 Ejercicios
🧮 Ejercicio 1 – Caja del Kiosco

Simula una compra con múltiples productos.

Funcionalidades:

Validación del nombre del cliente
Ingreso de cantidad de productos
Carga de precios con descuento opcional
Cálculo de:
Total sin descuento
Total con descuento
Ahorro total
Promedio por producto

Conceptos aplicados:

while para validaciones
for para iterar productos
Cálculos con float y formateo
🔐 Ejercicio 2 – Acceso al Campus

Sistema de login con menú interactivo.

Funcionalidades:

Login con máximo 3 intentos
Bloqueo de cuenta
Menú repetitivo con opciones:
Estado de inscripción
Cambio de clave
Mensaje motivacional
Salir

Validaciones:

Entrada numérica correcta
Rango de opciones
Clave con mínimo 6 caracteres
📅 Ejercicio 3 – Agenda de Turnos (Sin estructuras complejas)

Sistema de gestión de turnos para dos días.

Restricción clave:
❌ No uso de listas, diccionarios, tuplas ni sets

Funcionalidades:

Reservar turno
Cancelar turno
Ver agenda diaria
Resumen general

Lógica:

Uso de variables individuales (ej: lunes1, martes2)
Control de espacios vacíos con ""
🧠 Ejercicio 4 – Escape Room: La Bóveda

Juego interactivo basado en decisiones.

Objetivo:
Abrir 3 cerraduras antes de quedarse sin energía o tiempo.

Mecánicas:

Energía y tiempo limitados
Acciones:
Forzar cerradura
Hackear panel
Descansar
Sistema de alarma
Regla anti-spam (evita abuso de acciones)

Conceptos:

Estados del sistema
Condiciones múltiples
Uso de len() y acumuladores
⚔️ Ejercicio 5 – La Arena del Gladiador

Simulador de combate por turnos.

Características:

Jugador vs Enemigo
Sistema de turnos
Acciones:
Ataque pesado (con crítico)
Ráfaga veloz (for)
Curar

Tipos de datos utilizados:

string → nombre
int → vida, daño, pociones
float → daño crítico
boolean → control de turnos

Finalización:

Victoria o derrota según vida restante
🛠️ Tecnologías utilizadas
Python 🐍
Consola / CLI
Programación estructurada
🎯 Objetivos de aprendizaje

✔ Validar entradas correctamente
✔ Aplicar estructuras de control
✔ Diseñar lógica sin estructuras avanzadas
✔ Simular problemas reales
✔ Desarrollar pensamiento algorítmico

🚀 Cómo ejecutar
Clonar el repositorio:
git clone https://github.com/nikobarra/UTN-TUPaDProgramacion1
Ejecutar el archivo deseado:
python ejercicio1.py
📎 Notas
Todos los ejercicios siguen las consignas originales del TP
Se respeta la restricción de no usar manejo de excepciones
Código orientado a principiantes
