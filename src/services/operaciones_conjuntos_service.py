from __future__ import annotations

from typing import List, Optional, Set


class OperacionesConjuntosService:
    """Ejercicio típico de conjuntos: operaciones básicas entre A y B."""

    @staticmethod
    def _parse_set(raw: str) -> Set[str]:
        if raw is None:
            raise ValueError("El conjunto no puede ser nulo")

        raw = str(raw).strip()
        if raw == "":
            return set()

        # Permite entrada tipo: "1,2,3" o "a, b, c"
        items = [item.strip() for item in raw.split(",")]
        return {item for item in items if item != ""}

    def execute(self, a: str, b: str, x: str = "") -> dict:
        """
        Recibe conjuntos como strings separados por coma.

        Params:
            a: "1,2,3"  (conjunto A)
            b: "2,3,4"  (conjunto B)
            x: elemento a verificar (opcional)
        """
        A = self._parse_set(a)
        B = self._parse_set(b)

        union = A | B
        interseccion = A & B
        dif_a_b = A - B
        dif_b_a = B - A
        simetrica = A ^ B

        x = str(x).strip()
        pertenece_a: Optional[bool] = (x in A) if x != "" else None
        pertenece_b: Optional[bool] = (x in B) if x != "" else None

        def as_list(s: Set[str]) -> List[str]:
            return sorted(s)

        return {
            "A": as_list(A),
            "B": as_list(B),
            "union": as_list(union),
            "interseccion": as_list(interseccion),
            "diferencia_A_B": as_list(dif_a_b),
            "diferencia_B_A": as_list(dif_b_a),
            "diferencia_simetrica": as_list(simetrica),
            "cardinalidades": {
                "|A|": len(A),
                "|B|": len(B),
                "|A∪B|": len(union),
                "|A∩B|": len(interseccion),
            },
            "x": x if x != "" else None,
            "pertenece_A": pertenece_a,
            "pertenece_B": pertenece_b,
        }
