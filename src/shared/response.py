from typing import Any, TypeVar, Generic
from dataclasses import dataclass, asdict


def view_response(code: str, title: str, description: str, **extra: Any) -> dict:
    """Wrapper para respuestas de vista: devuelve el código fuente del servicio + metadata."""
    return {
        "type": "view",
        "title": title,
        "description": description,
        "code": code,
        **extra,
    }


def data_response(data: Any) -> dict:
    """Wrapper para respuestas de ejecución: devuelve el resultado tipado."""
    return {
        "type": "data",
        "data": data,
    }


def error_response(message: str, status: int = 400) -> tuple[dict, int]:
    """Wrapper para respuestas de error."""
    return {
        "type": "error",
        "message": message,
    }, status
