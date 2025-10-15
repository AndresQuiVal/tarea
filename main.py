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


# Lambda

generar_numero_aleatorio = lambda minimo, maximo: random.randint(minimo, maximo)




def verificar_intentos(intentos, numero_aleatorio):
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

    numero_secreto = generar_numero_aleatorio(limite_inferior, limite_superior)
    intentos_maximos = obtener_numero("Ingresa el número de intentos máximos: ")
    intentos = 0
    
    while intentos < intentos_maximos:
        intento = obtener_numero("Ingresa tu intento: ")
        intentos += 1
        if verificar_intentos(intento, numero_secreto):
            print("Has ganado")
            return
    
    print("Has perdido")


if __name__ == "__main__":
    jugar()