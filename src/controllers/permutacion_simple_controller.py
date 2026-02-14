from flask import Blueprint, jsonify, request
from src.services.permutacion_simple_service import PermutacionSimpleService
from src.shared.response import view_response, data_response, error_response

permutacion_simple_bp = Blueprint("permutacion_simple", __name__, url_prefix="/api/mat-inf")

service = PermutacionSimpleService()


@permutacion_simple_bp.route("/permutacion-simple/view", methods=["GET"])
def get_view():
    """Retorna el código fuente del servicio + metadata para armar la vista."""
    result = view_response(
        code=service.get_source_code(),
        title="Permutación Simple",
        description="Calcula la permutación simple de n elementos. P(n) = n!",
        params=[
            {"name": "n", "type": "int", "description": "Cantidad de elementos a permutar"},
        ],
    )
    return jsonify(result)


@permutacion_simple_bp.route("/permutacion-simple/execute", methods=["POST"])
def execute():
    """Ejecuta la permutación simple con los parámetros recibidos."""
    body = request.get_json(silent=True)

    if not body or "n" not in body:
        return jsonify(*error_response("El parámetro 'n' es requerido"))

    try:
        n = int(body["n"])
    except (ValueError, TypeError):
        return jsonify(*error_response("El parámetro 'n' debe ser un entero"))

    try:
        result = service.execute(n)
        return jsonify(data_response(result))
    except ValueError as e:
        return jsonify(*error_response(str(e)))
