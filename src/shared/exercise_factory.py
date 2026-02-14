"""
Fábrica de controladores para ejercicios.

Genera automáticamente los endpoints /view y /execute para cualquier
servicio de ejercicio. Los compañeros SOLO crean el servicio con execute().

Toda la configuración (ruta, título, params…) la define quien registra.

Uso en __init__.py:
    from src.shared.exercise_factory import register_exercises
    from src.services.mi_servicio import MiServicio

    register_exercises(app, [
        {
            "service": MiServicio,
            "route": "mi-ejercicio",
            "title": "Mi Ejercicio",
            "description": "Descripción...",
            "params": [
                {"name": "n", "type": "int", "description": "..."},
            ],
        },
    ])
"""

from __future__ import annotations

import inspect

from typing import Any, Dict, List, Union, get_args, get_origin, get_type_hints

from flask import Blueprint, jsonify, request
from src.shared.response import view_response, data_response, error_response


def create_exercise_blueprint(config: Dict[str, Any]):
    """
    Crea un Blueprint con /view y /execute a partir de un dict de configuración.

    config = {
        "service":     ClaseDelServicio,   ← la clase (no instancia)
        "route":       "permutacion-simple",
        "title":       "Permutación Simple",
        "description": "Calcula P(n) = n!",
        "params":      [{"name": "n", "type": "int", "description": "..."}],
    }
    """

    # ── Validar config ──
    required_keys = ["service", "route", "title", "description", "params"]
    for key in required_keys:
        if key not in config:
            raise KeyError(f"Falta la clave '{key}' en la configuración del ejercicio")

    service_class = config["service"]
    route_name = config["route"]
    title = config["title"]
    description = config["description"]
    params = config["params"]
    view_extra = config.get("view_extra", {})

    if view_extra is None:
        view_extra = {}
    if not isinstance(view_extra, dict):
        raise TypeError("'view_extra' debe ser un dict")

    bp = Blueprint(route_name, __name__, url_prefix="/api/mat-inf")
    service = service_class()

    def _type_label(t: Any) -> str:
        try:
            return t.__name__  # type: ignore[attr-defined]
        except Exception:
            return str(t)

    def _normalize_annotation(annotation: Any) -> Any:
        """Reduce Optional[T] / Union[T, None] to T for simple casting."""
        origin = get_origin(annotation)
        if origin is Union:
            args = [a for a in get_args(annotation) if a is not type(None)]
            if len(args) == 1:
                return args[0]
        return annotation

    def _coerce_value(value: Any, annotation: Any) -> Any:
        annotation = _normalize_annotation(annotation)

        if annotation is inspect.Parameter.empty or annotation is Any:
            return value

        # If already correct type, keep.
        try:
            if isinstance(annotation, type) and isinstance(value, annotation):
                return value
        except Exception:
            pass

        # Basic coercions
        if annotation is bool:
            if isinstance(value, bool):
                return value
            if isinstance(value, (int, float)):
                return bool(value)
            if isinstance(value, str):
                v = value.strip().lower()
                if v in {"true", "1", "yes", "y", "si", "sí"}:
                    return True
                if v in {"false", "0", "no", "n"}:
                    return False
            raise TypeError("bool")

        if annotation in (int, float, str):
            return annotation(value)

        # Fall back: try calling the annotation if it's callable
        if callable(annotation):
            return annotation(value)

        return value

    @bp.route(f"/{route_name}/view", methods=["GET"])
    def get_view():
        """Retorna el código fuente del servicio + metadata."""
        code = inspect.getsource(service_class)
        result = view_response(
            code=code,
            title=title,
            description=description,
            params=params,
            **view_extra,
        )
        return jsonify(result)

    @bp.route(f"/{route_name}/execute", methods=["POST"])
    def execute():
        """Ejecuta el servicio con los parámetros recibidos."""
        body = request.get_json(silent=True) or {}

        # Leer la firma de execute() para saber qué parámetros espera
        sig = inspect.signature(service.execute)
        try:
            # Resolve string annotations produced by `from __future__ import annotations`
            hints = get_type_hints(service.execute)
        except Exception:
            hints = {}
        kwargs = {}

        for param_name, param in sig.parameters.items():
            if param_name == "self":
                continue

            # Verificar que el parámetro fue enviado
            if param_name not in body:
                if param.default is inspect.Parameter.empty:
                    return jsonify(*error_response(f"El parámetro '{param_name}' es requerido"))
                else:
                    continue  # Tiene valor por defecto, no es obligatorio

            # Intentar convertir al tipo anotado
            value = body[param_name]
            annotation = hints.get(param_name, param.annotation)

            if annotation is not inspect.Parameter.empty:
                try:
                    value = _coerce_value(value, annotation)
                except (ValueError, TypeError):
                    return jsonify(
                        *error_response(
                            f"El parámetro '{param_name}' debe ser de tipo {_type_label(_normalize_annotation(annotation))}"
                        )
                    )

            kwargs[param_name] = value

        try:
            result = service.execute(**kwargs)
            return jsonify(data_response(result))
        except (ValueError, TypeError) as e:
            return jsonify(*error_response(str(e)))
        except Exception as e:
            return jsonify(*error_response(f"Error interno: {str(e)}", 500))

    return bp


def register_exercises(app, configs: List[Dict[str, Any]]):
    """
    Registra una lista de ejercicios en la aplicación Flask.

    Cada elemento de la lista es un dict con:
        service, route, title, description, params
    """
    for config in configs:
        bp = create_exercise_blueprint(config)
        app.register_blueprint(bp)
