from flask import Flask
from flask_cors import CORS
from src.controllers.hello_world_controller import hello_world_bp
from src.shared.exercise_factory import register_exercises

# ── Importar servicios ──
from src.services.permutacion_simple_service import PermutacionSimpleService

# ── Configuración de ejercicios ──
# Tú defines toda la metadata, tus compañeros solo crean el servicio con execute()
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
    # ↓ Agregar nuevos ejercicios aquí ↓
]


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(hello_world_bp)
    register_exercises(app, EXERCISES)

    return app
