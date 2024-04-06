# Ejercicio 1
def cambia(num):
    """
    Cambia los dígitos uno por ceros
    """
    if isinstance(num, int) and num > 0:
        return cambia_aux(num)
    else:
        return "Error"


def cambia_aux(num):
    if not num:
        return 0

    if num % 10 == 1:
        return 10 * cambia_aux(num // 10)
    else:
        return num % 10 + 10 * cambia_aux * (num // 10)


# Ejercicio 2
def compuesto(num):
    """
    Averigua si el número es compuesto. Esta es la manera que hice en el quiz, pero la manera
    eficiente está más abajo
    """
    if isinstance(num, int) and num > 1:
        return compuesto_aux(num, num - 1)
    else:
        return "Error"


def compuesto_aux(num, anterior):
    if anterior == 1:
        return False
    if num % anterior == 0:
        return True
    else:
        return compuesto_aux(num, anterior - 1)

# Ejercicio 2 eficiente
def compuesto_2(num):
    if isinstance(num, int) and num > 1:
        return compuesto_2_aux(num, 0)
    else:
        return "Error"


def compuesto_2_aux(num, index):
    if index == num // 2:
        return False

    if num % index == 0:
        return True
    else:
        return compuesto_2_aux(num, index + 1)
