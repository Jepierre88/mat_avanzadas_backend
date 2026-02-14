import math


class PermutacionSimpleService:
    """Calcula la permutación simple de n elementos: P(n) = n!"""

    def execute(self, n: int) -> dict:
        if n < 0:
            raise ValueError("n debe ser un entero no negativo")

        resultado = math.factorial(n)

        return {
            "n": n,
            "resultado": resultado,
            "formula": f"P({n}) = {n}!",
            "explicacion": f"P({n}) = {n}! = {resultado}",
        }
