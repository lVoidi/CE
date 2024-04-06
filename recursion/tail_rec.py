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
        return restard_aux(dig, num // 10, result, exp+1)
    else:
        return restard_aux(dig, num // 10, result + dif * (10**exp), exp + 1)


