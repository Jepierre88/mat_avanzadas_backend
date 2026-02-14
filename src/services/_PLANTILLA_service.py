"""
╔══════════════════════════════════════════════════════════════════╗
║              PLANTILLA PARA CREAR UN NUEVO EJERCICIO            ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  1. Copia este archivo con el nombre de tu ejercicio             ║
║     Ej: combinacion_simple_service.py                            ║
║                                                                  ║
║  2. Renombra la clase                                            ║
║     Ej: class CombinacionSimpleService:                          ║
║                                                                  ║
║  3. Implementa el método execute()                               ║
║     - Recibe los parámetros con type hints (n: int, r: int...)   ║
║     - Retorna un dict con los resultados                         ║
║     - Si hay error, lanza ValueError("mensaje")                 ║
║                                                                  ║
║  4. Avísale a Jean Pierre para que lo registre                   ║
║                                                                  ║
║  ¡Eso es todo! No te preocupes por rutas, APIs ni nada más.     ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""


class PlantillaService:

    def execute(self, n: int) -> dict:
        """
        Aquí va tu lógica matemática.
        - Usa type hints en los parámetros (n: int, r: float, etc.)
        - Retorna un dict con los resultados.
        - Si algo está mal, lanza: raise ValueError("mensaje de error")
        """
        resultado = n * 2  # ← Tu cálculo aquí

        return {
            "n": n,
            "resultado": resultado,
            "formula": f"f({n}) = {n} × 2",
            "explicacion": f"f({n}) = {n} × 2 = {resultado}",
        }
