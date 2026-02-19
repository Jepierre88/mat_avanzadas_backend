"""
Walkthrough (paso a paso) para el ejercicio de Técnicas de Conteo con dados.

Cada compañero puede crear su propio archivo de walkthrough siguiendo esta
estructura.  El archivo exporta dos cosas:

    CODE  – El código Python "educativo" que se muestra al usuario.
    STEPS – Lista de pasos que referencian líneas de CODE.

Ejemplo mínimo
───────────────
    CODE = \"\"\"x = 1
    y = x + 2\"\"\"

    STEPS = [
        {
            "lines": [1],
            "title": "Asignar x",
            "explanation": "Se crea la variable x con valor 1.",
            "variables": {"x": "1"},
        },
        {
            "lines": [2],
            "title": "Calcular y",
            "explanation": "Se suma 2 a x.",
            "variables": {"x": "1", "y": "3"},
        },
    ]
"""

# ─────────────────────────────────────────────────────────────────
#  CÓDIGO que se muestra en el visor del frontend
# ─────────────────────────────────────────────────────────────────
CODE = """\
from itertools import product

# Espacio muestral: todos los pares (azul, rojo)
dados = range(1, 7)
espacio = list(product(dados, dados))
total = len(espacio)

# Dobles: ambos dados iguales
dobles = [(b, r) for b, r in espacio if b == r]

# Suma es 4
suma_4 = [(b, r) for b, r in espacio if b + r == 4]

# Suma es 7 u 11
suma_7_11 = [(b, r) for b, r in espacio if b + r in (7, 11)]

# Azul muestra 2
azul_2 = [(b, r) for b, r in espacio if b == 2]

# Al menos uno muestra 2
al_menos_2 = [(b, r) for b, r in espacio if b == 2 or r == 2]

# Ninguno muestra 2
ninguno_2 = [(b, r) for b, r in espacio if b != 2 and r != 2]

# Suma par
suma_par = [(b, r) for b, r in espacio if (b + r) % 2 == 0]\
"""

# ─────────────────────────────────────────────────────────────────
#  PASOS del walkthrough  (las líneas son 1-indexed sobre CODE)
# ─────────────────────────────────────────────────────────────────

# No requiere parámetros del usuario (dados fijos 1-6)
TEST_PARAMS = {}

STEPS = [
    {
        "lines": [1],
        "title": "Importar herramientas",
        "explanation": (
            "Importamos product de itertools, que genera el producto "
            "cartesiano de dos o más iterables."
        ),
        "variables": {},
    },
    {
        "lines": [3, 4, 5, 6],
        "title": "Espacio muestral",
        "explanation": (
            "Definimos los valores de cada dado (1 a 6) y generamos "
            "todos los pares (azul, rojo) posibles. "
            "El total es 6 × 6 = 36."
        ),
        "variables": {
            "dados": "range(1, 7)",
            "espacio": "[(1,1), (1,2), …, (6,6)]",
            "total": "36",
        },
    },
    {
        "lines": [8, 9],
        "title": "Dobles",
        "explanation": (
            "Filtramos los pares donde ambos dados muestran el mismo número. "
            "Son (1,1), (2,2), (3,3), (4,4), (5,5), (6,6) → 6 resultados."
        ),
        "variables": {
            "dobles": "[(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)]",
            "len(dobles)": "6",
        },
    },
    {
        "lines": [11, 12],
        "title": "Suma es 4",
        "explanation": (
            "Buscamos pares cuya suma sea exactamente 4: "
            "(1,3), (2,2), (3,1) → 3 resultados."
        ),
        "variables": {
            "suma_4": "[(1,3), (2,2), (3,1)]",
            "len(suma_4)": "3",
        },
    },
    {
        "lines": [14, 15],
        "title": "Suma es 7 u 11",
        "explanation": (
            "Pares cuya suma es 7: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1) → 6. "
            "Suma 11: (5,6),(6,5) → 2. Total: 8 resultados."
        ),
        "variables": {
            "suma_7_11": "[(1,6), (2,5), …, (6,5)]",
            "len(suma_7_11)": "8",
        },
    },
    {
        "lines": [17, 18],
        "title": "Azul muestra 2",
        "explanation": (
            "Filtramos donde el dato azul (primera posición) es 2. "
            "Son (2,1), (2,2), (2,3), (2,4), (2,5), (2,6) → 6 resultados."
        ),
        "variables": {
            "azul_2": "[(2,1), (2,2), (2,3), (2,4), (2,5), (2,6)]",
            "len(azul_2)": "6",
        },
    },
    {
        "lines": [20, 21],
        "title": "Al menos uno muestra 2",
        "explanation": (
            "Pares donde el azul es 2 O el rojo es 2. "
            "Usamos inclusión-exclusión: 6 + 6 − 1 = 11 resultados."
        ),
        "variables": {
            "al_menos_2": "[(2,1), (2,2), …, (1,2), (3,2), …]",
            "len(al_menos_2)": "11",
        },
    },
    {
        "lines": [23, 24],
        "title": "Ninguno muestra 2",
        "explanation": (
            "Complemento del anterior: 36 − 11 = 25 resultados. "
            "Equivale a que ambos dados ∈ {1,3,4,5,6}, es decir 5 × 5."
        ),
        "variables": {
            "ninguno_2": "[(1,1), (1,3), …, (6,6)]",
            "len(ninguno_2)": "25",
        },
    },
    {
        "lines": [26, 27],
        "title": "Suma par",
        "explanation": (
            "La suma es par cuando ambos dados son pares o ambos impares. "
            "3 × 3 + 3 × 3 = 18 resultados."
        ),
        "variables": {
            "suma_par": "[(1,1), (1,3), …, (6,6)]",
            "len(suma_par)": "18",
        },
    },
]
