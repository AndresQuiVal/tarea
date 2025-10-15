import random

def obtener_numero(mensaje):
    """
    Obtiene un número entero del usuario.
    """
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingresa un número válido.")



def generar_numero_aleatorio(minimo, maximo):
    """
    Genera un número aleatorio entre un mínimo y un máximo.
    """
    return random.randint(minimo, maximo)


def verificar_Intentos(intentos, numero_aleatorio):
    """
    Verifica si el usuario ha utilizado todos los intentos.
    """
    if intento < numero_secreto:
        print("Muy bajo")
    elif intento > numero_secreto:
        print("Muy alto")
    else:
        print("¡Correcto!")
        return True
    
    return False


def jugar():
    """
    Juega al juego.
    """
    limite_inferior = obtener_numero("Ingresa el límite inferior: ")
    limite_superior = obtener_numero("Ingresa el límite superior: ")

    if limite_inferior > limite_superior:
        print("El límite inferior debe ser menor que el límite superior")
        return

    numero_Secreto = generar_numero_aleatorio(limite_inferior, limite_superior)
    intentos_maximos = obtener_numero("Ingresa el número de intentos máximos: ")
    intentos = 0
    
    while intentos < intentos_maximos:
        intento = obtener_numero("Ingresa tu intento: ")
        intentos += 1
        if verificar_Intentos(intento, numero_Secreto):
            print("Has ganado")
            return
    
    print("Has perdido")


if __name__ == "__main__":
    jugar()