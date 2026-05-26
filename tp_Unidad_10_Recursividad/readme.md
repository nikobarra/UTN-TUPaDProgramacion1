Ej 1 – Factorial: caso base n == 0 o 1 devuelve 1; caso recursivo multiplica n \* factorial(n-1).
Ej 2 – Fibonacci: casos base para posición 0 y 1; el resto suma los dos anteriores F(n-1) + F(n-2).
Ej 3 – Potencia: caso base exponente 0 devuelve 1; caso recursivo multiplica base \* potencia(base, exp-1).
Ej 4 – Decimal a binario: caso base cuando n es 0 o 1; caso recursivo llama con n // 2 y concatena el resto n % 2 al final.
Ej 5 – Palíndromo: caso base cadena de 0 o 1 letras; compara primera y última letra, y llama recursivamente con el interior palabra[1:-1].
Ej 6 – Suma de dígitos: caso base número menor a 10; extrae el último dígito con % 10 y llama con // 10.
Ej 7 – Pirámide de bloques: caso base n == 1; caso recursivo suma n + contar_bloques(n-1). Es esencialmente la suma triangular.
