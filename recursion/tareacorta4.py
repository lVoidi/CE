# TEC - Escuela de Ingeniería en Computadores
# CE1101 - Introducción a la programación
# Tarea corta 4a - Recursividad de pila

"""
-==Recursividad==-
La recursividad, en la matemática, es un tipo de proceso basado en su propia definición.
El ejemplo más conocido de recursividad en la matemática es el factorial de un número, la cual se define como
n! = n*(n-1)!

En la programación, una función recursiva es aquella que se llama a sí misma con el fin de hacer un ciclo eficiente 
y rápido. 
"""

"""
-==Condición de terminación o caso base==-
Tome una función recursiva, sea, factorial(x). 
El factorial de un número está definido de la siguiente manera:
n! = {
    1           si, n < 2
    n*(n-1)!    si, n > 1
}
Donde n es un número entero positivo

en python el código se representaría de la siguiente manera:

def factorial(n):
    if num < 2:
        return 1
    else:
        return n * factorial(n-1)
        
El caso base sería el que se encarga de evitar que la función recursiva corra indefinidamente. En el caso de un factorial,
no tendría sentido multiplicar por 1 o por 0, por eso la función termina cuando n < 2. Esta sería la condición de terminación.
"""

"""
-==¿Por qué una función recursiva podría caer en un ciclo infinito?==-
Tomemos el caso del factorial. Imaginemos que la función recursiva no tiene un caso una condicición de terminación

def factorial(n):
    return n * factorial(n-1)

Este es el caso de una función recursiva infinita. Tome n = 5 y llamemos a la función factorial.
factorial(5) = 5*4*3*2*1*0*-1*-2*-3...
Esta función no tiene sentido lógico ni matemático, pues toda la multiplicación sería infinita, pues la función
seguiría llamandose infinitamente. En el caso de python, no se llama infinitamente la función pues existe RecursionError,
pero en otros lenguajes si se puede caer en un bucle infinito. 

Tomemos el caso de bash y la fork bomb.
:(){:|:&}

Este es un caso de una función que no solo se llama recursivamente por la infinidad, sino que se duplica el llamado
cada vez que se llama a sí misma, y terminaría consumiendo toda la memoria del computador. 
"""

# Parte 1
def hay_par(num):
    if isinstance(num, int):
        return num % 2 == 0 or hay_par_aux(abs(num))
    else:
        return 403
    
def hay_par_aux(num):
    # Entrada: el numero 
    # Salida: True o False, dependiendo si el numero tiene algún par o no
    # Restricciones: Número válido entero
    current_digit = num % 10 
    
    if not num: # caso base 1 
        return False
    
    if current_digit % 2 == 0: # caso base 2
        return True 
    
    else:
        return hay_par_aux(num // 10)

print(hay_par(2043))

# Parte 2: este es el código corregido y con entradas, salidas y restricciones
# Esta función suma todos los dígitos distintos a uno
def q(n):
    if isinstance(n, int):
        return q_aux(abs(n))
    else:
        return "Error"

def q_aux(n):
    # Entrada: numero
    # Salida: La suma de todos los dígitos distintos de uno 
    # Restricciones: Numero entero válido
    if n == 0: # caso base
        return 0
    elif (n % 10 == 1):
        return q_aux(n // 10)
    else:
        return n % 10 + q_aux(n // 10)

# Parte 3
def iguales(num):
    num = abs(num)
    if isinstance(num, int):
        return iguales_aux(num, num % 10)
    else:
        return 403
    
def iguales_aux(num, last_digit):
    # Entrada: numero en la iteración actual y el último dígito del numero completo.
    # En este caso el usuario solo tiene que digitar el número en dado caso ** last_digit es un auxiliar
    # Salida: True o False, dependiendo si el último dígito es igual al primero o no
    # Restricciones: Número entero positivo
    current_digit = num % 10
    if not num // 10: # caso base
        return current_digit == last_digit
    
    return iguales_aux(num // 10, last_digit)

# Parte 4
def num_append(num1, num2):
    # Entrada: Los dos números a juntar
    # Salida: Los dos números juntos
    # Restricciones: Números enteros válidos
    if isinstance(num1, int) and isinstance(num2, int):
        return num1*(10**num_length(num2)) + num2
    else:
        return -1

def num_length(num):
    if not num // 10: # caso base
        return 1
    return 1 + num_length(num // 10)

# Parte 5
def revise_num(num):
    if isinstance(num, int):
        return revise_num_aux(abs(num), 0, 0)

def revise_num_aux(num, par, impar):
    # Entrada: el número a revisar, cantidad de pares e impares inicial 
    # En este caso el usuario solo tiene que digitar el número en dado caso * Par e impar son auxiliares
    # Salida: Una tupla con la cantidad de dígitos pares e impares
    # Restricciones: Número válido entero
    current_digit = num % 10 
    if not num: # caso base
        return (par, impar)   
    if current_digit % 2 == 0:
        return revise_num_aux(num // 10, par + 1, impar)
    return revise_num_aux(num // 10, par, impar + 1)

# Parte 6
def cuente_ceros(num):
    if isinstance(num, int):
        return 1 if not num else cuente_ceros_aux(abs(num))
    
def cuente_ceros_aux(num):
    # Entrada: número para contar sus ceros
    # Salida: La cantidad de ceros del número
    # Restricciones: Número entero positivo
    current_digit = num % 10
    if num == 0: # caso base
        return 0
    if current_digit == 0:
        return 1 + cuente_ceros_aux(num // 10)
    else:
        return cuente_ceros_aux(num // 10)

# Parte 7
def forme1(num):
    if isinstance(num, int):
        return forme1_aux(abs(num))

def forme1_aux(num):
    # Entrada: el numero para analizar
    # Salida: La combinación de todos los unos
    # Restricciones: 
    current_digit = num % 10
    
    if num == 0: # caso base
        return 0
    
    if current_digit == 1:
        return 1 + 10*forme1_aux(num // 10)
    else:
        return forme1_aux(num // 10)


# Parte 8
def forme_parimpar(num):
    # Entrada: El número a analizar
    # Salida: Una tupla con los numeros pares e impares juntos
    # Restricciones: los números deben ser enteros válidos
    if isinstance(num, int):
        return forme_parimpar_aux(abs(num))

def juntar_pares(num):
    if not num: # caso base
        return 0
    if (num % 10) % 2 == 0:
        return num % 10 + 10 * juntar_pares(num // 10)
    return juntar_pares(num // 10)

def juntar_impares(num):
    if not num: # caso base
        return 0
    if (num % 10) % 2 != 0:
        return num % 10 + 10 * juntar_impares(num // 10)
    return juntar_impares(num // 10)

def forme_parimpar_aux(num):
    return (juntar_pares(num), juntar_impares(num))
    
    
# Parte 9
# La función num_length ya la definí en la linea 130, la estoy
# reutilizando para no reescribirla
def invierta(num):
    if isinstance(num, int):
        return invierta_aux(num, num_length(num)-1)

def invierta_aux(num, exp):
    # Entrada: El número a invertir y el exponente actual
    # Salida: El número invertido
    # Restricciones: los números deben ser enteros válidos
    current_digit = num % 10
    if not num: # caso base
        return 0
    
    return current_digit*(10**exp) + invierta_aux(num // 10, exp - 1)

# Parte 10
def multi(num1, num2):
    if isinstance(num1, (int, float)) and isinstance(num2, int):
        return multi_aux(abs(num1), abs(num2))
    return "Error: El segundo número solo puede ser entero"

def multi_aux(num1, num2):
    # Entrada: El número float o int que va a ser multiplicado,
    # num2 numero entero que sea la cantidad de veces que se va
    # a sumar
    # Salida: El número multiplicado
    # Restricciones: El primer numero puede ser int o float,
    # y el segundo solo puede ser int
    if not num2: # caso base
        return 0
    
    return num1 + multi_aux(num1, num2-1)

def a(k):
    if k == 1:
        return 1
    if k >= 2:
        return 2*a(k-1) + k
    else:
        return k

print(a(3))