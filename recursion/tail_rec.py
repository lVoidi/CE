# Ejercicio 1. Obtener dígito menor
def menor(num):
    if isinstance(num, int):
        return menor_aux(num, num % 10)
    else:
        return "Error"


def menor_aux(num, menor):
    if not num:
        return menor
    if num % 10 < menor:
        return menor_aux(num // 10, num % 10)
    else:
        return menor_aux(num // 10, menor)


# Ejercicio 2. Quitar el dígito dig del número num
def restard(dig, num):
    if isinstance(dig, int) and isinstance(num, int) and 0 <= dig <= 9:
        return restard_aux(dig, num, 0, 0)
    else:
        return "Error"


def restard_aux(dig, num, result, exp):
    if not num:
        return result
    dif = num % 10 - dig
    if dif <= 0:
        return restard_aux(dig, num // 10, result, exp + 1)
    else:
        return restard_aux(dig, num // 10, result + dif * (10**exp), exp + 1)


# Ejercicio 3. Cambiar un dígito divisible entre 4 por un cero (1488 -> 1000)
def cambia(num):
    if isinstance(num, int):
        return cambia_aux(num, 0, 0)
    else:
        return "Error"


def cambia_aux(num, result, exp):
    if not num:
        return result

    if (num % 10) % 4 == 0:
        return cambia_aux(num // 10, result, exp + 1)
    else:
        return cambia_aux(num // 10, result + (num % 10) * (10**exp), exp + 1)


# Ejercicio 4. Devolver una tupla (x, y) tal que x representan los dígitos mayores a dig, y y los dígitos menores a dig en num
def divida(dig, num):
    if isinstance(dig, int) and isinstance(num, int) and 0 <= dig <= 9:
        return divida_aux(dig, num, 0, 0, 0, 0)
    else:
        return "Error"


def divida_aux(dig, num, menores, mayores, exp_menores, exp_mayores):
    if not num:
        return (mayores, menores)

    current_digit = num % 10
    mult_menores = 10**exp_menores
    mult_mayores = 10**exp_mayores
    if current_digit >= dig:
        return divida_aux(
            dig,
            num // 10,
            menores,
            mayores + mult_mayores * current_digit,
            exp_menores,
            exp_mayores + 1,
        )
    if current_digit < dig:
        return divida_aux(
            dig,
            num // 10,
            menores + mult_menores * current_digit,
            mayores,
            exp_menores + 1,
            exp_mayores,
        )

# Ejercicio 5. Comprobar si todos los digitos de num son divisibles entre dig
# La magia aquí era hacerlo con recursividad de cola y no con recursividad simple
def todos_div(num, dig):
    if isinstance(num, int) and isinstance(dig, int) and 0 <= dig <= 9:
        return todos_div_aux(num, dig, True)
    else:
        return "Error"

def todos_div_aux(num, dig, result):
    if not num:
        return result
    
    divisible = (num % 10) % dig == 0
    
    return todos_div_aux(num//10, dig, result and divisible)

print(todos_div(46148, 2))