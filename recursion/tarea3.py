def get_beats(age):
    """
    Entrada: edad
    Salida: Numero de pulsaciones por c/10 segundos
    Restricciones: La edad debe ser un número entero entre 0 y 220
    
    
    ##Nota: Está claro que la edad debe ser >0, sin embargo el límite no es muy
    claro. Lo dejaré en 220 pues de otra forma no tendría sentido pues nadie puede
    tener pulsaciones negativas, pero si pueden tener pulsaciones iguales a cero. 
    Considero que depende un poco del punto de vista, un límite 
    """
    if isinstance(age, int) and 0 < age <= 220:
        return (220 - age)/10
    
    return 403
    
print(f"""
{get_beats(10)=}
{get_beats("Ramiro Briceño")=}
      """)

"""
>>> get_beats(10)=21.0
>>> get_beats("Ramiro Briceño")=403
"""



def exchange_to_dollars(colon):
    """
    Entrada: Colones
    Salida: Dolares
    Restricciones: Números positivos
    """
    
    if isinstance(colon, (int, float)) and colon > 0:
        return colon/600
    
    return 403

def exchange_to_colon(dollar):
    """
    Entrada: Dolares
    Salida: Colones
    Restricciones: Números positivos
    """
    if isinstance(dollar, (int, float)) and dollar > 0:
        return dollar*600
    
    return 403


my_exchange = 240000 # colones
get_dollars = exchange_to_dollars(my_exchange)

print(get_dollars, "$")
# >>> 400.0 $

revert_to_colon = exchange_to_colon(get_dollars)
print(revert_to_colon, "₡")
# >>> 240000.0 ₡

def celcius_to_farenheit(celsius):
    """
    Entrada: Celcius
    Salida: Farenheit
    Restricciones: Número válido mayor a −273,15 C
    """
    if isinstance(celsius, (int, float)) and celsius >= -273.15:
        return (9/5)*celsius + 32
    
    return 403

celcius_1 = 200
farenheit_1 = celcius_to_farenheit(celcius_1)

print(farenheit_1)
# >>> 392.0

def llave(gigabytes):
    """
    Entrada: gigabytes
    Salida: bytes
    Restricciones: Numeros válidos mayores a cero
    """
    if isinstance(gigabytes, (int, float)) and gigabytes > 0:
        return gigabytes * (1024**3)

    return 403

def get_area(base, height):
    """
    Entrada: La base y la altura
    Salida: Area del rectangulo
    Restricciones: Numero > 0 
    """
    if isinstance(base, (int, float)) and isinstance(height, (int, float)) and base > 0 and height > 0:
        return base*height
    
    return 403

def get_perimeter(base, height):
    """
    Entrada: La base y la altura
    Salida: Perímetro del rectangulo
    Restricciones: Numero > 0 
    """
    if isinstance(base, (int, float)) and isinstance(height, (int, float)) and base > 0 and height > 0:
        return 2*(base + height)
    
    return 403


my_rectangle_base = 12
my_rectangle_height = 10

print(f"""
{get_area(my_rectangle_base, my_rectangle_height)=}      
{get_perimeter(my_rectangle_base, my_rectangle_height)=}
      """)
# >>> get_area(my_rectangle_base, my_rectangle_height)=120
# >>> get_perimeter(my_rectangle_base, my_rectangle_height)=44


def adjunto(entero, digito):
    """
    Entrada: Número entero y dígito a adjuntar
    Salida: Los dígitos adjuntos
    Restricciones: 2 números enteros mayores a cero, el digito debe ser un único dígito
    # No pueden ser negativos pues darían lugar a irregularidades
    """
    if isinstance(entero, int) and isinstance(digito, int) and entero > 0 and 0 <= digito <= 9:
        return entero*10 + digito
    
    return 403

print(f"""
{adjunto(2003, 9)=}
{adjunto(192912, 0)=}
    """)
# adjunto(2003, 9)=20039
# adjunto(192912, 0)=1929120


def romano(numero):
    """
    Entrada: Número 
    Salida: Numero en romano
    Restricciones: Número entero entre 1 y 7
    """

    if isinstance(numero, int) and 1 <= numero <= 7:
        left = "I" * (numero % 5) if numero <= 5 else ""
        result = left + "V" * (numero//5) 
        return result if numero <= 5 else result + "I" * (7 - numero % 7)

print(f"""
{romano(6)=}
{romano(5)=}
{romano(3)=}
      """)
# romano(6)='VI'
# romano(5)='V'
# romano(3)='III'
