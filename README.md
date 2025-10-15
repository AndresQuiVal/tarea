# Juego de Adivinanza de Números

## 📝 Descripción
Este es un juego interactivo de adivinanza de números desarrollado en Python. El usuario debe adivinar un número aleatorio dentro de un rango definido y con un número limitado de intentos.

## 🎮 Características
- Rango de números personalizable (límite inferior y superior)
- Número de intentos configurable
- Validación de entrada del usuario
- Retroalimentación en cada intento ("Muy bajo" o "Muy alto")
- Uso de funciones lambda para generación de números aleatorios
- Código siguiendo las convenciones de Python (snake_case)

## 📋 Código Actual

```python
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
```

## 🚀 Cómo Ejecutar

```bash
python main.py
```

## 📖 Instrucciones de Uso

1. Ejecuta el programa
2. Ingresa el límite inferior del rango de números
3. Ingresa el límite superior del rango de números
4. Define el número máximo de intentos
5. Comienza a adivinar el número secreto
6. Recibirás pistas si tu número es "Muy bajo" o "Muy alto"
7. ¡Gana adivinando el número antes de quedarte sin intentos!

## 📂 Estructura del Proyecto

```
tarea/
│
├── main.py          # Archivo principal del juego
└── README.md        # Este archivo
```

## 🔧 Funciones Principales

### `obtener_numero(mensaje)`
- Solicita y valida la entrada de números enteros del usuario
- Maneja excepciones para entradas inválidas

### `generar_numero_aleatorio` (Lambda)
- Genera un número aleatorio entre el mínimo y máximo especificado
- Implementado como función lambda

### `verificar_intentos(intentos, numero_aleatorio)`
- Verifica el intento del usuario contra el número secreto
- Proporciona retroalimentación sobre si el número es mayor o menor
- Retorna `True` si el usuario adivinó correctamente

### `jugar()`
- Función principal que orquesta el flujo del juego
- Configura los parámetros del juego
- Gestiona el ciclo de intentos

## 📊 Historial de Desarrollo (Git)

### Repositorio
- **URL**: https://github.com/AndresQuiVal/tarea.git
- **Rama principal**: `main`
- **Rama de desarrollo**: `andres-2`

### Commits Recientes

```
5f37ea5 - Andres Quiroz Valdovinos (4 minutos atrás)
  └─ implementado lambda function para generar_numero_aleatorio y renombrar 
     variables y funciones para no usar camelCase, convencion de python

9136a9a - Andres Quiroz Valdovinos (14 minutos atrás)
  └─ Separado funcion principal en jugar() -> siendo la main, 
     verificar_intentos, generar_numero_aleatorio, y obtener_numero. 
     separacion de logica

4e3fc7b - Andres Quiroz Valdovinos (32 minutos atrás)
  └─ Added
```

### Gráfico de Branches

```
* 5f37ea5 (HEAD -> andres-2, origin/andres-2) 
│         implementado lambda function
│
* 9136a9a Separado funcion principal
│
* 4e3fc7b (origin/main, origin/HEAD, main) Added
```

## 🔄 Cambios Realizados

### Commit 1: Initial Commit (4e3fc7b)
- ✅ Versión inicial del proyecto

### Commit 2: Separación de Lógica (9136a9a)
- ✅ Refactorización del código en funciones modulares
- ✅ Creación de `jugar()` como función principal
- ✅ Separación de lógica en funciones independientes:
  - `obtener_numero()`
  - `generar_numero_aleatorio()`
  - `verificar_intentos()`
- ✅ Mejora en la organización del código

### Commit 3: Convenciones de Python y Lambda (5f37ea5)
- ✅ Implementación de función lambda para `generar_numero_aleatorio`
- ✅ Renombrado de variables y funciones de camelCase a snake_case
- ✅ Aplicación de convenciones de estilo PEP 8
- ✅ Mejora en la legibilidad del código

## 👨‍💻 Autor
**Andres Quiroz Valdovinos**

## 📝 Notas Técnicas
- Lenguaje: Python 3
- Convenciones: PEP 8 (snake_case)
- Módulos utilizados: `random`

## 🐛 Problemas Conocidos
- La función `verificar_intentos()` utiliza variables `intento` y `numero_secreto` que no están definidas en su scope (deberían pasarse como parámetros)

## 🔮 Mejoras Futuras
- [ ] Corregir el scope de variables en `verificar_intentos()`
- [ ] Agregar un sistema de puntuación
- [ ] Implementar niveles de dificultad
- [ ] Guardar historial de partidas
- [ ] Agregar interfaz gráfica (GUI)

---

*Proyecto desarrollado como parte de Tarea 2*

