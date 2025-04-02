"""
Módulo que define clases para realizar operaciones matemáticas básicas y calcular promedios.

Clases:
    - OperacionesBasicas: Permite realizar sumas y restas.
    - CalculadoraPromedio: Calcula el promedio de una lista de valores.

Constantes:
    - NUMEROS: Lista de números utilizada para calcular el promedio.
    - NUM1, NUM2: Números utilizados en las operaciones básicas.
"""


class OperacionesBasicas:
    """Clase para realizar operaciones matemáticas básicas como suma y resta."""

    def __init__(self):
        """Inicializa la clase con un atributo resultado en 0."""
        self.resultado = 0

    def sumar(self, a, b):
        """Suma dos números y almacena el resultado.

        Args:
            a (float): Primer número.
            b (float): Segundo número.
        """
        self.resultado = a + b

    def restar(self, a, b):
        """Resta dos números y almacena el resultado.

        Args:
            a (float): Primer número.
            b (float): Segundo número.
        """
        self.resultado = a - b

    def obtener_resultado(self):
        """Obtiene el resultado de la última operación realizada.

        Returns:
            float: Resultado de la operación matemática.
        """
        return self.resultado


class CalculadoraPromedio:
    """Clase para calcular el promedio de una lista de valores."""

    def __init__(self, valores):
        """Inicializa la clase con una lista de valores.

        Args:
            valores (list of float): Lista de números a promediar.
        """
        self._valores = valores

    @property
    def valores(self):
        """Getter para obtener la lista de valores.

        Returns:
            list of float: Lista de números a promediar.
        """
        return self._valores

    @valores.setter
    def valores(self, nuevos_valores):
        """Setter para modificar la lista de valores.

        Args:
            nuevos_valores (list of float): Nueva lista de números a promediar.
        """
        if not nuevos_valores:
            raise ValueError("La lista de valores no puede estar vacía.")
        self._valores = nuevos_valores

    def calcular_promedio(self):
        """Calcula el promedio de los valores almacenados.

        Returns:
            float: Promedio de los valores.
        """
        suma = sum(self._valores)
        promedio_numeros = suma / len(self._valores)
        return promedio_numeros


# Variables globales
NUMEROS = [1, 2, 3, 4, 5]  # Lista de números para calcular el promedio
NUM1 = 10  # Primer número para operaciones básicas
NUM2 = 20  # Segundo número para operaciones básicas

# Ejecución principal
if __name__ == "__main__":
    # Usar la clase OperacionesBasicas
    operaciones = OperacionesBasicas()
    operaciones.sumar(NUM1, NUM2)
    print(f"El resultado de la suma es: {operaciones.obtener_resultado()}")

    operaciones.restar(NUM1, NUM2)
    print(f"El resultado de la resta es: {operaciones.obtener_resultado()}")

    # Usar la clase CalculadoraPromedio
    calculadora_promedio = CalculadoraPromedio(NUMEROS)
    promedio = calculadora_promedio.calcular_promedio()
    print(f"El promedio de los números es: {promedio}")
