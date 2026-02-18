from flask import Flask
from flask_cors import CORS
from src.controllers.hello_world_controller import hello_world_bp
from src.shared.exercise_factory import register_exercises

# ── Importar servicios ──
from src.services.permutacion_simple_service import PermutacionSimpleService
from src.services.operaciones_conjuntos_service import OperacionesConjuntosService
from src.services.tecnicas_conteo_service import TecnicasConteoService

EXERCISES = [
    {
        "service": PermutacionSimpleService,
        "route": "permutacion-simple",
        "title": "Permutación Simple",
        "description": "Calcula la permutación simple de n elementos. P(n) = n!",
        "params": [
            {"name": "n", "type": "int", "description": "Cantidad de elementos a permutar"},
        ],
    },
    {
        "service": OperacionesConjuntosService,
        "route": "operaciones-conjuntos",
        "title": "Operaciones con Conjuntos",
        "description": "Calcula unión, intersección y diferencias entre A y B.",
        "params": [
            {
                "name": "a",
                "type": "string",
                "description": "Conjunto A, separado por comas. Ej: 1,2,3",
            },
            {
                "name": "b",
                "type": "string",
                "description": "Conjunto B, separado por comas. Ej: 2,3,4",
            },
            {
                "name": "x",
                "type": "string",
                "description": "Elemento opcional para verificar pertenencia",
            },
        ],
        "view_extra": {
            "statement": (
                "Dado dos conjuntos finitos A y B (ingresados como listas separadas por coma), "
                "calcula: A ∪ B, A ∩ B, A − B, B − A y la diferencia simétrica A △ B. "
                "Opcional: para un elemento x, determina si x ∈ A y si x ∈ B."
            )
        },
    },
    {
        "service": TecnicasConteoService,
        "route": "tecnicas-conteo",
        "title": "Técnicas de Conteo (Dados)",
        "description": (
            "Se lanzan dos dados distinguibles (azul y rojo). "
            "Generar el espacio muestral y verificar condiciones de conteo."
        ),
        "params": [],
        "view_extra": {
            "statement": (
                "Contexto\n"
                "Se lanzan dos dados distinguibles: uno azul y uno rojo. El espacio muestral es:\n"
                "S = { (b,r) : b, r ∈ {1,…,6} }\n\n"
                "Ejercicios\n"
                "1. Determine el número de resultados que cumplen cada condición:\n"
                "o Total de resultados posibles\n"
                "o Resultados donde ambos dados muestran el mismo número, es decir, dobles.\n"
                "o Resultados cuya suma es 4\n"
                "o Resultados cuya suma es 7 u 11\n"
                "o Resultados donde el dado azul muestra 2\n"
                "o Resultados donde al menos uno muestra 2\n"
                "o Resultados donde ninguno muestra 2\n"
                "o Resultados cuya suma es par\n\n"
                "2. Implemente un programa en Python que genere el espacio muestral y permita verificar cada inciso automáticamente"
            )
        },
    },
    # ↓ Agregar nuevos ejercicios aquí ↓
]


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(hello_world_bp)
    register_exercises(app, EXERCISES)

    return app
