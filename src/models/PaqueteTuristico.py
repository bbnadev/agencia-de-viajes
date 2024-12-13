from models.Destino import Destino
from datetime import date


class PaqueteTuristico:
    def __init__(self, id: int = None, nombre: str = "", fechaInicio: date = None, fechaFin: date = None, costoTotal: float = 0.0):
        self._id = id
        self._nombre = nombre
        self._destinos = []
        self._fechaInicio = fechaInicio
        self._fechaFin = fechaFin
        self._costoTotal = costoTotal

# Getters

    def get_id(self) -> int:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def get_destinos(self) -> list:
        return self._destinos

    def get_fechaInicio(self) -> date:
        return self._fechaInicio

    def get_fechaFin(self) -> date:
        return self._fechaFin

    def get_costoTotal(self) -> float:
        return self._constoTotal

# Setters

    def set_id(self, id: int):
        self._id = id

    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def add_destino(self, destino: Destino):
        self._destinos.append(destino)

    def set_fechaInicio(self, FechaInicio):
        self._fechaInicio = FechaInicio

    def set_fechaFin(self, FechaFin):
        self._fechaFin = FechaFin

    def set_costoTotal(self, costoTotal):
        self._costoTotal = costoTotal
