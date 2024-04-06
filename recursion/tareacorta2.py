# TEC - Escuela de Ingeniería en Computadores
# CE1101 - Introducción a la Programación. Grupo 1
# Tarea corta 2


# 1. La secuencia tiene un 6 en cada termino par
# y en los numeros impares se va a aumentando en 5
# empezando desde 4
def serie(n):
    # e: la cantidad de términos a generar
    # s: la lista con la secuencia
    # r: numero entero positivo
    if isinstance(n, int) and n > 0:
        return serie_aux(1, [], 4, n)
    else:
        return "Error"


def serie_aux(n, l, odd_term, end):
    if n - 1 == end:
        return l

    if n % 2 == 0:
        return serie_aux(n + 1, l + [6], odd_term, end)
    else:
        return serie_aux(n + 1, l + [odd_term], odd_term + 5, end)


# 2.
def intersec(num1, num2):
    # e: los 2 numeros
    # s: los numeros de num1 contenidos por num2
    # r: numeros enteros positivos
    num1 = abs(num1)
    num2 = abs(num2)
    if isinstance(num1, int) and isinstance(num2, int):
        return intersec_aux(num_as_list(num1), num_as_list(num2), 0, 0)
    else:
        return "Error"


def num_as_list(num):
    if num < 10:
        return [num]
    else:
        return num_as_list(num // 10) + [num % 10]


def digit_in_list(digit, lst):
    if not lst:
        return False

    if digit == lst[0]:
        return True
    else:
        return digit_in_list(digit, lst[1:])


def intersec_aux(num1, num2, generated, index):

    if index == len(num1):
        return generated

    if digit_in_list(num1[index], num2):
        return intersec_aux(num1, num2, generated * 10 + num1[index], index + 1)

    return intersec_aux(num1, num2, generated, index + 1)


# 3.
def menor(num):
    # e: El número
    # s: dígito menor del numero
    # r: numero entero positivo
    num = abs(num)
    if isinstance(num, int):
        return menor_aux(num, num)
    else:
        return "Error"


def menor_aux(num, menor):
    if num == 0:
        return menor

    if num % 10 < menor:
        return menor_aux(num // 10, num % 10)

    return menor_aux(num // 10, menor)


# 4.
def todos_div(num, dig):
    # e: El número y el dígito
    # s: True o False, dependiendo si todos los digitos son divisibles
    # r: numero entero positivo
    num = abs(num)
    dig = abs(dig)
    if isinstance(num, int) and isinstance(dig, int):
        return todos_div_aux(num, dig)
    else:
        return "Error"


def todos_div_aux(num, dig):
    if num == 0:
        return True

    if (num % 10) % dig == 0:
        return True and todos_div_aux(num // 10, dig)

    return False


# 5.
def calificacion(lista):
    # e: La lista con las calificaciones
    # s: Promedio de todos las calificaciones, excepto la más alta y la más baja
    # r: Una lista válida, con números entre 0 y 10
    if isinstance(lista, list) and lista:
        return calificacion_aux(
            lista, 0, len(lista), get_lowest(lista, 10), get_highest(lista, 10)
        )
    else:
        return "Error"


def calificacion_aux(lista, index, length, lowest, highest):
    if index == length:
        return suma(lista, 0, length) / length
    if lista[index] == lowest or lista[index] == highest:
        if index == 0:
            new_l = lista[index + 1 :]
            return calificacion_aux(new_l, index, len(new_l), lowest, highest)

        new_l = lista[:index] + lista[index + 1 :]
        return calificacion_aux(new_l, index, len(new_l), lowest, highest)

    return calificacion_aux(lista, index + 1, length, lowest, highest)


def suma(l, index, length):
    if index == length:
        return 0

    return l[0] + suma(l[1:], index + 1, length)


def get_lowest(l, lowest):
    if l == []:
        return lowest

    if l[0] < lowest:
        return get_lowest(l[1:], l[0])

    return get_lowest(l[1:], lowest)


def get_highest(l, highest):
    if l == []:
        return highest

    if l[0] > highest:
        return get_highest(l[1:], l[0])

    return get_highest(l[1:], highest)


print(calificacion([2, 6, 10, 9, 9, 8, 1]))


# 6.
def invertir(lista):
    # e: lista
    # s: lista invertida
    # r: Una lista válida
    if isinstance(lista, list):
        return invertir_aux(lista, [], len(lista) - 1)


def invertir_aux(lista, nueva, indice):
    if not lista:
        return nueva

    return invertir_aux(lista[:indice], nueva + [lista[indice]], indice - 1)


# 7.
def cambie(lista, num1, num2):
    if isinstance(lista, list) and isinstance(num1, int) and isinstance(num2, int):
        return cambie_aux(lista, num1, num2)
    else:
        return "Error"


def cambie_aux(lista, num1, num2):
    if not lista:
        return []

    if lista[0] == num1:
        return [num2] + cambie_aux(lista[1:], num1, num2)
    else:
        return [lista[0]] + cambie_aux(lista[1:], num1, num2)


# 8.
def elimine(lista, num):
    if isinstance(lista, list) and isinstance(num, int):
        return elimine_aux(lista, num)
    else:
        return "Error"


def elimine_aux(lista, num):
    if not lista:
        return []

    if lista[0] == num:
        return lista[1:]

    return [lista[0]] + elimine_aux(lista[1:], num)


# 9.
def elimine_todos(lista, num):
    if isinstance(lista, list) and isinstance(num, int):
        return elimine_todos_aux(lista, num)
    else:
        return "Error"


def elimine_todos_aux(lista, num):
    if not lista:
        return []

    if lista[0] == num:
        return elimine_todos_aux(lista[1:], num)

    return [lista[0]] + elimine_todos_aux(lista[1:], num)
