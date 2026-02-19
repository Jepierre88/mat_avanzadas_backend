"""
Walkthrough (paso a paso) para Permutación Simple.

Exporta:
    CODE  – Código Python educativo que se muestra al usuario.
    STEPS – Lista de pasos referenciando líneas de CODE (1-indexed).
"""

CODE = """\
import math

def permutacion_simple(n):
    # Validar entrada
    if n < 0:
        raise ValueError("n debe ser >= 0")

    # Calcular factorial
    resultado = math.factorial(n)

    # Construir respuesta
    formula = f"P({n}) = {n}!"
    explicacion = f"P({n}) = {n}! = {resultado}"

    return {
        "n": n,
        "resultado": resultado,
        "formula": formula,
        "explicacion": explicacion,
    }\
"""

# Valores de prueba con los que se ilustra el tour
TEST_PARAMS = {"n": 5}

STEPS = [
    {
        "lines": [1],
        "title": "Importar math",
        "explanation": (
            "Importamos el módulo math de la biblioteca estándar "
            "para usar la función factorial."
        ),
        "variables": {},
    },
    {
        "lines": [3],
        "title": "Definir la función",
        "explanation": (
            "Creamos la función permutacion_simple que recibe un "
            "parámetro n (la cantidad de elementos a permutar)."
        ),
        "variables": {"n": "5"},
    },
    {
        "lines": [4, 5, 6],
        "title": "Validar entrada",
        "explanation": (
            "Verificamos que n no sea negativo. "
            "Los factoriales no están definidos para números negativos."
        ),
        "variables": {"n": "5"},
    },
    {
        "lines": [8, 9],
        "title": "Calcular factorial",
        "explanation": (
            "Usamos math.factorial(n) para calcular n!.\n"
            "Para n = 5: 5! = 5 × 4 × 3 × 2 × 1 = 120."
        ),
        "variables": {"n": "5", "resultado": "120"},
    },
    {
        "lines": [11, 12, 13],
        "title": "Construir respuesta",
        "explanation": (
            "Armamos strings descriptivos con la fórmula y la explicación "
            "del cálculo realizado."
        ),
        "variables": {
            "n": "5",
            "resultado": "120",
            "formula": '"P(5) = 5!"',
            "explicacion": '"P(5) = 5! = 120"',
        },
    },
    {
        "lines": [15, 16, 17, 18, 19, 20],
        "title": "Retornar resultado",
        "explanation": (
            "Devolvemos un diccionario con todos los datos: "
            "el valor de n, el resultado numérico, la fórmula y la explicación."
        ),
        "variables": {
            "n": "5",
            "resultado": "120",
            "formula": '"P(5) = 5!"',
            "explicacion": '"P(5) = 5! = 120"',
            "return": '{"n": 5, "resultado": 120, ...}',
        },
    },
]
